import Navbar from "../components/Navbar";
import icon_image from "../assets/GeoCraft_icon_light.png";
import CodeEditor from "../components/CodeEditor";

const Generate = () => {

    const handleGenerateClick = () => {
        // Obtener el código del componente CodeEditor
        let code = document.querySelector(".code-editor-textarea").value;

        // Endpoint de la API /generate_project
        fetch("http://localhost:8000/generate_project", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code
            })
        })
            .then(response => {
                // Verificar si la respuesta es exitosa
                if (!response.ok) {
                    throw new Error("Error al generar el proyecto");
                }

                // Obtener el nombre del archivo desde los encabezados
                const contentDisposition = response.headers.get("Content-Disposition");
                const fileNameMatch = contentDisposition && contentDisposition.match(/filename="([^"]+)"/);
                const fileName = fileNameMatch ? fileNameMatch[1] : "project.zip";

                // Convertir la respuesta a blob
                return response.blob().then(blob => ({ blob, fileName }));
            })
            .then(({ blob, fileName }) => {
                // Crear un enlace para descargar el archivo
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement("a");
                a.href = url;
                a.download = fileName; // Usar el nombre del archivo obtenido
                document.body.appendChild(a);
                a.click();
                a.remove();
                window.URL.revokeObjectURL(url); // Limpiar URL del blob
            })
            .catch(error => {
                console.error("Error:", error);
            });
    };


    return (
        <div className="page-container">
            <Navbar />
            <div className="generate-content-container">
                <h1>Generate Unity World</h1>
                <div className="generate-code-content-container">
                    <div className="fixed-image">
                        <img src={icon_image} alt="Icon" />
                    </div>
                    <div className="editor-container">
                        <CodeEditor />
                        <button className="generate-button"
                            onClick={handleGenerateClick}>Generate</button>
                    </div>
                </div>
            </div>

        </div >
    );
};

export default Generate;