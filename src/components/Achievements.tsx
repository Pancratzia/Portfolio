
import useFetch from "../hooks/useFetch";
import { Achievement } from "./Achievement";



const Achievements = () => {
  const { data: reposData, loading: loadingData } = useFetch(
    "https://api.github.com/users/pancratzia/repos",
    import.meta.env.VITE_GITHUB_API_KEY
  );

  const { data: memberData, loading: loadingMember } = useFetch(
    "https://api.github.com/users/pancratzia",
    import.meta.env.VITE_GITHUB_API_KEY
  );

  return (
    <div className="achievements">
      <h2 className="about__heading">My Achievements</h2>
      <div className="achievements__grid">
        <Achievement
          title="GitHub Repositories"
          loading={loadingData}
          data={reposData}
          number={Array.isArray(reposData) ? reposData.length : 0}
        />

        <Achievement
          title="Member Of GitHub Since"
          loading={loadingMember}
          data={memberData}
          number={null}
        />

        <Achievement
          title="Projects Created"
          loading={false}
          data={null}
          number="+20"
        />
      </div>
    </div>
  );
};

export default Achievements;
