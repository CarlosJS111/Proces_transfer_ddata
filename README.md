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