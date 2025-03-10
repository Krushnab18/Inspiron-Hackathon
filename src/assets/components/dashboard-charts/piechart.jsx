import React from 'react';
import './dashboard-charts.css';
import { PieChart, Pie, Cell, Tooltip, Label, Legend, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Japan', sales: 20000 },
  { name: 'China', sales: 35000 },
  { name: 'Russia', sales: 25000 },
  { name: 'USA', sales: 15000 },
];

const COLORS = ['#132F53', '#627BC6', '#065EDF', '#3891D6'];

const PieChartComponent = () => {

  const totalSales = data.reduce((accumulator, currentValue) => {
    return accumulator + currentValue.sales;
  }, 0);

  return (
    <div className='pie-chart-div'>
      <div className="pie-chart-title">
        <span>Top Countries Sales</span>
      </div>
      <ResponsiveContainer width="100%" height="80%">
        <PieChart>
          <Pie
            data={data}
            dataKey="sales"
            nameKey="name"
            cx="50%"
            cy="45%"
            innerRadius={90}
            outerRadius={120}
            cornerRadius={15}
            paddingAngle={-10}
          >
            {data.map((entry, index) => {
              if(index === 0) {
                return <Cell key={`cell-${index}`} fill={COLORS[index]} pathLength={100} />;
              }
              return <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />;
            })}
            <Label
              value={`Total: $${totalSales}`}
              position="center"
              style={{ fontSize: '3vh', fontWeight: 'bold', fill: '#000' }}
            />
          </Pie>
          <Legend
            className='dashboard-pie-chart-legend'
            layout="vertical"
            align="right"
            verticalAlign="middle"
            iconSize={20}
            wrapperStyle={{ lineHeight: '10vh', margin: '2vh' }}
            formatter={(value) => <span style={{ fontFamily: 'Arial', fontSize: '14px', fontWeight: 'bold' }}>{value}</span>}
          />
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PieChartComponent;
