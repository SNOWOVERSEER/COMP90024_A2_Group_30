FROM python:3.10

WORKDIR /app

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY Mastodon_Harvester.py /app/Mastodon_Harvester.py

CMD ["python", "/app/Mastodon_Harvester.py"]
