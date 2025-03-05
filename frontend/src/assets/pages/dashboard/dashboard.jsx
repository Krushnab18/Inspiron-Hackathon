import "./dashboard.css";
import Header from "../../header/header.jsx";
import Cards from "./dashboard_cards";
import Navbar from "../../navbar/navbar";
import ChartCard from "./chartcard";

function Dashboard() {
	return (
		<>
			<Navbar />
			<div className="dashboard-div">
				<div className="dashboard-content">
					<Header title="Dashboard" />
					<Cards />
					<div className="grid-container">
						<ChartCard title="Pie Chart" chartType="pie" />
						<ChartCard title="Bar Chart" chartType="bar" />
					</div>
				</div>
			</div>
		</>
	);
}

export default Dashboard;
