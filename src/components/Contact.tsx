import { useRef } from "react";
import emailjs from "@emailjs/browser";
import Swal from "sweetalert2";

const Contact = () => {
  const form = useRef<HTMLFormElement | null>(null);

  const sendEmail = (e: any) => {
    e.preventDefault();

    emailjs
      .sendForm(
        import.meta.env.VITE_EMAILJS_SERVICE_ID,
        import.meta.env.VITE_EMAILJS_TEMPLATE_ID,
        e.target,
        import.meta.env.VITE_EMAILJS_PUBLIC_KEY
      )
      .then(
        (result: any) => {
          if (result.text === "OK") {
            Swal.fire({
              title: "Email sent!",
              text: "Thank you for reaching out. I'll get back to you as soon as possible.",
              icon: "success",
            });
          }

          form.current?.reset();
        },
        (error: any) => {
          console.log(error.text);
          Swal.fire({
            title: "Error!",
            text: "Something went wrong. Please try again later.",
            icon: "error",
          });
        }
      );
  };

  return (
    <section className="contact" id="contact">
      <h2 className="contact__heading">Contact Me</h2>
      <form className="contact__form" ref={form} onSubmit={sendEmail}>
        <legend className="contact__legend">
          Want to get in touch? Fill out the form below and I will get back to
          you as soon as possible.
        </legend>

        <fieldset className="contact__fieldset">
          <legend className="contact__legend--fieldset">Contact Info</legend>

          <div className="contact__field">
            <label className="contact__label" htmlFor="name">
              Name
            </label>
            <input
              className="contact__input"
              type="text"
              id="name"
              name="name"
              placeholder="Enter your full name"
              required
            />
          </div>

          <div className="contact__field">
            <label className="contact__label" htmlFor="email">
              Email
            </label>
            <input
              className="contact__input"
              type="email"
              id="email"
              name="email"
              placeholder="Enter your email"
              required
            />
          </div>

          <div className="contact__field--textarea">
            <label className="contact__label" htmlFor="message">
              Message
            </label>
            <textarea
              className="contact__textarea"
              id="message"
              name="message"
              placeholder="Enter your message"
              required
            ></textarea>
          </div>
        </fieldset>

        <div className="contact__actions">
          <input
            type="reset"
            value="Reset"
            className="contact__submit--reset"
          />
          <input className="contact__submit" type="submit" value="Submit" />
        </div>
      </form>
    </section>
  );
};

export default Contact;
