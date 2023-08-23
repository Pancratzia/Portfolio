import "./Projects.scss";
import { SiGithub } from "react-icons/si";
import { FaRegEye } from "react-icons/fa";

import "../../assets/styles/variables.scss";
import "../../assets/styles/responsive.scss";

function Projects() {
  return (
    <div className="projects">
      <h2 className="h2-title">Projects</h2>

      <div className="container">
        <div className="projects-container">
          <div className="card">
            <div className="card-header">
              <h3>Project Title</h3>
              <div className="img">
                <img src="https://via.placeholder.com/300" alt="" />
              </div>
            </div>

            <div className="card-body">
              <p>
                Some quick example text to build on the card title and make up
                the bulk of the card's content.
              </p>
              <span>00/00/0000</span>
            </div>

            <div className="card-footer">
              <a href="#"><SiGithub /></a>
              <a href="#"><FaRegEye /></a>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}

export default Projects;
