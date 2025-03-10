import './dashboard-charts.css'
import LineChart from './linechart'
import PieChartComponent from './piechart'

function DashboardCharts() {
    return (
        <>
            <div className="dashboard-charts-div">
                <LineChart />
                <PieChartComponent />
            </div>
        </>
    )
}

export default DashboardCharts