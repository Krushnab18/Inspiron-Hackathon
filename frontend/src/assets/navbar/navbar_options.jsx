import { useLocation } from "react-router-dom";
import Option from "./option";
import dashboard_image from "../images/dashboard.png";
import analytics_image from "../images/analytics.png";
import transaction_image from "../images/transaction.png";
import settings_image from "../images/settings.png";
import aichat_image from "../images/aichat.png";

function NavbarOptions() {
	const location = useLocation();

	const navbar_options = [
		{ id: 1, text: "Dashboard", image: dashboard_image, link: "/dashboard/" },
		{ id: 2, text: "Analytics", image: analytics_image, link: "/analytics/" },
		{
			id: 3,
			text: "Transactions",
			image: transaction_image,
			link: "/transactions/",
		},
		{ id: 4, text: "Settings", image: settings_image, link: "/settings/" },
		{ id: 5, text: "Ai Chat", image: aichat_image, link: "/aichat/" },
	];

	return (
		<div className="options">
			{navbar_options.map((option) => (
				<Option
					key={option.id}
					text={option.text}
					image={option.image}
					link={option.link}
					selected={location.pathname === option.link}
					onClick={() => setSelected(option.id)}
				/>
			))}
		</div>
	);
}

export default NavbarOptions;
