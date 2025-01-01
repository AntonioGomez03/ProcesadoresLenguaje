import Navbar from "../components/Navbar";
import InfoCard from "../components/InfoCard";
import logo from "../assets/logo_geocraft.png";
import terrainExample from "../assets/terrain_example.jpg";
import organizacionProyecto from "../assets/organizacion_proyecto.png";

const About = () => {

    const markdownContent = `
# <img src="${logo}" alt="Emoji" width="30" style="vertical-align: middle;" /> GeoCraft

GeoCraft es un lenguaje que permite simplificar y automatizar el proceso de creación de terrenos 3D en Unity.

<br />
<div align="center">
    <img src="${logo}" alt="Logo de GeoCraft" width="20%" />
    <br>
    <em>Logo de GeoCraft</em>
</div>
<br />

El objetivo de este proyecto es desarrollar una herramienta que utilice este lenguaje para complementar el trabajo de diseñadores en la creación de terrenos de manera procedural en Unity. 

La utilidad de esta herramienta radica en su capacidad para facilitar la generación inicial de entornos y modelos que pueden ser tomados como base sobre la cual trabajar.

## 📚 Fundamentos
Este lenguaje está basado en el modelo de trabajo de Unity y en la generación procedural de terrenos (como en el videojuego **Minecraft**, basado en **chunks**).

<br />
<div align="center">
    <img src="${terrainExample}" alt="Ejemplo de GeoCraft" width="95%" />
</div>
<br />

### ⚡¿Qué es la generación procedural?
Técnica utilizada en gráficos por computador y videojuegos para crear escenas de manera automática, sin necesidad de diseñarlos manualmente, en base a unas directrices.

### 🧩¿Qué es un chunk?
Se refiere a una porción o bloque de datos que se maneja como una sola unidad. En el contexto de la generación de terrenos, un chunk es una sección del mundo virtual que se carga y se procesa de manera independiente.

### 🛠️ Metodología de Trabajo
El objetivo del proyecto es generar terrenos 3D en Unity de manera sencilla usando nuestro lenguaje. Nos basaremos en el concepto de chunks, que son secciones o "trozos" del terreno que se pueden manejar de manera individual.

El lenguaje también permitirá la generación de objetos prefabricados, como árboles y vegetación, dentro de cada chunk.

## 📊 Organización del Proyecto
La idea del proyecto consiste en tomar un código escrito en nuestro lenguaje específico y pasarlo a través de un procesador de lenguaje diseñado para este fin. Al ejecutar este proceso, se generará una carpeta que contendrá subcarpetas para cada escena definida en el código. Cada una de estas escenas se traducirá en un archivo de código con la extensión .cs, el cual, al ser ejecutado en Unity, creará automáticamente la escena correspondiente en el entorno 3D.

<br />
<div align="center">
    <img src="${organizacionProyecto}" alt="Organización del Proyecto" width="300" />
</div>
<br />

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
            <div className="about-content-container">
                <h1>About</h1>
                <InfoCard markdownContent={markdownContent} />
            </div>
        </div>
    );
};

export default About;