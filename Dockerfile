# first layer is our python base image enabling us to run pip
FROM python:3.10

# create directory in the container for adding your files
WORKDIR /user/src/app 

# copy over the requirements file and run pip install to install the packages into your container at the directory defined above
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt --user 
COPY . . 

# enter entry point parameters executing the container
ENTRYPOINT ["python", "venv/main.py"] 

# exposing the port to match the port in the runserver.py file
EXPOSE 5555