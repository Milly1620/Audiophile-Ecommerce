FROM python:3.8-slim-buster AS python
WORKDIR /ecommerce
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /ecommerce/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django-prometheus
COPY . /ecommerce
# RUN python manage.py makemigrations
# RUN python manage.py migrate
EXPOSE 8000
# run python program
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]