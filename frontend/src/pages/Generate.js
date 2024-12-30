import Navbar from "../components/Navbar";
import icon_image from "../assets/GeoCraft_icon_light.png";
import CodeEditor from "../components/CodeEditor";

const Generate = () => {
    return (
        <div className="page-container">
            <Navbar />
            <div className="content-container">
                <div className="fixed-image">
                    <img src={icon_image} alt="Icon" />
                </div>
                <div className="editor-container">
                    <CodeEditor />
                    <button className="generate-button">Generate</button>
                </div>
            </div>

        </div>
    );
};

export default Generate;