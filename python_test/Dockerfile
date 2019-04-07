FROM python:3.6-slim
RUN pip install psycopg2-binary

COPY . /home
WORKDIR /home

ENV POSTGRES_USER blue
ENV POSTGRES_PASSWORD blue
ENV POSTGRES_DB blue
ENV POSTGRES_CONTAINER pg
CMD ["sh" , "program.sh"]
