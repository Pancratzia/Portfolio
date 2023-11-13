
type Props = {
    href : string,
    text : string,
    icon : string
  }
  
  export const Social = ( props : Props ) => {
    return (
      <div className="header__social">
        <a href={props.href} rel="noreferrer" target="_blank">
          <i className={"header__icon " + props.icon}></i>
          <span className="hidden">{props.text}</span>
        </a>
      </div>
    )
  }