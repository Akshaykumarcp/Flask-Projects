# pull python image from docker hub (also has OS)
FROM python:3
# inside the OS that has python installed from above, set current working directory
WORKDIR /usr/src/app
# copy req.txt file to current working dir
COPY requirements.txt .
# say the OS machine to run below command
RUN pip install --no-cache-dir -r requirements.txt
# copy all the files present in local directory to current working directory which is set above
COPY . .
# finally run the command
CMD [ "python", "app.py" ]
