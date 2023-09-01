import "./About.scss";
import ProfileIMG from "../../assets/img/profile.jpg";

function About() {
  const currentAge = () => {
    const year = 1999;
    const month = 8;
    const day = 18;

    const today = new Date();

    if (month <= today.getMonth()) {
      if (day <= today.getDate()) {
        return today.getFullYear() - year;
      }
    }
    return today.getFullYear() - year - 1;
  };

  const factData = [
    {
      id: 1,
      title: "Who am I?",
      text: "My name is Laura Ortega, better known as Pancratzia",
    },
    {
      id: 2,
      title: "What am I?",
      text: "I'm a FullStack Developer",
    },
    {
      id: 3,
      title: "Where do I live?",
      text: "I'm currently living in Barquisimeto, Venezuela",
    },
    {
      id: 4,
      title: "How old am I?",
      text: "I'm " + currentAge() + " years old",
    },
  ];

  return (
    <div className="about" id="about">
      <h2 className="h2-title">About Me</h2>
      <div className="container">
        <div className="img-container">
          <img src={ProfileIMG} alt="Profile Image" className="img" />
        </div>

        <div className="text-container">
          {factData.map((fact) => (
            <div key={fact.id} className="fact">
              <h3>{fact.title}</h3>
              <p>{fact.text}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default About;
