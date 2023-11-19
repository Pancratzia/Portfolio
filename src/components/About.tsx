const About = () => {
  return (
    <section className="about" id="about">
      <h2 className="about__heading">About Me</h2>
      <div className="about__grid">
        <div className="about__image-container">
          <picture>
            <source srcSet="img/personal/profile.avif" type="image/avif" />
            <source srcSet="img/personal/profile.webp" type="image/webp" />
            <source srcSet="img/personal/profile.png" type="image/png" />

            <img
              className="about__image"
              src="img/personal/profile.png"
              width="300"
              height="100%"
              alt="About"
              loading="lazy"
            />
          </picture>
        </div>

        <div className="about__info">
          <p className="about__description">
            As a <span className="about__keyword">FullStack Developer</span>, I
            am driven by an unwavering passion for{" "}
            <span className="about__keyword">programming</span>, a love for{" "}
            <span className="about__keyword">problem-solving</span>, and an
            insatiable curiosity for exploration. I thrive on the continuous
            pursuit of knowledge, embodying a commitment to lifelong learning.
            Having pursued my studies in{" "}
            <span className="about__keyword">Telematics Engineering</span> at
            the Universidad Centro Occidental Lisandro Alvarado in Barquisimeto,
            Venezuela, I've come to understand that being a programmer is a{" "}
            <span className="about__keyword">
              journey of perpetual learning and unlearning
            </span>
            .
          </p>
          <p className="about__description">
            My dedication extends beyond the academic realm, as I believe in
            delivering <span className="about__keyword">excellence</span> in
            every professional endeavor. With an inherent belief that being a
            developer is synonymous with{" "}
            <span className="about__keyword">constant evolution</span>, I am
            motivated by the desire to grow personally and professionally each
            day. My approach to work is anchored in the philosophy that{" "}
            <span className="about__keyword">
              continuous improvement is not just a goal, but a way of life
            </span>
            .
          </p>
        </div>
      </div>

      <footer className="about__footer">
        <p className="about__footer-text">
          Do you want to know more about me? <a href="https://drive.google.com/file/d/1-IR2j718rKg6Q-EWdLbgRS-H16-sDP-O/view?usp=sharing" target="_blank" className="about__footer-link">Read my CV!</a>
        </p>
      </footer>

    </section>
  );
};

export default About;
