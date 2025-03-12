# Data Processing Project

Este proyecto implementa un proceso de carga, extracción, transformación y exportación de datos en PostgreSQL.

## Requisitos

- Docker y Docker Compose
- Python 3.8+
- PostgreSQL

## Instalación

1. Instala las dependencias con:

   ```bash
   pip install -r requirements.txt
   ```

2. Levanta la base de datos con Docker:

   ```bash
   docker-compose up -d
   ```

## Uso

### 1 Cargar datos

```bash
python scripts/load_data.py
```

### 2️ Extraer datos

```bash
python scripts/extract_data.py
```

### 3️ Transformar datos

```bash
python scripts/transform_data.py
```

### 4️ Exportar datos

```bash
python scripts/export_data.py
```

## Crear vista en PostgreSQL

Ejecuta:

```bash
psql -U admin -d transactions_db -f scripts/create_view.sql
```

---
### Mostrar total por día

```bash
python datos_d.py
```
### Pruebas Unitarias con SQLite

```bash
python -m pytest
```

## Procesamiento y Transferencia de Datos comentarios solicitados

Este proyecto implementa un proceso de carga, extracción, transformación y dispersión de datos en una base de datos estructurada, asegurando la correcta organización y consulta de la información.

## 1.1 Carga de Información
Requerimiento: Cargar el dataset de compras en una base de datos estructurada o no estructurada (MySQL, PostgreSQL, MongoDB, etc.).

Solución:
Se eligió PostgreSQL debido a su robustez, cumplimiento con ACID, capacidad para manejar grandes volúmenes de datos y su naturaleza de código abierto.

El script scripts/load_data.py crea las siguientes tablas:

companies: Contiene el identificador y nombre de la compañía.
charges: Contiene los datos de las transacciones, con las siguientes columnas:
id
company_id (clave foránea que relaciona con companies)
amount
status
created_at
updated_at
Problema encontrado:
Durante la carga del dataset en formato CSV, se detectaron problemas con el formato de las fechas y los valores nulos. Algunos registros tenían fechas en diferentes formatos (YYYY-MM-DD y MM/DD/YYYY), lo que generaba errores al insertarlos en PostgreSQL. Además, ciertos campos contenían valores vacíos en lugar de NULL, lo que causaba conflictos con las restricciones de la base de datos.

Solución implementada:

Se estandarizó el formato de fechas antes de la carga.
Se reemplazaron los valores vacíos por NULL en el preprocesamiento del archivo CSV.
Se utilizó pandas para leer y limpiar los datos antes de insertarlos en la base de datos.
Esto garantizó una carga de datos sin errores y con la estructura esperada.

## 1.2 Extracción
Requerimiento: Implementar un procedimiento de extracción de la información utilizando un lenguaje de programación y exportarla a un formato adecuado (CSV, Avro, Parquet, etc.).

Solución:
Se utiliza Python junto con la biblioteca pandas para extraer los datos desde la tabla charges en PostgreSQL.
El formato Parquet fue seleccionado por su eficiencia en compresión y velocidad, lo que lo hace ideal para grandes volúmenes de datos.

El script scripts/extract_data.py:

Conecta a la base de datos.
Ejecuta una consulta para extraer los datos.
Guarda los resultados en data/extracted_data.parquet.
Esto permite un acceso rápido y eficiente a los datos para su posterior procesamiento.

## 1.3 Transformación
Requerimiento: Transformar la información extraída para que cumpla con el esquema propuesto.

Solución:
Se usa Python y pandas para realizar las transformaciones necesarias.

El script scripts/transform_data.py:

Carga los datos desde data/extracted_data.parquet.
Renombra columnas según el esquema requerido (por ejemplo, paid_at se renombra a updated_at).
Maneja valores nulos y normaliza espacios en blanco para asegurar la calidad de los datos.
Guarda el resultado en data/transformed_data.parquet.
Este proceso garantiza que la información esté correctamente estructurada antes de insertarla en la base de datos.

## 1.4 Dispersión de la Información
Requerimiento: Insertar la información transformada en una base de datos estructurada, creando tablas relacionadas.

Solución:
Se mantiene el uso de PostgreSQL para aprovechar sus capacidades de gestión de datos relacionales.

El script scripts/export_data.py:

Conecta a la base de datos.
Inserta los datos transformados en la tabla charges (mientras que companies ya se carga en la etapa inicial).
Garantiza que la información del dataset esté correctamente distribuida y relacionada.
Esta estrategia asegura la integridad y disponibilidad de los datos para su análisis.

## 1.5 Creación de Vista SQL
Requerimiento: Diseñar una vista en la base de datos que permita visualizar el monto total transaccionado por día para cada compañía.

:Solución
Se creó el archivo scripts/create_view.sql, que define la vista transactions_summary.

Y para visualizar los datos: 

:Solución
Se creó el archivo python datos_d.py, que muestra el resultado por día.