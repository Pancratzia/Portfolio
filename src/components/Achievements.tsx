import { useEffect } from "react";
import useFetch from "../hooks/useFetch";
import { Achievement } from "./Achievement";
import AOS from "aos";
import "aos/dist/aos.css";

const Achievements = () => {
  const {
    data: reposData,
    loading: loadingData,
    error: errorData,
  } = useFetch(
    "https://api.github.com/users/pancratzia/repos",
    import.meta.env.VITE_GITHUB_API_KEY
  );

  const {
    data: memberData,
    loading: loadingMember,
    error: errorMember,
  } = useFetch(
    "https://api.github.com/users/pancratzia",
    import.meta.env.VITE_GITHUB_API_KEY
  );

  const ANIMATIONS = [
    "fade-up", "flip-up", "flip-right", "flip-down", "flip-left", "zoom-in", "zoom-in-up", "zoom-in-down"
  ]

  const randomAnimation = () => {
    return ANIMATIONS[Math.floor(Math.random() * ANIMATIONS.length)];
  }

  useEffect(() => {
    AOS.init();
  }, [])

  return (
    <div className="achievements" id="achievements">
      <h2 className="achievements__heading">My Achievements</h2>
      <div className="achievements__grid">
        <Achievement
          title="GitHub Repositories"
          loading={loadingData}
          data={reposData}
          number={Array.isArray(reposData) ? reposData.length : 0}
          error={errorData}
          aos={randomAnimation()}
        />

        <Achievement
          title="GitHub Member Since"
          loading={loadingMember}
          data={memberData}
          number={null}
          error={errorMember}
          aos={randomAnimation()}
        />

        <Achievement
          title="Projects Created"
          loading={false}
          data={null}
          number="+20"
          error={null}
          aos={randomAnimation()}
        />

        <Achievement
          title="Successful Jobs"
          loading={false}
          data={null}
          number="+5"
          error={null}
          aos={randomAnimation()}
        />
      </div>
    </div>
  );
};

export default Achievements;
