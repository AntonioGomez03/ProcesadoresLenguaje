# <img src="assets/logo.png" alt="Emoji" width="30" style="vertical-align: middle;" /> GeoCraft

GeoCraft es un lenguaje que permite simplificar y automatizar el proceso de creación de terrenos 3D en Unity.

![Logo de GeoCraft](assets/logo.png)
<br>
*Logo de GeoCraft*

El objetivo de este proyecto es desarrollar una herramienta que utilice este lenguaje para complementar el trabajo de diseñadores en la creación de terrenos de manera procedural en Unity. 

La utilidad de esta herramienta radica en su capacidad para facilitar la generación inicial de entornos y modelos que pueden ser tomados como base sobre la cual trabajar.

## 📚 Fundamentos
Este lenguaje está basado en el modelo de trabajo de Unity y en la generación procedural de terrenos (como en el videojuego **Minecraft**, basado en **chunks**).
![chunk](https://github.com/user-attachments/assets/743dea48-891c-4280-a4b9-ea0cc4def051)
<br>
### ⚡¿Qué es la generación procedural?
Técnica utilizada en gráficos por computador y videojuegos para crear escenas de manera automática, sin necesidad de diseñarlos manualmente, en base a unas directrices.
<br><br>
### 🧩¿Qué es un chunk?
Se refiere a una porción o bloque de datos que se maneja como una sola unidad. En el contexto de la generación de terrenos, un chunk es una sección del mundo virtual que se carga y se procesa de manera independiente.
<br><br>

### 🛠️ Metodología de Trabajo
El objetivo del proyecto es generar terrenos 3D en Unity de manera sencilla usando nuestro lenguaje. Nos basaremos en el concepto de chunks, que son secciones o "trozos" del terreno que se pueden manejar de manera individual.

El proyecto estará dividido en escenas y cada una representará un modelo 3D diferente y estará compuesta por múltiples chunks, lo que permite una organización modular.

La idea es que cada chunk puede ser trabajado de forma independiente, lo que significa que se pueden modificar sus características, como el tamaño, la forma, la textura y otros atributos sin afectar a los demás. Esta modularidad permite a los desarrolladores personalizar y ajustar cada parte del terreno según las necesidades específicas del proyecto.

El lenguaje también permitirá la generación de objetos prefabricados, como árboles y vegetación, dentro de cada chunk. 
<br><br>

### 📊 Organización del proyecto
La idea del proyecto consiste en tomar un código escrito en nuestro lenguaje específico y pasarlo a través de un procesador de lenguaje diseñado para este fin. Al ejecutar este proceso, se generará una carpeta que contendrá subcarpetas para cada escena definida en el código. Cada una de estas escenas se traducirá en un archivo de código con la extensión .cs, el cual, al ser ejecutado en Unity, creará automáticamente la escena correspondiente en el entorno 3D.
![image](https://github.com/user-attachments/assets/72d9df9c-a4ad-4697-b585-c3b3dc0447a9)
<br><br><br>