# Trabajo final — Herramientas para Inteligencia Artificial

## Descripción
Análisis del dataset AI4I 2020 mediante Google Colab, Pandas, SQLite y Matplotlib.

El CSV original contiene 10 000 registros y 14 columnas. SQLite contiene dos tablas
relacionadas (`maquinas` y `operaciones`). El dataset final consultado contiene
10 000 registros y 9 columnas.

## Archivos esperados
- `Trabajo_Final_Herramientas_IA_EXPLICADO.ipynb`: notebook completo con código y explicaciones.
- `ai4i2020.csv`: CSV original descargado desde UCI.
- `mantenimiento_industrial.sql`: exportación SQL de la base de datos.
- `mantenimiento_industrial.db`: archivo SQLite.
- `dataset_final.csv`: consulta integrada de las dos tablas.
- `visualizaciones/`: cuatro gráficos PNG.
- `crear_base_datos.py`: script de creación de la base, útil para la rúbrica.
- `wiki/Home.md`: borrador del informe para publicar en la Wiki de GitHub.

## Cómo ejecutar
1. Abrir `Trabajo_Final_Herramientas_IA.ipynb` con Google Colab.
2. Ejecutar las celdas en orden desde arriba. Se descarga el CSV público.
3. Revisar la creación de las tablas, consultas y gráficos.
4. Descargar los archivos SQL, DB, dataset final y figuras para el repositorio.
5. Publicar el contenido de `wiki/Home.md` en la pestaña Wiki de GitHub.

## Importante
El archivo SQL es el respaldo del esquema y los registros; no representa una segunda
fuente independiente. El CSV y las tablas SQLite derivan de AI4I 2020.

## Fuente del dataset
UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset
