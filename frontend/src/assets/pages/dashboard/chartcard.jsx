import "./chartcard.css";

const ChartCard = ({ title, chartType }) => {
	return (
		<div className="chart-card-container">
			<div className="chart-card-header">
				<h2 className="chart-card-title">{title}</h2>
			</div>
			<div className="chart-content">
				<img
					src={`https://placehold.co/300x200?text=${chartType}+Chart`}
					alt={`${chartType} chart placeholder`}
					className="chart-image"
				/>
			</div>
		</div>
	);
};

export default ChartCard;
