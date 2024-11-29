import Navbar from "../componentes/Navbar";
import ProgramInput from "../componentes/ProgramInput";
import icon_image from "../assets/GeoCraft_icon_light.png";

const Generate = () => {
    return (
        <div className="page-container">
            <Navbar />
            <div className="content-container">
                <div class="fixed-image">
                    <img src={icon_image} alt="Icon" />
                </div>
                <ProgramInput />
            </div>

        </div>
    );
};

export default Generate;