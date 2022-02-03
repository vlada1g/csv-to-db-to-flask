FROM python:3.9

WORKDIR /app

COPY . /app
RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

# ENTRYPOINT ["python","./csv_to_db_alchemy.py"]

CMD ["python","-u", "./main.py"]