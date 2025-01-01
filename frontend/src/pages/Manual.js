import Navbar from "../components/Navbar";
import InfoCard from "../components/InfoCard";
import logo from "../assets/logo_geocraft.png";
import terrainExample from "../assets/terrain_example.jpg";
import organizacionProyecto from "../assets/organizacion_proyecto.png";

const Manual = () => {

    const markdownContent = `
# 📝 Descripción del Lenguaje
A continuación, se enumeran y explican los componentes del lenguaje.

## 📚 Tipos de datos
En GeoCraft, los tipos de datos son fundamentales para la manipulación y el almacenamiento de la información. Los tipos de datos que se utilizan en este lenguaje son los siguientes:

### 🔢 INT
El tipo \`INT\` se utiliza para representar números enteros, tanto positivos como negativos. Este tipo es esencial para realizar operaciones artiméticas básicas, como suma, resta, multiplicación y división.

**Características**
- **Rango:** Puede almacenar valores comprendidos en el rango de  *-2,147,483,648* a *2,147,483,647*.
- **Operaciones:** Soporta operaciones aritméticas básicas.

**Ejemplo**
\`\`\`
INT a = 3
INT b = 2
INT c = a + b  // Resultado: 5
\`\`\`

### 📏 FLOAT
El tipo \`FLOAT\` permite la representación de números decimales.

**Características**
- **Rango:** Puede almacenar valores comprendidos en el rango de *-3.402823E38* a *3.402823E38*.
- **Operaciones:** Soporta operaciones aritméticas básicas.

**Ejemplo**
\`\`\`
FLOAT a = 23.5
FLOAT b = -74.006
FLOAT c = a + b  // Resultado: -50.506
\`\`\`

### 📜 STRING
El tipo \`STRING\` se utiliza para representar secuencias de caracteres o cadenas, permitiendo la manipulación de texto en el lenguaje.

**Características**
- **Contenido:** Puede contener letras, números, espacios, etc. que estén entre los símbolos \`"\`.
- **Operaciones:** Soporta operaciones de concatenación.

**Ejemplo**
\`\`\`
STRING nombre = "Carlos"
STRING apellido = "Pérez"
STRING nombre_apellido = nombre + " " + apellido // Resultado: "Carlos Pérez"
\`\`\`

## 🏷️ Descriptores
Los descriptores funcionan como bloques para la definición de los datos (presentando un enfoque muy parecido a la programación orientada a objetos). Cada descriptor está compuesto por una serie de atributos que permiten describir sus características. 

Existen 2 tipos de descriptores: Chunk y Gameobject.

### 🌴 GAMEOBJECT
El descriptor \`GAMEOBJECT\` está diseñado para definir modelos 3D que se dibujarán de manera procedural en el terreno, como árboles, rocas, hierba u otros elementos decorativos del entorno. Este descriptor permite especificar ciertos atributos que controlan la apariencia y distribución de estos objetos dentro del terreno.

**Atributos**
- **Ruta del modelo:** Define la ubicación del modelo 3D que se va a utilizar. En este caso, el ID "src/models/tree" se refiere a un archivo de un modelo 3D en esa ruta específica.
- **Densidad:** Define la densidad del objeto, lo que significa cuántos de estosobjetos se generarán en el área correspondiente del terreno. Un valor de 56 indica que habrá 56 instancias del objeto dispersas por el chunk.
- **Escala:** Este atributo controla la escala del modelo. Sin embargo, si se desea que algunos sean más grandes y otros más pequeños, creando una distribución más natural, se deberán definir los atributos MAX_SCALE y MIN_SCALE.

**Ejemplo**
\`\`\`
GAMEOBJECT object1 = GAMEOBJECT("src/models/tree", 10, 2.0)

// Ejemplo de definición de Gameobject con MAX_SCALE y MIN_SCALE
GAMEOBJECT object2 = GAMEOBJECT("src/models/rock", 5, 0.5, 1.5)
\`\`\`

### 🧩 CHUNK
Descriptor que representa una porción de terreno dentro de una escena. Este CHUNK tiene varios atributos clave que definen su apariencia y estructura, así como la posibilidad de contener objetos adicionales.

**Atributos**
- **Posición x:** Posición X dentro de la matriz de chunks de la escena.
- **Posición y:** Posición Y dentro de la matriz de chunks de la escena.
- **Escala:** Escala del Ruido Perlin para controlar el detalle (transición suave o abrupta entre montaña y llano).
- **Multiplicador de altura:** Multiplicador de altura para ajustar la elevación del terreno.
- **Textura:** Cadena de texto que hace referencia a la textura del terreno en el proyecto.
- **Lista de objetos:** Lista de objetos dentro del chunk (ver apartado de listas de descriptores).

**Ejemplo**
\`\`\`
CHUNK global_chunk1 = CHUNK(0,0,20.0, 7.5, "src/textures/grass", global_objects)
\`\`\`

## 📋 Listas
En GeoCraft es posible utilizar listas para dos tipos específicos de descriptores: \`CHUNK\` y \`GAMEOBJECT\`. Una vez creada una lista de uno de estos tipos, se podrán añadir elementos correspondientes a ese tipo. Para agregar una nueva instancia de Chunk o Gameobject a la lista, se utilizará la palabra reservada \`APPEND\`, seguida de la lista a la que se desea añadir el elemento y del elemento que se desea añadir.

**Ejemplo**
\`\`\`
CHUNK global_chunk1 = CHUNK(0, 0, 20.0, 7.5, "src/textures grass", global_objects)
LIST<CHUNK> global_chunks

APPEND global_chunks global_chunk1
\`\`\`

Además, la declaración de \`APPEND\` resulta especialmente útil para añadir descriptores de tipo \`CHUNK\` a una lista previamente declarada, particularmente cuando estos se crean dentro de un bucle. Esto permite generar múltiples chunks de manera eficiente y rápida.

## 🔁 Bucles

En nuestro lenguaje, existen dos tipos de bucles.

### ➰ Bucle convencional
GeoCraft presenta la posibilidad de utilizar bucles convencionales. La idea de este tipo de bucles consiste en realizar un número determinado de iteraciones desde un valor numerico \`i\` hasta otro valor \`n\`.

**Ejemplo**
\`\`\`
INT i = 0
FOR i FROM 0 TO 5 {
// Código del bucle
}
\`\`\`

### 🔃 Bucle para recorrer listas
El segundo tipo de bucle está diseñado para recorrer listas de elementos. Este tipo de bucle es muy util a la hora de representar en una escena los chunks contenidos en una lista.

**Ejemplo**
\`\`\`
FOR c in CHUNKS{
    // Código del bucle
}
\`\`\`

## 🧮 Operaciones básicas

- **Asignación (=):** Asigna una expresión a una variable de un tipo de dato específico.
- **Operaciones aritméticas:**
    - **Suma (+):** Suma dos elementos aritméticos.
    - **Resta (-):** Resta dos elementos aritméticos.
    - **Multiplicación (*):** Multiplica dos elementos aritméticos.
    - **División (/):** Divide dos elementos aritméticos.
- **Operación ADD:** Esta operación sirve para representar un chunk dentro de una escena asegurando que solo se puedan utilizar chunks que hayan sido previamente definidos y declarados. Asimismo, se puede utlizar esta operacion dentro de un bucle para poder dibujar los multiples chunks de una lista.

    \`\`\`
    // La variable chunks referencia a una lista de chunks previamente creada
    FOR c IN chunks {
        ADD c
    }
    \`\`\`

# 🛠️ Estructura principal de un programa GeoCraft
En un programa *GeoCraft*, se distinguen dos bloques principales: *setup* y *world*.

## ⚙️ Setup
Este bloque comienza con las palabras reservadas **DEFINE SETUP()** y se centra en la definición de objetos, variables y chunks globales que el usuario puede utilizar en las diferentes escenas que desee generar.

**Ejemplo**
\`\`\`
DEFINE SETUP(){
// Definición de variables globales
INT WIDTH_CHUNK = 20
INT LENGH_CHUNK = 

// Definición de objetos globales
GAMEOBJECT global_object1 = GAMEOBJECT("src/models/tree", 10, 2.0)
GAMEOBJECT global_object2 = GAMEOBJECT("src/models/rock", 5, 1.0)
LIST<GAMEOBJECT> global_objects = [global_object1, global_object2]

// Ejemplo de APPEND
APPEND global_objects GAMEOBJECT("src/models/house", 10, 2.0)

// Ejemplo de APPEND
GAMEOBJECT global_object3 = GAMEOBJECT("src/models/car", 10, 2.0)
APPEND global_objects global_object3

// Ejemplo de CHUNK
CHUNK global_chunk1 = CHUNK(0,0,20.0, 7.5, "src/textures/grass", global_objects)
}
\`\`\`

## 🗺️ World
El bloque **World** representa la metáfora del proyecto, actuando como la estructura organizativa principal que contiene todas las escenas del entorno. Este bloque comienza con las palabras reservadas **DEFINE WORLD(nombre)**, siendo *nombre* un parámetro que indica el nombre de la carpeta del proyecto generado.

Dentro de este bloque, se definen una o varias escenas, donde cada una de ellas corresponde a un archivo *.cs* individual. En estas escenas se llevan a cabo las definiciones de los chunks, así como la lógica del sistema, que incluye la creación de objetos, la utilización de bucles, y la gestión de listas. De este modo, **WORLD** sirve como un contenedor que agrupa y organiza todos los componentes necesarios para la contrucción y funcionamiento del entorno virtual.

**Ejemplo**
\`\`\`
DEFINE WORLD("Mi Mundo"){
// Definición de escena
DEFINE SCENE("Escena 1", WIDTH_CHUNK, LENGH_CHUNK){
// Definición de objetos
GAMEOBJECT object1 = GAMEOBJECT("src/models/tree", 15, 1.8)
GAMEOBJECT object2 = GAMEOBJECT("src/models/rock", 2, 1.2)
LIST<GAMEOBJECT> objects = [object1, object2]

// Creacion de 10 chunks con arboles y rocas
LIST<CHUNK> chunks
FOR i FROM 0 TO 10 {
CHUNK c = CHUNK(0,i,15.0, 10.0, "src/textures/mountain", objects)
APPEND chunks c
}

// Añaden los chunks generados previamente
FOR c IN chunks {
ADD c
}

// Añadir un chunk global
ADD global_chunk
}

DEFINE SCENE("Escena 2", WIDTH_CHUNK + 10, LENGH_CHUNK + 10){
// Definición de variables
INT n = 5
// Añadir un chunk global
ADD global_chunk
}
}
\`\`\`

# 🚀 Tecnologías Utilizadas

[![Python][Python-logo]][Python-url]
[![Java][Java-logo]][Java-url]
[![JFlex][JFlex-logo]][JFlex-url]
[![ANTLR4][ANTLR4-logo]][ANTLR4-url]
[![CUP][CUP-logo]][CUP-url]

[Python-logo]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Java-logo]: https://img.shields.io/badge/Java-DD0000?style=for-the-badge&logo=openjdk&logoColor=white
[Java-url]: https://www.java.com
[ANTLR4-logo]: https://img.shields.io/badge/ANTLR4-A80000?style=for-the-badge&logo=openjdk&logoColor=white
[ANTLR4-url]: https://www.antlr.org
[CUP-logo]: https://img.shields.io/badge/CUP-8E3A2D?style=for-the-badge&logo=openjdk&logoColor=white
[CUP-url]: http://www2.cs.tum.edu/projects/cup/
[JFlex-logo]: https://img.shields.io/badge/JFlex-1E7D3A?style=for-the-badge&logo=openjdk&logoColor=white
[JFlex-url]: http://jflex.de
`;
    return (
        <div className="page-container">
            <Navbar />
            <div className="manual-content-container">
                <h1>Manual</h1>
                <InfoCard markdownContent={markdownContent} />
            </div>
        </div>
    );
};

export default Manual;