import { EXTRA_PROJECTS } from "../data/data";

const Extra = () => {
  return (
    <div className="extra">
      <h2 className="extra__heading--extra">Extra Projects</h2>
      <div className="extra__grid">
        {EXTRA_PROJECTS.map((project, index) => (
          <a className="extra__project" href={project.link} key={index} target="_blank">
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
    </div>
  );
};

export default Extra;
