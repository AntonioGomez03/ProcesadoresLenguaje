Para poder llevar a cabo la ejecución de nuestro procesador de lenguaje empleando JFLEX y CUP, se usará la IDE de Eclipse.

En este caso, se selecciona la opción "File ->Import Projects from File System" y se elige la ruta a la carpeta que contiene todos los archivos necesarios para nuestro procesador (carpeta llamada src dentro de la carpeta java). Asimismo, añadimos en el proyecto de Eclipse el jar externo de cup, que podemos descargar desde la página oficial y los jar externos referentes a Jackson (http://www.java2s.com/ref/jar/jar.html) para procesar los JSON . 

Para ejecutarlo, seleccionamos la opción del proyecto "properties->run as" y especificamos como argumento 
cualquiera de los archivos de ejemplo para el procesador en este lenguaje. En este caso, se imprimirá el JSON 
que sirve como lenguaje intermedio además de que escribirá un archivo llamado world.json donde se encuentra 
el output.

