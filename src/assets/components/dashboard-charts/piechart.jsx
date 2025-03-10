import React from 'react';
import './dashboard-charts.css'
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Company A', sales: 15000 },
  { name: 'Company B', sales: 20000 },
  { name: 'Company C', sales: 35000 },
  { name: 'Company D', sales: 25000 },
  { name: 'Company E', sales: 30000 },
];

const COLORS = ['#FF8042', '#0088FE', '#00C49F', '#FFBB28', '#FF6F61'];

const PieChartComponent = () => {
  return (
    <div className='pie-chart-div'>
      <div className="pie-chart-title">
        <span>Top Countries Sales</span>
      </div>
      <ResponsiveContainer width="80%" height="80%">
        <PieChart>
          <Pie
            data={data}
            dataKey="sales"
            nameKey="name"
            cx="50%"
            cy="50%"
            outerRadius={100}
            fill="#8884d8"
            label
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
          {/* <Legend /> */}
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PieChartComponent;