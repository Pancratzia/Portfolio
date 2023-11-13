
type Props = {
    href : string,
    text : string,
    icon : string
  }
  
  export const Social = ( props : Props ) => {
    return (
      <div className="social">
        <a href={props.href} rel="noreferrer" target="_blank">
          <i className={"social__icon " + props.icon}></i>
          <span className="hidden">{props.text}</span>
        </a>
      </div>
    )
  }