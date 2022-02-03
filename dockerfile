FROM  python:3.9

COPY app.py .

RUN pip3 install requests
CMD python callMeBabe.py
