import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Dashboard from "./assets/pages/dashboard/dashboard";
import Analytics from "./assets/pages/analytics/analytics";
import Transactions from "./assets/pages/transactions/transactions";
import Settings from "./assets/pages/settings/settings";
import Logout from "./assets/pages/logout/logout";
import Chat from "./assets/pages/aichat/chat";

function App() {
	return (
		<>
			<div className="page-div">
				<Router>
					<Routes>
						<Route path="/dashboard/" element={<Dashboard />} />
						<Route path="/analytics/" element={<Analytics />} />
						<Route path="/transactions/" element={<Transactions />} />
						<Route path="/settings/" element={<Settings />} />
						<Route path="/logout/" element={<Logout />} />
						<Route path="/aichat/" element={<Chat />} />
					</Routes>
				</Router>
			</div>
		</>
	);
}

export default App;
