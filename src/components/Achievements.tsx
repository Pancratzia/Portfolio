import useFetch from "../hooks/useFetch";
import { Achievement } from "./Achievement";

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
        />

        <Achievement
          title="GitHub Member Since"
          loading={loadingMember}
          data={memberData}
          number={null}
          error={errorMember}
        />

        <Achievement
          title="Projects Created"
          loading={false}
          data={null}
          number="+20"
          error={null}
        />

        <Achievement
          title="Successful Jobs"
          loading={false}
          data={null}
          number="+5"
          error={null}
        />
      </div>
    </div>
  );
};

export default Achievements;
