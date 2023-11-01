FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

RUN apt-get -y update
RUN apt-get -y install vim

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN useradd -r nginx
RUN usermod -a -G root nginx

# /var/log/gunicorn 폴더 생성
RUN mkdir -p /var/log/gunicorn

# 쓰기 가능한 권한 설정
RUN chmod -R 777 /var/log/gunicorn

EXPOSE 8000


CMD gunicorn --bind 0.0.0.0:8000 config.wsgi --timeout 300
#    --log-level=debug --access-logfile /var/log/gunicorn/access.log --log-file /var/log/gunicorn/error.log
#CMD ["python", "mdm_project/manage.py", "runserver", "0.0.0.0:8000"]