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
  const {
    title,
    image,
    description,
    github,
    demo,
    demoUser,
    demoPass,
    tags,
    aos,
  } = props;
  return (
    <article className="project" data-aos={aos}>
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
          <p className="project__demo-user">
            User: <span>{demoUser}</span>
          </p>
          <p className="project__demo-pass">
            Password: <span>{demoPass}</span>
          </p>
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
    </article>
  );
};
