import { FC } from "react";

interface AchievementProps {
    title: string;
    loading: boolean;
    data: { created_at?: string } | null;
    number: string | number | null;
    error: any;
  }
  
  export const Achievement: FC<AchievementProps> = ({ title, loading, data, number, error }) => {
    
    return (
      <div className="achievement">
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