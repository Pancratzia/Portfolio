interface Props {
  title: string;
  image: string;
  description: string;
  github: string;
  demo: string;
}

export const Project = (props: Props) => {
  const { title, image, description, github, demo } = props;
  return (
    <div className="project">
      <h3 className="project__title">{title}</h3>
      <picture>
        <source srcSet={`img/projects/${image}.avif`} type="image/avif" />
        <source srcSet={`img/projects/${image}.webp`} type="image/webp" />
        <source srcSet={`img/projects/${image}.png`} type="image/png" />

        <img
          className="project__image"
          src={`img/projects/${image}.png`}
          width="300"
          height="100%"
          alt={`Project: ${title}`}
          loading="lazy"
        />
      </picture>
      <p className="project__description">{description}</p>

      <div className="project__links">
        <a
          className="project__link"
          href={github}
          target="_blank"
          rel="noreferrer"
        >
          <i className="fab fa-github-square"></i>
        </a>
        <a
          className="project__link"
          href={demo}
          target="_blank"
          rel="noreferrer"
        >
          <i className="fa fa-external-link"></i>
        </a>
      </div>
    </div>
  );
};

const PROJECTS = [
  {
    title: "Project 1",
    image: "project1",
    description: "Project 1 description",
    github: "https://github.com",
    demo: "https://github.com", 
  },
  {
    title: "Project 2",
    image: "project2",
    description: "Project 2 description",
    github: "https://github.com",
    demo: "https://github.com",
  },
  {
    title: "Project 3",
    image: "project3",
    description: "Project 3 description",
    github: "https://github.com",
    demo: "https://github.com",
  },
  {
    title: "Project 4",
    image: "project4",
    description: "Project 4 description",
    github: "https://github.com",
    demo: "https://github.com",
  }
]

const Projects = () => {
  return (
    <div className="projects">
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
          />
        ))}
      </div>
    </div>
  );
};

export default Projects;
