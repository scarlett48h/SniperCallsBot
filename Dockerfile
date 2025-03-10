FROM python:3.12.3-alpine3.20
WORKDIR /var/www/coinsniper
COPY . .
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
CMD python main.py