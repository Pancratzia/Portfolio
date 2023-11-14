import Aos from "aos";
import { useEffect } from "react";
import { random } from "../utils/functions";
import { ANIMATIONS } from "../data/consts";

const About = () => {

  useEffect(() => {
    Aos.init();
  }, []);

  return (
    <div className="about" id="about">
      <h2 className="about__heading">About Me</h2>
      <div className="about__grid">
        <div className="about__image-container">
          <img
            className="about__image"
            src="img/personal/profile.png"
            alt="About"
            loading="lazy"
          />
        </div>

        <div className="about__info" data-aos={random(ANIMATIONS)}>
          <p className="about__description">As a <span className="about__keyword">FullStack Developer</span>, I am driven by an unwavering passion for <span className="about__keyword">programming</span>, a love for <span className="about__keyword">problem-solving</span>, and an insatiable curiosity for exploration. I thrive on the continuous pursuit of knowledge, embodying a commitment to lifelong learning. Having pursued my studies in <span className="about__keyword">Telematics Engineering</span> at the Universidad Centro Occidental Lisandro Alvarado in Barquisimeto, Venezuela, I've come to understand that being a programmer is a <span className="about__keyword">journey of perpetual learning and unlearning</span>.</p>
          <p className="about__description">
          My dedication extends beyond the academic realm, as I believe in delivering <span className="about__keyword">excellence</span> in every professional endeavor. With an inherent belief that being a developer is synonymous with <span className="about__keyword">constant evolution</span>, I am motivated by the desire to grow personally and professionally each day. My approach to work is anchored in the philosophy that <span className="about__keyword">continuous improvement is not just a goal, but a way of life</span>.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;
