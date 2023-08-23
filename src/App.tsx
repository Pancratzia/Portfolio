import { useEffect, useState, useRef } from "react";
import "./assets/styles/App.scss";
import Footer from "./components/footer/Footer";
import Header from "./components/header/Header";
import About from "./components/about/About";
import Skills from "./components/skills/Skills";
import Projects from "./components/projects/Projects";

function App() {
  const [isHeaderVisible, setIsHeaderVisible] = useState(true);
  const contentRef = useRef<HTMLDivElement | null>(null); 

  useEffect(() => {
    const handleScroll = () => {
      const header = document.getElementById("header");
      if (header) {
        const rect = header.getBoundingClientRect();
        setIsHeaderVisible(rect.bottom > 0);
      }

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
  

  const contentHeight = contentRef.current?.offsetHeight || 0;
  const windowHeight = window.innerHeight;

  return (
    <>
      <div className="main-content" ref={contentRef}>
        <Header />
        <About />
        <Skills />
        <Projects />
      </div>

      <Footer fixed={!isHeaderVisible || contentHeight <= windowHeight} />
    </>
  );
}

export default App;
