FROM python:3.12.2

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "8000"]