import { FC } from "react";

interface AchievementProps {
    title: string;
    loading: boolean;
    data: { created_at?: string } | null;
    number: string | number | null;
    error: any;
    aos?: string;
  }
  
  export const Achievement: FC<AchievementProps> = ({ title, loading, data, number, error, aos }) => {
    
    return (
      <div className="achievement" data-aos={aos}>
        <h3 className="achievement__title">{title}</h3>
        <p className="achievement__number">
          {loading && "..."}
          {error && "0"}
          {data?.created_at
            ? data.created_at.slice(0, 4)
            : number}
        </p>
      </div>
    );
  };