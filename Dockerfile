FROM python:alpine3.10
WORKDIR /app 
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5001
EXPOSE 5002
CMD python ./Manufacture_controller_5001.py
CMD python ./Distributor_controller_5002.py
CMD python ./Hospital_controller_5003.py


#COPY requirements.txt /app/requirements.txt

#ENTRYPOINT ["python", "./Manufacture_controller_5001.py"]
#ENTRYPOINT ["python", "./Distributor_controller_5002.py"]
#ENTRYPOINT ["python", "./Hospital_controller_5003"]
