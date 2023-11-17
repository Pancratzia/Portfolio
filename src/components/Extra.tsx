import { EXTRA_PROJECTS } from "../data/data";

const Extra = () => {
  return (
    <div className="extra">
      <h2 className="extra__heading">Extra Projects</h2>
      <div className="extra__grid">
        {EXTRA_PROJECTS.map((project, index) => (
          <div className="extra__project" key={index}>
            <div className="extra__header">
              <h3 className="extra__title">{project.title}</h3>
              <a
                className="extra__link"
                href={project.link}
                target="_blank"
                rel="noreferrer"
              >
                <i className="fa fa-eye"></i>
              </a>
            </div>
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
          </div>
        ))}
      </div>
    </div>
  );
};

export default Extra;
