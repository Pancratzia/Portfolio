import { useState, useEffect, SetStateAction, useRef } from "react";
import emailjs from "@emailjs/browser";

import "./Contact.scss";
function Contact() {
  const [username, setUsername] = useState("");
  const [avatarUrl, setAvatarUrl] = useState("https://via.placeholder.com/50");
  const form = useRef<HTMLFormElement | null>(null);

  useEffect(() => {
    if (username.length >= 1) {
      fetch(`https://api.github.com/users/${username}`)
        .then((response) => {
          if (response.status === 200) {
            return response.json();
          } else {
            throw new Error("Usuario no encontrado");
          }
        })
        .then((data) => {
          setAvatarUrl(data.avatar_url);
        })
        .catch((error) => {
          console.error(error);
          setAvatarUrl("https://via.placeholder.com/50");
        });
    } else {
      setAvatarUrl("https://via.placeholder.com/50");
    }
  }, [username]);

  const handleUsernameChange = (event: {
    target: { value: SetStateAction<string> };
  }) => {
    setUsername(event.target.value);
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    
    event.preventDefault();

    const serviceID = import.meta.env.VITE_SERVICE_ID;
    const templateID = import.meta.env.VITE_TEMPLATE_ID;
    const publicKEY = import.meta.env.VITE_PUBLIC_KEY;

    if (form.current) {
      emailjs
        .sendForm(
          serviceID,
          templateID,
          form.current,
          publicKEY
        )
        .then(
          (result) => {
            console.log(result.text);
            form.current?.reset();
          },
          (error) => {
            console.log(error.text);
          }
        );
    } else {
      console.error("El formulario no se ha inicializado correctamente.");
    }
  };

  return (
    <div className="contact">
      <div className="container">
        <h2 className="h2-title">Contact Me</h2>
        <div className="contact-container">
          <form ref={form} onSubmit={handleSubmit} className="form" method="POST">
            <legend>Want to get in touch? Feel free to write a message!</legend>

            <div className="form-field">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                name="name"
                id="name"
                placeholder="Your name..."
                required
              />
            </div>

            <div className="form-field">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                name="email"
                id="email"
                placeholder="Your email..."
                required
              />
            </div>

            <div className="form-field">
              <label htmlFor="github-username">
                GitHub Username <small>(Optional)</small>
              </label>
              <div className="user-info">
                <img src={avatarUrl} alt="github profile picture" />
                <div className="input">
                  <input
                    type="text"
                    name="github-username"
                    id="github-username"
                    placeholder="Your github username..."
                    onChange={handleUsernameChange}
                  />
                </div>
              </div>
            </div>

            <div className="form-field">
              <label htmlFor="subject">Subject</label>
              <input
                type="text"
                name="subject"
                id="subject"
                placeholder="Your subject..."
                required
              />
            </div>

            <div className="form-field">
              <label htmlFor="message">Message</label>
              <textarea
                name="message"
                id="message"
                placeholder="Your message..."
                required
              ></textarea>
            </div>

            <div className="buttons">
              <input type="submit" value="Send" />
              <input type="reset" value="Reset" />
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Contact;
