FROM redhat/ubi8

RUN yum install -y python3 python3-pip flask

COPY app.py /app.py

ENTRYPOINT [ "python3", "/app.py" ]



