const Projects = () => {
  return (
    <div className="projects">
      <h2 className="projects__heading">My Projects</h2>
      <div className="projects__grid">
        <div className="project">
          <h3 className="project__title">My Portfolio</h3>
          <picture>

            <source srcSet="img/projects/portfolio.avif" type="image/avif" />
            <source srcSet="img/projects/portfolio.webp" type="image/webp" />
            <source srcSet="img/projects/portfolio.png" type="image/png" />

            <img 
              className="project__image"
              src="img/projects/portfolio.png"
              width="300"
              height="100%"
              alt="Portfolio"
              loading="lazy"
            />
          </picture>
          <p className="project__description">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi consequatur accusantium soluta perspiciatis veniam laboriosam ab maiores ad illo praesentium magni possimus molestias eos corrupti vitae vero dignissimos, molestiae, minus neque inventore. Consectetur asperiores magni at accusantium nihil libero optio. Quod debitis vero quidem exercitationem a sint assumenda ipsa ipsum.
          </p>

          <div className="project__links">
            <a
              className="project__link"
              href="https://github.com/pancratzia/portfolio"
              target="_blank"
              rel="noreferrer"
            >
              <i className="fab fa-github-square"></i>
            </a>
            <a
              className="project__link"
              href="#"
              target="_blank"
              rel="noreferrer"
            >
              <i className="fa fa-external-link"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Projects;
