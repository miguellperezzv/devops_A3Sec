# Ejecución del proyectp



## Pasos para Ejecutar el Proyecto en Docker



### 1. Configuración del Compose YAML

En el archivo `docker-compose.yml`, hay dos servicios definidos: `flask_app` y `flask_db`. 

### 2. Construcción de la Imagen de la Aplicación (Opcional)

### 3\. Ejecución de los Contenedores

Para ejecutar los contenedores definidos en el archivo `docker-compose.yml`, utiliza el siguiente comando:

bashCopy code

`docker-compose up`

Esto iniciará los contenedores `flask_app` y `flask_db`, y tu aplicación Flask estará disponible en el puerto 5000 en tu sistema local.

### 4\. Acceso a la Aplicación

Abre tu navegador web e ingresa la dirección `http://localhost:5000/` para acceder a la aplicación web ejecutándose dentro del contenedor Docker. Dependiendo de cómo haya configurado tu aplicación, podrías acceder a otros endpoints o servicios proporcionados por tu proyecto Flask.



```bash
docker-compose build



