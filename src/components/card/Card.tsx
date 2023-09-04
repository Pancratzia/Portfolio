import { SiGithub } from "react-icons/si";
import { FaRegEye } from "react-icons/fa";
import "./Card.scss";

interface CardProps {
  title: string;
  imageUrl: string;
  description: string;
  date: string;
  github?: string;
  live?: string;
}

function Card(props: CardProps) {
  const { title, imageUrl, description, date, github, live } = props;

  return (
    <div className="card">
      <div className="card-header">
        <h3>{title}</h3>
        <div className="img">
          <img src={imageUrl} alt={title} />
        </div>
      </div>

      <div className="card-body">
        <p>{description}</p>
        <span>{date}</span>
      </div>

      <div className="card-footer">
        {github && (
          <div className="icon">
            <a href={github} target="_blank">
              <SiGithub />
            </a>
          </div>
        )}

        {live && (
          <div className="icon">
            <a href={live} target="_blank">
              <FaRegEye />
            </a>
          </div>
        )}
      </div>
    </div>
  );
}

export default Card;
