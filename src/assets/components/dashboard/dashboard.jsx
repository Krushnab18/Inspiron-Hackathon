import './dashboard.css'
import Navbar from "../navbar/navbar"
import Cards from '../card/cards'
import DashboardCharts from '../dashboard-charts/dashboard-charts'

function Dashboard() {
    return (
        <>
            <div className="dashboard-page">
                <Navbar />
                <div className="dashboard-div">
                    <Cards />
                    <DashboardCharts />
                </div>
            </div>
        </>
    )
}

export default Dashboard