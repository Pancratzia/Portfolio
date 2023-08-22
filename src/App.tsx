import { useEffect, useState } from "react";
import "./assets/styles/App.scss";
import Footer from "./components/footer/Footer";
import Header from "./components/header/Header";
import About from "./components/about/About";

function App() {
  const [isHeaderVisible, setIsHeaderVisible] = useState(true);

  useEffect(() => {
    const handleScroll = () => {
      const header = document.getElementById("header");
      if (header) {
        const rect = header.getBoundingClientRect();
        setIsHeaderVisible(rect.bottom > 0);
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <>
      <Header />
      <About />
      <Footer fixed={!isHeaderVisible} />
    </>
  );
}

export default App;
