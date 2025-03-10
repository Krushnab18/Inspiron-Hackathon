import './navbar.css'
import { Link } from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

function Option({ icon, text, selected, onClick, link }) {
    return (
        <>
            <Link to={link} style={{textDecoration: "none"}}>
                <div className={`navbar-option-div ${selected ? 'selected' : ''}`} onClick={onClick}>
                    <div className="navbar-option-icon" style={{color: selected ? "#2563eb" : "gray"}}>
                        <FontAwesomeIcon icon={icon} className='icon'/>
                    </div>
                    <div className={`navbar-option-text ${selected ? 'selected' : ''}`}>
                        <span>{selected ? text : ""}</span>
                    </div>
                </div>
            </Link>
        </>
    )
}

export default Option