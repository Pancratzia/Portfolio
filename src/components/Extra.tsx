
import "aos/dist/aos.css";
import { Swiper, SwiperSlide } from "swiper/react";
import { EXTRA_PROJECTS } from "../data/data";
import { Navigation } from 'swiper/modules';
import 'swiper/css';
import "swiper/css/navigation";

const Extra = () => {

  return (
    <section className="extra">
      <h2 className="extra__heading--extra">Extra Projects</h2>
      
        <Swiper
          navigation={true}
          modules={[Navigation]}
          className="extra__grid"
          spaceBetween={25}
          slidesPerView={1}
          breakpoints={{
            768: {
              slidesPerView: 2,
            },
            1024: {
              slidesPerView: 3,
            },
          }}
          loop={true}
          centeredSlides={true}
          
        >
          {EXTRA_PROJECTS.map((project, index) => (
            <SwiperSlide key={index} className="extra__project">
             <h3 className="extra__title">{project.title}</h3>
             <a className="extra__link" href={project.link} target="_blank">
                <i className="extra__icon fa fa-eye"></i>
              </a>

                <p className="extra__description">{project.description}</p>

                <div className="extra__footer">
                  <div className="extra__tags">
                    {project.tags &&
                      project.tags.map((tag, index) => (
                        <p key={index} className="extra__tag">
                          {tag}
                        </p>
                      ))}
                  </div>
                </div>
              
            </SwiperSlide>
          ))}
        </Swiper>
      
    </section>
  );
};

export default Extra;
