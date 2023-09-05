import Card from '../card/Card';
import './Projects.scss';

function Projects() {
  const projectData = [
    {
      title: 'PancraLocation',
      imageUrl: 'pancralocation.png',
      description: 'React Project using a node.js server and MongoDB with an optional SQLite alternative version to geolocate the user in realtime and verify if they\'re inside one of the five polygons around the globe.',
      date: '05/08/2023',
      github: 'https://github.com/Pancratzia/PancraLocation',
      live: 'https://pancralocation.onrender.com/',
    },
    {
      title: 'Pokedex',
      imageUrl: 'pokedex.png',
      description: 'Frontend project using HTML, CSS and JS with Pokedex API. Pokemons are showed randomly and they card background changes depending on the type of the pokemon showing.',
      date: '14/03/2023',
      github: 'https://github.com/Pancratzia/50Proyectos50Dias/tree/main/37-Pokedex',
      live: 'https://pokedex-pancratzia.netlify.app/',
    },
    {
      title: 'PanCrAFÉ',
      imageUrl: 'pancrafe.png',
      description: 'Frontend project creating a café blog using HTML, CSS and JS. It\'s responsive and was created using BEM methodology for better organization while styling.',
      date: '10/10/2022',
      live: 'https://pancrafe.netlify.app/',
    },
    {
      title: 'Bienes Raices',
      imageUrl: 'bienesraices.png',
      description: 'Frontend project creating a real estate website using HTML, CSS and JS for Juan Pablo de la Torre Valdez Web Development course on Udemy and deployed on netlify.',
      date: '27/10/2022',
      live: 'https://pancratzia-bienesraices-responsive.netlify.app/',
    }
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

