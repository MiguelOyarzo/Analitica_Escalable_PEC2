# Analitica_Escalable_PEC2
Miguel Oyarzo Altamirano
PEC2 de curso analítica escalable. UAH

Directorios


1-Pipeline: este contiene un archivo ipynb y la base de datos de titanic.csv.
Se implementan dos pipeline, uno de transformación de variables y otra de implementación de un modelo de regresión logística para predecir si los pasajeros sobreviven o no, en base a las variables de clase, sexo, edad e importe pagado.

2-Algoritmo empaquetado: contiene dos carpetas. La primera denominada plk, contiene el pipeline del modelo antes mencionado en formato plk. En cambio, la carpeta Pipy, contiene los archivos utililzados para subir el algoritmo a pip en el siguiente link https://pypi.org/project/titanic-ML-Miguel-OyarzoA/#files. Este puede ser descargado a traves del archivo https://files.pythonhosted.org/packages/e3/9c/9e8e737976144d02d03926772696402decf32dfa4ed7d86ee4f79fed5e4d/titanic_ML_Miguel_OyarzoA-1.0.0.tar.gz y ser instalado con el siguiente comando: pip install titanic-ML-Miguel-OyarzoA

3-Flask: En resumen, el proceso de contenerización del algoritmo utilizado se divide en dos partes: una que utiliza Docker para ejecutar el programa app.py de forma interactiva, y otra que utiliza Flask para construir una aplicación de predicción de supervivencia del Titanic como una API. En la primera parte, se genera una imagen de Docker a partir de los archivos del directorio Flask, que incluyen el programa app.py y el modelo en formato pkl. Esta imagen se publica en Docker Hub y se puede descargar y ejecutar en un contenedor Docker.

Para generar la imagen, se utilizó el comando: docker build -t analitica-escalable/ml-appmo .    

En la segunda parte, se utiliza la biblioteca Flask para construir una aplicación web. La aplicación sirve un formulario HTML en la ruta raíz, donde se pueden ingresar las características necesarias para realizar predicciones de supervivencia del Titanic. El servicio responde tanto a peticiones POST como GET. Para utilizar la aplicación, se puede enviar una petición POST utilizando el formulario web, especificando los valores correctos para obtener una predicción precisa. La respuesta se mostrará en el mismo formulario HTML. 

Para la ejecución del contenedor: docker run -p 5000:5000 tenzingdorje/ml-appmo:tag

La aplicación de Flask se empaqueta en una imagen de Docker, se publica en Docker Hub y se puede descargar y ejecutar en un contenedor Docker utilizando comandos similares a los de la primera parte.

Para publicarlo en DockerHub se uso:  docker push tenzingdorje/ml-appmo:tag
Para descargarlo: docker pull tenzingdorje/ml-appmo

En ambos casos, al ejecutar el contenedor Docker, se necesita mapear un puerto local para establecer la conexión con el servicio web del contenedor. Una vez que el contenedor esté en funcionamiento, se puede acceder a la aplicación web a través de una URL en el navegador.





En resumen, este proceso de contenerización permite utilizar el algoritmo de predicción de supervivencia del Titanic de manera fácil y portable, encapsulándolo en contenedores de Docker que se pueden ejecutar en diferentes entornos.
