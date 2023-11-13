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
          <div className="header__social">
            <a href="https://twitter.com/pancratzia" rel="noreferrer" target="_blank">
              <i className="header__icon fab fa-twitter-square"></i>
              <span className="hidden">Pancratzia's Twitter</span>
            </a>
          </div>

          <div className="header__social">
            <a href="https://github.com/pancratzia" rel="noreferrer" target="_blank">
              <i className="header__icon fab fa-github-square"></i>
              <span className="hidden">Pancratzia's GitHub</span>
            </a>
          </div>

          <div className="header__social">
            <a 
              rel="noreferrer"
              href="https://www.linkedin.com/in/leortegaperez/"
              target="_blank"
            >
              <i className="header__icon fab fa-linkedin"></i>
              <span className="hidden">Pancratzia's LinkedIn</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Header;
