import './navbar.css'
import { Link } from 'react-router-dom'

function Option( {text, image, link, selected, onClick } ) {
    return (
        <>
            <Link to={link} style={{textDecoration: "none"}}>
                <div className="option-div" style={{ backgroundColor: selected ? "#0F14F6" : "black"}} onClick={onClick}>
                    <div className="option-image-div">
                        <img src={image} alt="img" className='option-image' />
                    </div>
                    <div className="option-text">
                        <h5>{text}</h5>
                    </div>
                </div>  
            </Link>
        </>
    )
}

export default Option