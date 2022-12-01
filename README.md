# Prueba tuHabi 
El proyecto se desarrolla como una arquitectura de microservicios, esto con el fin de tener servicios independientes, ligeras e implementables cada con su propio objetivo dentro de la aplicación general.
Las herramientas utilizadas son:
```
mysql-connector-python==8.0.31
fastapi==0.88.0
python-dotenv==0.21.0
uvicorn==0.20.0
```

Primero iniciaré configurando las librerías necesarias. Realizaré una estructura de carpetas que permita tener ordenado el codigo, de manera que pueda ser modular.
Posteriormente realizaré la configuración a la base de datos, haŕe algunas pruebas de conexión.
Una vez que ya tenga configurada la conexión a la base de datos, crearé la consulta SQL para poder filtrar de acuerdo a la solicitud del usuario y con ello crearé las primeras pruebas unitarias, para ir comprobando los resultados obtenidos con los resultados esperados.

