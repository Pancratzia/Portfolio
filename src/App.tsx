import { useEffect, useState, useRef } from "react";
import "./assets/styles/App.scss";
import Footer from "./components/footer/Footer";
import Header from "./components/header/Header";
import About from "./components/about/About";
import Skills from "./components/skills/Skills";
import Projects from "./components/projects/Projects";
import Contact from "./components/contact/Contact";

function App() {
  const [isHeaderVisible, setIsHeaderVisible] = useState(true);
  const [footerHeight, setFooterHeight] = useState(0);
  const contentRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const handleScroll = () => {
      const header = document.getElementById("header");
      if (header) {
        const rect = header.getBoundingClientRect();
        setIsHeaderVisible(rect.bottom > 0);
      }

      const footer = document.querySelector(".footer") as HTMLElement;
      if (footer) {
        const calculatedFooterHeight = footer.offsetHeight + 20;
        setFooterHeight(calculatedFooterHeight);
      }
    };

    window.addEventListener("scroll", handleScroll);
    handleScroll(); // Llama a handleScroll en la carga inicial para establecer la altura correcta
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <>
      <div className="main-content" ref={contentRef} style={{ paddingBottom: `${footerHeight}px` }}>
        <Header />
        <About />
        <Skills />
        <Projects />
        <Contact />
      </div>

      <Footer fixed={!isHeaderVisible} />
    </>
  );
}

export default App;
