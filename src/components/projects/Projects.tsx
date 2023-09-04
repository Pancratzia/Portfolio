import Card from '../card/Card';
import './Projects.scss';

function Projects() {
  const projectData = [
    {
      title: 'PancraLocation',
      imageUrl: 'pancralocation.jpg',
      description: 'React Project using a node.js server and MongoDB with an optional SQLite alternative version to geolocate the user in realtime and verify if they\'re inside one of the five polygons around the globe.',
      date: '05/08/2023',
      github: 'https://github.com/Pancratzia/PancraLocation',
      live: 'https://pancralocation.onrender.com/',
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
              imageUrl={`/projects/${project.imageUrl}`}
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

