import { useState, useEffect, SetStateAction, useRef } from "react";
import emailjs from "@emailjs/browser";

import "./Contact.scss";
import Swal from "sweetalert2";
function Contact() {
  const [username, setUsername] = useState("");
  const [avatarUrl, setAvatarUrl] = useState("https://via.placeholder.com/50");
  const form = useRef<HTMLFormElement | null>(null);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");

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
      emailjs.sendForm(serviceID, templateID, form.current, publicKEY).then(
        (result) => {
          Swal.fire({
            icon: "success",
            title: "Your email has been sent!",
            text: "I will contact you as soon as possible!",
            showConfirmButton: false,
            timer: 3000,
          });
          console.log(result.text);

          resetForm();
        },
        (error) => {

          console.error(error.text);

          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Something went wrong!",
            showConfirmButton: false,
            timer: 1500,
          });
        }
      );
    } else {
      console.error("El formulario no se ha inicializado correctamente.");
    }
  };

  const resetForm = () => {
    setName("");
    setEmail("");
    setUsername("");
    setSubject("");
    setMessage("");
  }

  return (
    <div className="contact" id="contact">
      <div className="container">
        <h2 className="h2-title">Contact Me</h2>
        <div className="contact-container">
          <form
            ref={form}
            onSubmit={handleSubmit}
            className="form"
            method="POST"
          >
            <legend>Want to get in touch? Feel free to write a message!</legend>

            <div className="form-field">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                name="name"
                id="name"
                placeholder="Your name..."
                value={name}
                onChange={(e) => setName(e.target.value)}
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
                value={email}
                onChange={(e) => setEmail(e.target.value)}
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
                    value={username}
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
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                required
              />
            </div>

            <div className="form-field">
              <label htmlFor="message">Message</label>
              <textarea
                name="message"
                id="message"
                placeholder="Your message..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                required
              ></textarea>
            </div>

            <div className="buttons">
              <input type="submit" value="Send" />
              <input type="button" value="Reset" onClick={resetForm} />
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Contact;
