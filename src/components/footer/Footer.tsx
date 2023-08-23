import "./Footer.scss";

type Props = {
  fixed?: boolean;
};

function Footer(props: Props) {
  return (
    <div className={`footer ${props.fixed ? "fixed" : ""}`}>
      <div className="container">
        <div className="links">
        <ul>
              <li>
                <a href="#header">Home</a>
              </li>
              <li>
                <a href="#about">About Me</a>
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
        </div>

        <div className="copy">
          <p>© {new Date().getFullYear()} - Laura Ortega</p>
        </div>

      </div>
    </div>
  );
}

export default Footer;
