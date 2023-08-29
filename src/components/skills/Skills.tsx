import { useEffect, useRef } from "react";
import { FaHtml5, FaCss3Alt, FaJs, FaBootstrap, FaJava } from "react-icons/fa";
import {
  SiArduino,
  SiCplusplus,
  SiGithub,
  SiGit,
  SiMysql,
  SiMongodb,
  SiNodedotjs,
  SiReact,
  SiSass,
  SiPostman,
  SiSpringboot,
} from "react-icons/si";
import { renderToString } from "react-dom/server";
import "./Skills.scss";

function Skills() {
  const iconsContainerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const iconsContainer = iconsContainerRef.current;
    if (!iconsContainer) return;

    iconsContainer.innerHTML = "";

    const createBouncingIcon = (icon: JSX.Element, color: string) => {
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
        const maxX = iconsContainer.offsetWidth - bouncingIcon.offsetWidth;
        const maxY = iconsContainer.offsetHeight - bouncingIcon.offsetHeight;
      
        if (x < 0 || x > maxX) {
          dxValue = -dxValue;
          x = Math.max(0, Math.min(maxX, x)); // Mantener x dentro de los límites
        }
      
        if (y < 0 || y > maxY) {
          dyValue = -dyValue;
          y = Math.max(0, Math.min(maxY, y)); // Mantener y dentro de los límites
        }
      
        x += dxValue;
        y += dyValue;
      
        bouncingIcon.style.left = x + "px";
        bouncingIcon.style.top = y + "px";
      
        requestAnimationFrame(moveIcon);
      };
      

      moveIcon();
    };

    createBouncingIcon(<FaHtml5 />, "#E34F26");
    createBouncingIcon(<FaCss3Alt />, "#264DE4");
    createBouncingIcon(<FaJs />, "#F7DF1E");
    createBouncingIcon(<FaBootstrap />, "#7952B3");
    createBouncingIcon(<FaJava />, "#007396");
    createBouncingIcon(<SiArduino />, "#00979D");
    createBouncingIcon(<SiCplusplus />, "#00599C");
    createBouncingIcon(<SiGithub />, "#181717");
    createBouncingIcon(<SiGit />, "#F05032");
    createBouncingIcon(<SiMysql />, "#4479A1");
    createBouncingIcon(<SiMongodb />, "#47A248");
    createBouncingIcon(<SiNodedotjs />, "#339933");
    createBouncingIcon(<SiReact />, "#61DAFB");
    createBouncingIcon(<SiSass />, "#CC6699");
    createBouncingIcon(<SiPostman />, "#FF6C37");
    createBouncingIcon(<SiSpringboot />, "#6DB33F");
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
