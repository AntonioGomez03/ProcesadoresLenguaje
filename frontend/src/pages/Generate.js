import Navbar from "../components/Navbar";
import icon_image from "../assets/GeoCraft_icon_light.png";
import CodeEditor from "../components/CodeEditor";

const Generate = () => {

    const handleGenerateClick = () => {
        // Obtain the code from the CodeEditor component
        let code = document.querySelector(".code-editor-textarea").value;
        // Api endpoint /generate_project
        fetch("http://localhost:8000/generate_project", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code
            })
        }).then(response => response.json())
            .then(data => {
                // If the response is successful, redirect to the download page
                if (data.status === "success") {
                    window.location.href = "/download";
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
    }


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