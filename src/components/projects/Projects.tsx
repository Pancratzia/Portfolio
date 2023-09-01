import Card from '../card/Card';
import './Projects.scss';

function Projects() {
  const projectData = [
    {
      title: 'Project 1',
      imageUrl: 'https://via.placeholder.com/300',
      description: 'Description of Project 1',
      date: '00/00/0000',
      github: 'https://github.com',
      live: 'https://live.com',
    },
    {
      title: 'Project 2',
      imageUrl: 'https://via.placeholder.com/300',
      description: 'Description of Project 2',
      date: '00/00/0000',
      github: 'https://github.com',
    },
  ];

  return (
    <div id="projects" className="projects">
      <h2 className="h2-title">Projects</h2>

      <div className="container">
        <div className="projects-container">
          {projectData.map((project, index) => (
            <Card
              key={index}
              title={project.title}
              imageUrl={project.imageUrl}
              description={project.description}
              date={project.date}
              github={project.github}
              live={project.live}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Projects;

