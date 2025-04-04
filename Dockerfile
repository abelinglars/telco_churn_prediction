FROM python:3.13

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY src/main.py /app/main.py
COPY ./rf.sav /rf.sav
CMD ["fastapi", "run", "/app/main.py", "--port", "80"]
