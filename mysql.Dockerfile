FROM mysql:latest

WORKDIR /app
COPY database_schema.sql /app/database_schema.sql
CMD ["bash", "-c", "cat database_schema.sql | mysql -u root -p root"]