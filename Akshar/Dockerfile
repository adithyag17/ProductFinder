FROM python:3.11-slim 

WORKDIR /code 

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

CMD ["python3","final_scraper.py"]
