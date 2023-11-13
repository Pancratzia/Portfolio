const Navbar = () => {
  const handleClick = () => {
    const openNavbar = document.getElementById("openNavbar");
    const closeNavbar = document.getElementById("closeNavbar");
    const navbarLinks = document.querySelectorAll(".navbar__link");

    openNavbar?.classList.toggle("navbar__icon--hidden");
    openNavbar?.classList.toggle("navbar__icon--visible");
    closeNavbar?.classList.toggle("navbar__icon--visible");
    closeNavbar?.classList.toggle("navbar__icon--hidden");

    navbarLinks.forEach((link) => {
      link.classList.toggle("navbar__link--visible");
      link.classList.toggle("navbar__link--hidden");
    })

  };

  return (
    <nav className="navbar">
      <div className="navbar__action" onClick={handleClick}>
        <i
          id="openNavbar"
          className="navbar__icon fas fa-bars navbar__icon--visible"
        ></i>
        <i
          id="closeNavbar"
          className="navbar__icon fas fa-times navbar__icon--hidden"
        ></i>
      </div>
      <a href="#" className="navbar__link navbar__link--hidden">
        Home
      </a>
      <a href="#" className="navbar__link navbar__link--hidden">
        About Me
      </a>
      <a href="#" className="navbar__link navbar__link--hidden">
        Skills
      </a>
      <a href="#" className="navbar__link navbar__link--hidden">
        Projects
      </a>
      <a href="#" className="navbar__link navbar__link--hidden">
        Contact
      </a>
    </nav>
  );
};

export default Navbar;
