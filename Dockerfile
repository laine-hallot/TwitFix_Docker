FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
COPY app/requirements.txt /
RUN pip3 install -r /requirements.txt
CMD	["python3", "wsgi.py"]