FROM mysql:latest
COPY database_schema.sql ~/database_schema.sql
ENTRYPOINT ["cat database_schema.sql | mysql -u root -p root"]