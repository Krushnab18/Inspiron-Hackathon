import "./header.css";
import account_image from "../images/account.png";

function Header({ title }) {
	return (
		<>
			<div className="header-div">
				<div className="header-title">
					<h2>{title}</h2>
				</div>
				<div className="account-div">
					<div className="account-image-div">
						<img src={account_image} alt="" className="account-image" />
					</div>
					<img src="" alt="" className="account-img" />
					<div className="account-div-right">
						<div className="account-name">
							<h5>Account</h5>
						</div>
					</div>
				</div>
			</div>
		</>
	);
}

export default Header;
