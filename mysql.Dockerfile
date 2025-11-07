FROM mysql:latest

WORKDIR /app
COPY database_schema.sql /app/database_schema.sql
ENTRYPOINT ["cat database_schema.sql | mysql -u root -p root"]