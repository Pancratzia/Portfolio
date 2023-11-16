import Aos from "aos";
import "aos/dist/aos.css";
import { ANIMATIONS } from "../data/consts";
import { random } from "../utils/functions";
import { useEffect } from "react";

interface Props {
  title: string;
  image: string;
  description: string;
  github: string;
  demo: string;
  demoUser: string;
  demoPass: string;
  tags?: string[];
  aos?: string;
}

export const Project = (props: Props) => {
  const { title, image, description, github, demo, demoUser, demoPass, tags, aos } =
    props;
  return (
    <div className="project" data-aos={aos}>
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
    github: "https://github.com/Pancratzia/Web-Development-Repository/tree/main/06-BienesRaicesMVC",
    demo: "https://pancratzia-bienesraices.000webhostapp.com/",
    demoUser: "test@admin.com",
    demoPass: "admin",
    tags: ["HTML", "CSS", "JavaScript", "PHP", "MySQL", "MVC", "Admin"],
  },
  {
    title: "App Salon",
    image: "project2",
    description: "Website for a beauty salon where a list of services is displayed for clients along with the option to schedule an appointment. It includes an administration section to manage customer information, appointments, and services.",
    github: "https://github.com/Pancratzia/Web-Development-Repository/tree/main/07-AppSalon",
    demo: "https://desqate.domcloud.io/",
    demoUser: "admin@appsalon.com - client@appsalon.com",
    demoPass: "123456789",
    tags: ["HTML", "CSS", "JavaScript", "PHP", "MySQL", "MVC", "PHPMailer", "Admin", "DOMCloud"],
  },
  {
    title: "UpTask",
    image: "project3",
    description: "A simple task application where each user can register and create projects, consisting of tasks that can be deleted, modified, and marked as completed.",
    github: "https://github.com/Pancratzia/Web-Development-Repository/tree/main/08-UpTask",
    demo: "https://dobloye.domcloud.io/",
    demoUser: "test@user.com",
    demoPass: "123456",
    tags: ["HTML", "CSS", "JavaScript", "PHP", "MySQL", "MVC", "PHPMailer", "DOMCloud"],
  },
  {
    title: "PankraCamp",
    image: "project4",
    description: "Project for a two-day event featuring conferences and workshops. It includes an administrative area to manage event information and a user registration system for attendees. Attendees can purchase three types of tickets and make payments through PayPal (The project is a demo, so it is using a PayPal sandbox account).",
    github: "https://github.com/Pancratzia/Web-Development-Repository/tree/main/09-PankraCamp",
    demo: "https://fahbelo.domcloud.io/",
    demoUser: "test@admin.com - test@user.com",
    demoPass: "123456",
    tags: ["HTML", "CSS", "JavaScript", "PHP", "MySQL", "MVC", "PHPMailer", "Admin", "DOMCloud", "PayPal"],
  },
];

const Projects = () => {

  useEffect(() => {
    Aos.init();
  }, []);


  return (
    <div className="projects" id="projects">
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
    </div>
  );
};

export default Projects;
