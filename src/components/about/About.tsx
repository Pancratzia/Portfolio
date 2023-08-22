import "./About.scss";
import ProfileIMG from "../../assets/img/profile.jpg";

function About() {
  return (
    <div className="about" id="about">
      <div className="container">

      <div className="img-container">
        <img src={ProfileIMG} alt="Profile Image" className="img" />
      </div>

        <div className="text-container">Text</div>
      </div>
    </div>
  );
}

export default About;
