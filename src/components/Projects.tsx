interface Props {
  title: string;
  image: string;
  description: string;
  github: string;
  demo: string;
  demoUser: string;
  demoPass: string;
  tags?: string[];
}

export const Project = (props: Props) => {
  const { title, image, description, github, demo, demoUser, demoPass, tags } =
    props;
  return (
    <div className="project">
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

      <div className="project__info">
        <h3 className="project__title">{title}</h3>

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
            <i className="fa fa-eye"></i>
          </a>
        </div>

        <div className="project__info-demo">
          <p className="project__demo-user">User: <span>{demoUser}</span></p>
          <p className="project__demo-pass">Password: <span>{demoPass}</span></p>
        </div>
      </div>

      <div className="project__footer">
        <div className="project__tags">
          {tags &&
            tags.map((tag, index) => (
              <p key={index} className="project__tag">
                {tag}
              </p>
            ))}
        </div>
      </div>
    </div>
  );
};

const PROJECTS = [
  {
    title: "Bienes Raices",
    image: "project1",
    description:
      "Website for a real estate agency where a listing of properties for sale is displayed, along with details for each of them. It includes an Administration Panel to manage information related to properties, sellers, and blog posts",
    github: "https://github.com",
    demo: "https://github.com",
    demoUser: "Admin",
    demoPass: "Admin",
    tags: ["HTML", "CSS", "JavaScript", "PHP", "MySQL", "MVC", "Admin"],
  },
  {
    title: "Project 2",
    image: "project2",
    description: "Project 2 description",
    github: "https://github.com",
    demo: "https://github.com",
    demoUser: "Admin",
    demoPass: "Admin",
  },
  {
    title: "Project 3",
    image: "project3",
    description: "Project 3 description",
    github: "https://github.com",
    demo: "https://github.com",
    demoUser: "Admin",
    demoPass: "Admin",
  },
  {
    title: "Project 4",
    image: "project4",
    description: "Project 4 description",
    github: "https://github.com",
    demo: "https://github.com",
    demoUser: "Admin",
    demoPass: "Admin",
  },
];

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
            demoUser={project.demoUser}
            demoPass={project.demoPass}
            tags={project.tags}
          />
        ))}
      </div>
    </div>
  );
};

export default Projects;
