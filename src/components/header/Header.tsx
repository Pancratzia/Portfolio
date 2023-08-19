import "./Header.scss";

function Header() {

  const title= "< Laura Ortega />";
  return (
    <div className="header">
      <div className="container">
        <div className="top-header">
          <a href="/">
            <h1>
              {title} <span>Pancratzia </span>
            </h1>
          </a>
          <h2>FullStack Web Developer</h2>
        </div>

        <div className="middle-header">
          <ul className="socials">
            <li>
              <a href="https://twitter.com/pancratzia">Twitter</a>
            </li>
            <li>
              <a href="https://www.linkedin.com/in/leortegaperez/">Linkedin</a>
            </li>
            <li>
              <a href="https://github.com/pancratzia">Github</a>
            </li>
          </ul>
        </div>

        <div className="bottom-header">
          <nav className="nav">
            <ul>
              <li>
                <a href="/">Home</a>
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
