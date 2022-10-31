FROM python:3.7-buster

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y build-essential

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN "python" "db_init.py"

EXPOSE 5000

CMD [ "python", "./vulpy.py" ]