const Navbar = () => {
  const navbarLinks = [
    { text: "About Me", href: "#" },
    { text: "Achievements", href: "#" },
    { text: "Skills", href: "#" },
    { text: "Projects", href: "#" },
    { text: "Contact", href: "#" },
  ];

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
    });
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
      {navbarLinks.map((link, index) => (
        <a
          key={index}
          href={link.href}
          className={`navbar__link navbar__link--hidden`}
        >
          {link.text}
        </a>
      ))}
    </nav>
  );
};

export default Navbar;
