FROM python:3.6-alpine


RUN apk update
ADD src/ /app
WORKDIR /app
RUN pip install -r requirements.txt && \ 
    python manage.py migrate

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD ["manage.py", "runserver", "0.0.0.0:5000"]


