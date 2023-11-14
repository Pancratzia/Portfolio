const Footer = () => {
  return (
    <footer className="footer">
      <p className="footer__alias">Pancratzia</p>
      <p className="footer__text">
        © {new Date().getFullYear()} Laura Ortega. All rights reserved.
      </p>
    </footer>
  );
};

export default Footer;
