FROM python:3.6-slim
RUN pip install psycopg2-binary

COPY . /home
WORKDIR /home
CMD ["sh" , "program.sh"]
