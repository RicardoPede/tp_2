# TRABAJO PRACTICO N° 2

## Configuración del Programa

El programa está desarrollado en Python, un lenguaje de programación de alto nivel que permite una programación eficaz de scripts y un desarrollo rápido de aplicaciones en diversas áreas en una amplia variedad de plataformas.

El programa utiliza las bibliotecas `pandas` y `sqlalchemy`. `Pandas` se utiliza para la manipulación y análisis de datos, especialmente para la lectura y escritura de archivos CSV. `SQLAlchemy` se utiliza para la interacción con la base de datos.
***
## Iniciación
***
Se crea un nuevo directorio para el proyecto: Esto se puede hacer desde la terminal con el comando `mkdir nombre_del_proyecto`.
Se navega al nuevo directorio: Se usa el comando `cd nombre_del_proyecto`.
Se crea un entorno virtual: Es opcional, pero es una buena práctica para aislar las dependencias del proyecto. Se hace con el comando `python -m venv venv`.
Se activa el entorno virtual: En Windows, se usa el comando `.\venv\Scripts\activate`.

## Dependencias

Para instalar las dependencias necesarias, se ejecuta el siguiente comando en la terminal:

```bash
pip install pandas sqlalchemy
```

***
## Ejecución del Proyecto
***

```bash
python create-csv-file.py
```

El programa comienza leyendo un archivo CSV ubicado en "data_base" que contiene información sobre las provincias argentinas y sus respectivas localidades utilizando pandas.

Luego, se establece una conexión con la base de datos utilizando sqlalchemy.

Los datos del archivo CSV se insertan en una tabla de la base de datos, mediante la utilización de MySQLdb.

Una vez que los datos se han importado a la base de datos, el programa realiza una serie de operaciones de manipulación de datos, incluyendo la agrupación de localidades por provincia.

Finalmente, cada grupo de localidades se exporta a un archivo con el nombre de cada provincia dentro del directorio csv_province.

***
## Criterios de Evaluación
***
El programa será evaluado en base a los siguientes criterios:

### Correcta lectura del archivo CSV.
### Creación de una tabla en la base de datos con las columnas adecuadas.
### Correcta inserción de datos en la base de datos.
### Manipulación eficaz de los datos una vez en la base de datos, especialmente la agrupación por provincia.