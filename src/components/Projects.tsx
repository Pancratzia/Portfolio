import Aos from "aos";
import "aos/dist/aos.css";
import { ANIMATIONS, PROJECTS } from "../data/data";
import { random } from "../utils/functions";
import { useEffect } from "react";
import { Project } from "./Project";
import Extra from "./Extra";

const Projects = () => {

  useEffect(() => {
    Aos.init();
  }, []);


  return (
    <>
    <main className="projects" id="projects">
      <h2 className="projects__heading">My Projects</h2>
      <div className="projects__grid">
        {PROJECTS.map((project, index) => (
          <Project
            key={index}
            title={project.title}
            image={project.image}
            description={project.description}
            github={project.github}
            demo={project.demo}
            demoUser={project.demoUser}
            demoPass={project.demoPass}
            tags={project.tags}
            aos={random(ANIMATIONS)}
          />
        ))}
      </div>
    </main>

    <Extra />
    </>
  );
};

export default Projects;
