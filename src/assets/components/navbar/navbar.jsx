import './navbar.css'
import account_image from '../../images/account.png'
import NavBarOptions from './navbar_options';

function Navbar() {
    return (
        <>
            <nav className="nav">
                <div className="flex">
                    <div className="logo">
                        <img src={null} alt="logo" />
                        <span>RevTrack</span>
                    </div>
                    <div className="nav-options">
                        <NavBarOptions />
                    </div>
                    <div className="profile">
                        <img src={account_image} alt="" />
                        <div className="profile-info">
                            <h6>Default User</h6>
                            <span className="role">Admin 1</span>
                        </div>
                    </div>
                </div>            
            </nav>
        </>
    )
}

export default Navbar