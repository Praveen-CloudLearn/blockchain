class Distributor:
    
    def __init__(self):
        self.distributors_closeTransactions={}
        
    def add_transaction(self,blockchain,sender,hospital,itemcode,lot,quantity):
        message=''
        index=-1
        distributor_transactions=blockchain.iterate_chain('receiver',sender)
        if sender in self.distributors_closeTransactions:
            close_transactions=self.distributors_closeTransactions[sender]
            distributor_transactions=distributor_transactions.difference(close_transactions)
        if len(distributor_transactions)==0:
            message='Distributor: '+sender+' does not have any open transactions'
            return index,message
        itemcodeset=blockchain.iterate_chain('itemcode',itemcode)
        LOTset=blockchain.iterate_chain('LOT',lot)
        d_itemcodeset=distributor_transactions.intersection(itemcodeset)
        d_LOTset=distributor_transactions.intersection(LOTset)
        d_itemcode_LOTset=d_itemcodeset.intersection(LOTset)
        print(d_itemcode_LOTset)
        if len(d_itemcodeset)==0:
            message='Provided Item code is not present in the blockchain for distributor: '+sender
            return index,message
        elif len(d_LOTset)==0:
            message='Provided LOT is not present in the blockchain for distributor: '+sender
            return index,message
        elif len(d_itemcode_LOTset)==0:
            message='Combination of LOT and item code is not present in the blockchain for distributor: '+sender
            return index,message
        for bt in d_itemcode_LOTset:
            block_transaction=bt
            b=int(bt[1])
            t=int(bt[-1])
        if blockchain.chain[b]['transactions'][t]['quantity'] < quantity:
            message='Sufficient quantity of vaccines is not present for LOT: '+lot+' itemcode: '+itemcode
            return index,message
        if sender not in self.distributors_closeTransactions:
            self.distributors_closeTransactions[sender]=set({block_transaction})
        else:
            self.distributors_closeTransactions[sender].add(block_transaction)
        index=blockchain.add_transaction(sender,hospital,itemcode,lot,quantity)
        if blockchain.chain[b]['transactions'][t]['quantity'] > quantity:
            index=blockchain.add_transaction(sender,sender,itemcode,lot,blockchain.chain[b]['transactions'][t]['quantity']-quantity,lot_expdate)
        return index,message
    
#    def get_all_transactions():
#    def get_all_closed_transactions():
#    def get_all_open_transactions():
