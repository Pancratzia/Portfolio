import Aos from "aos";
import "aos/dist/aos.css";
import { ANIMATIONS, EXTRA_PROJECTS } from "../data/data";
import { useEffect } from "react";
import { random } from "../utils/functions";

const Extra = () => {

  useEffect(() => {
    Aos.init();
  }, []);

  return (
    <section className="extra">
      <h2 className="extra__heading--extra">Extra Projects</h2>
      <div className="extra__grid">
        {EXTRA_PROJECTS.map((project, index) => (
          <a
            className="extra__project"
            href={project.link}
            key={index}
            target="_blank"
            data-aos={random(ANIMATIONS)}
          >
            <h3 className="extra__title">{project.title}</h3>

            <p className="extra__description">{project.description}</p>

            <div className="extra__footer">
              <div className="extra__tags">
                {project.tags &&
                  project.tags.map((tag, index) => (
                    <p key={index} className="extra__tag">
                      {tag}
                    </p>
                  ))}
              </div>
            </div>
          </a>
        ))}
      </div>
    </section>
  );
};

export default Extra;
