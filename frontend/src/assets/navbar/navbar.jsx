import './navbar.css'
import NavbarOptions from './navbar_options'
import logout_image from '../images/logout.png'
import { Link } from 'react-router-dom'

function Navbar() {
    return (
        <>
            <div className="navbar-div">
                <div className="company-div">
                    <img src='' alt='' />
                    <h3>Company Name</h3>
                </div>
                <div className="options">
                    <NavbarOptions />
                </div>
                <Link to="/logout">
                    <div className="logout">
                        <img src={logout_image} alt="logout" className="logout-image" />
                        <h5>Logout</h5>
                    </div>
                </Link>
            </div>
        </>
    )
}

export default Navbar