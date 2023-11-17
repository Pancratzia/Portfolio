import { useEffect, useRef } from "react";

function Skills() {
  const iconsContainerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const iconsContainer = iconsContainerRef.current;
    if (!iconsContainer) return;

    iconsContainer.innerHTML = "";

    const createBouncingIcon = (iconClass: string, color: string) => {
      const bouncingIcon = document.createElement("div");
      bouncingIcon.className = "skills__icon";

      bouncingIcon.innerHTML = `<i class="${iconClass}" style="color: ${color};"></i>`;
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
          x = Math.max(0, Math.min(maxX, x));
        }

        if (y < 0 || y > maxY) {
          dyValue = -dyValue;
          y = Math.max(0, Math.min(maxY, y));
        }

        x += dxValue;
        y += dyValue;

        bouncingIcon.style.left = x + "px";
        bouncingIcon.style.top = y + "px";

        requestAnimationFrame(moveIcon);
      };

      moveIcon();
    };

    createBouncingIcon("devicons devicons-html5", "#E34F26");
    createBouncingIcon("devicons devicons-css3", "#264DE4");
    createBouncingIcon("devicons devicons-javascript", "#F7DF1E");
    createBouncingIcon("devicons devicons-bootstrap", "#7952B3");
    createBouncingIcon("devicons devicons-sass", "#CC6699");
    createBouncingIcon("fa-brands fa-react", "#61DAFB");
    createBouncingIcon("devicons devicons-nodejs", "#339933");
    createBouncingIcon("devicons devicons-github_badge", "#181717");
    createBouncingIcon("devicons devicons-git", "#F05032");
    createBouncingIcon("devicons devicons-php", "#777BB4");
    createBouncingIcon("devicons devicons-mysql", "#00758F");
    createBouncingIcon("devicons devicons-postgresql", "#336791");
  }, []);

  return (
    <section className="skills" id="skills">
      <h2 className="skills__heading">My Skills</h2>
      <div className="skills__grid">
        <div className="skills__icons" ref={iconsContainerRef}></div>
      </div>
    </section>
  );
}

export default Skills;
