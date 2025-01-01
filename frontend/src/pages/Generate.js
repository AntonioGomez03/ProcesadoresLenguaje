import Navbar from "../components/Navbar";
import icon_image from "../assets/GeoCraft_icon_light.png";
import CodeEditor from "../components/CodeEditor";

const Generate = () => {

    const handleGenerateClick = () => {
        // Obtain the code from the CodeEditor component
        let code = document.querySelector(".code-editor-textarea").value;
        console.log(code);
    }


    return (
        <div className="page-container">
            <Navbar />
            <div className="generate-content-container">
                <div className="fixed-image">
                    <img src={icon_image} alt="Icon" />
                </div>
                <div className="editor-container">
                    <h1>Generate Unity World</h1>
                    <CodeEditor />
                    <button className="generate-button"
                        onClick={handleGenerateClick}>Generate</button>
                </div>
            </div>

        </div >
    );
};

export default Generate;