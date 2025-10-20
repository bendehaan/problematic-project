FROM python:3.14

RUN apt-get update
RUN apt-get install -y build-essential

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN "python" "db_init.py"

EXPOSE 8080

CMD [ "python", "./vulpy.py" ]
