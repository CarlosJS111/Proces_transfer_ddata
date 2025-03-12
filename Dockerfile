# Imagen oficial de PostgreSQL
FROM postgres:13

# Copia el script de inicialización
COPY init.sql /docker-entrypoint-initdb.d/
