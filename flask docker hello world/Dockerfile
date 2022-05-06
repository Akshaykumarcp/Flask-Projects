# base image
FROM python:alpine3.8
# copy current directory to /app directory
COPY . /app
# set current working directory
WORKDIR /app
# install dependencies
RUN pip install -r requirements.txt
# expose port 
EXPOSE 5000
# run the command
CMD python ./index.py



