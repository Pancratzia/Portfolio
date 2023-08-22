import { useEffect, useState, useRef } from "react";
import "./assets/styles/App.scss";
import Footer from "./components/footer/Footer";
import Header from "./components/header/Header";
import About from "./components/about/About";

function App() {
  const [isHeaderVisible, setIsHeaderVisible] = useState(true);
  const contentRef = useRef<HTMLDivElement | null>(null); // Agrega el tipo de referencia

  useEffect(() => {
    const handleScroll = () => {
      const header = document.getElementById("header");
      if (header) {
        const rect = header.getBoundingClientRect();
        setIsHeaderVisible(rect.bottom > 0);
      }

      // Obtener la altura real del footer
      const footer = document.querySelector(".footer") as HTMLElement; // Asegura el tipo
      if (footer) {
        let footerHeight = footer.offsetHeight;
        footerHeight +=20;
        if (contentRef.current) {
          contentRef.current.style.marginBottom = !isHeaderVisible ? `${footerHeight}px` : "0";
        }
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, [isHeaderVisible]);

  return (
    <>
      <div className="content" ref={contentRef}>
        <Header />
        <About />
      </div>

      <Footer fixed={!isHeaderVisible} />
    </>
  );
}

export default App;
