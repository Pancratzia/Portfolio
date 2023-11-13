import Navbar from "./Navbar";
import { Social } from "./Social";


const Header = () => {
  return (
    <div className="header">
      <div className="header__grid">
        <div className="header__info">
          <h1 className="header__logo">
            <a href="/" className="header__link">
              &#60; Laura Ortega &#47;&#62;
            </a>
          </h1>
          <h2 className="header__alias">Pancratzia</h2>
          <p className="header__subtitle">FullStack Developer</p>
        </div>
        <div className="header__socials">

          <Social href="https://twitter.com/pancratzia" text="Pancratzia's Twitter" icon="fab fa-twitter-square" />
          <Social href="https://github.com/pancratzia" text="Pancratzia's GitHub" icon="fab fa-github-square" />
          <Social href="https://www.linkedin.com/in/leortegaperez" text="Pancratzia's LinkedIn" icon="fab fa-linkedin" />
        </div>
      </div>

      <Navbar />
    </div>
  );
};

export default Header;
