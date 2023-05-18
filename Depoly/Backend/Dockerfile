# Python iso
FROM python:3

# working dirtary
WORKDIR /app

# cpy the file to the docker
COPY . /app/

# install requirements
RUN pip install -r requirements.txt

# run Django
CMD python manage.py runserver 0.0.0.0:8000
