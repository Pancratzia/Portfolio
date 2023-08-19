import "./Header.scss";
import { FaSquareTwitter, FaSquareGithub, FaLinkedin } from "react-icons/fa6";

function Header() {
  const title = "< Laura Ortega />";
  return (
    <div className="header" id="header">
      <div className="container">
        <div className="top-header">
          <h1>
            <a href="/">{title}</a> <span>Pancratzia </span>
          </h1>

          <h2>FullStack Developer</h2>
        </div>

        <div className="middle-header">
          <ul className="socials">
            <li>
              <a href="https://twitter.com/pancratzia">
                <FaSquareTwitter />
              </a>
            </li>
            <li>
              <a href="https://www.linkedin.com/in/leortegaperez/">
                <FaLinkedin />
              </a>
            </li>
            <li>
              <a href="https://github.com/pancratzia">
                <FaSquareGithub />
              </a>
            </li>
          </ul>
        </div>

        <div className="bottom-header">
          <nav className="nav">
            <ul>
              <li>
                <a href="#header">Home</a>
              </li>
              <li>
                <a href="#about">About</a>
              </li>
              <li>
                <a href="#skills">Skills</a>
              </li>
              <li>
                <a href="#projects">Projects</a>
              </li>
              <li>
                <a href="#contact">Contact</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  );
}

export default Header;
