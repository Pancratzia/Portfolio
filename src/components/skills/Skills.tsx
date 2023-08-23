import { useEffect, useRef } from "react";
import { FaHtml5, FaCss3Alt, FaJs, FaBootstrap, FaJava } from "react-icons/fa";
import { SiArduino, SiCplusplus, SiGithub, SiGit, SiMysql, SiMongodb, SiNodedotjs, SiReact, SiSass, SiPostman, SiSpringboot } from "react-icons/si";
import { renderToString } from "react-dom/server";
import "./Skills.scss";

function Skills() {
  const iconsContainerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const iconsContainer = iconsContainerRef.current;
    if (!iconsContainer) return;
  

    iconsContainer.innerHTML = '';
  
    const createBouncingIcon = (icon: JSX.Element, dx: number, dy: number, color: string) => {
      const bouncingIcon = document.createElement("div");
      bouncingIcon.className = "bouncing-icon";
      

      const iconHtml = renderToString(icon);
      bouncingIcon.innerHTML = iconHtml;
      bouncingIcon.style.color = color;
      iconsContainer.appendChild(bouncingIcon);
  
      let x = Math.random() * (iconsContainer.offsetWidth - 40); 
      let y = Math.random() * (iconsContainer.offsetHeight - 40); 

      let dxValue = Math.random() * 2 + 1; 
      let dyValue = Math.random() * 2 + 1;
      if (Math.random() > 0.5) dxValue = -dxValue; 
      if (Math.random() > 0.5) dyValue = -dyValue; 
      const moveIcon = () => {
        if (x < 0 || x > iconsContainer.offsetWidth - 40) {
          dxValue = -dxValue;
        }
        if (y < 0 || y > iconsContainer.offsetHeight - 40) {
          dyValue = -dyValue;
        }
  
        x += dxValue;
        y += dyValue;
  
        bouncingIcon.style.left = x + "px";
        bouncingIcon.style.top = y + "px";
  
        requestAnimationFrame(moveIcon);
      };
  
      moveIcon();
    };
  
    createBouncingIcon(<FaHtml5 />, 4, 3, "#E34F26");
    createBouncingIcon(<FaCss3Alt />, 1, 5, "#264DE4");
    createBouncingIcon(<FaJs />, 2, 2, "#F7DF1E");
    createBouncingIcon(<FaBootstrap />, 3, 4, "#7952B3");
    createBouncingIcon(<FaJava />, 5, 1, "#007396");
    createBouncingIcon(<SiArduino />, 1, 3, "#00979D");
    createBouncingIcon(<SiCplusplus />, 3, 2, "#00599C");
    createBouncingIcon(<SiGithub />, 2, 4, "#181717");
    createBouncingIcon(<SiGit />, 4, 1, "#F05032");
    createBouncingIcon(<SiMysql />, 2, 3, "#4479A1");
    createBouncingIcon(<SiMongodb />, 1, 4, "#47A248");
    createBouncingIcon(<SiNodedotjs />, 3, 1, "#339933");
    createBouncingIcon(<SiReact />, 4, 2, "#61DAFB");
    createBouncingIcon(<SiSass />, 1, 2, "#CC6699");
    createBouncingIcon(<SiPostman />, 3, 5, "#FF6C37");
    createBouncingIcon(<SiSpringboot />, 2, 1, "#6DB33F");
  
  }, []);
  
  

  return (
    <div className="skills" id="skills">
      <h2 className="h2-title">My Skills</h2>
      <div className="container">
        <div className="icons-container" ref={iconsContainerRef}></div>
      </div>
    </div>
  );
}

export default Skills;
