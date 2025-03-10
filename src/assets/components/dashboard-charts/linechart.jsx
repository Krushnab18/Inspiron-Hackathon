import React, { useState } from 'react';
import './dashboard-charts.css';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { format } from 'date-fns';

const updatedData = [
  { date: new Date(2023, 1, 16), sales: 10916.45, cogs: 6347.05, profit: 4569.4 },
  { date: new Date(2023, 1, 17), sales: 18755.82, cogs: 9676.59, profit: 9079.23 },
  { date: new Date(2023, 1, 18), sales: 44168.27, cogs: 24800.16, profit: 19368.11 },
  { date: new Date(2023, 1, 19), sales: 64675.81, cogs: 37357.32, profit: 27318.49 },
  { date: new Date(2023, 1, 20), sales: 24399.37, cogs: 9176.16, profit: 15223.21 },
  { date: new Date(2023, 1, 21), sales: 64693.01, cogs: 30219.4, profit: 34473.61 },
  { date: new Date(2023, 1, 22), sales: 18495.57, cogs: 9095.43, profit: 9400.14 },
  { date: new Date(2023, 1, 23), sales: 3855.37, cogs: 1992.87, profit: 1862.5 },
  { date: new Date(2023, 1, 24), sales: 26281.22, cogs: 12651.04, profit: 13630.18 },
  { date: new Date(2023, 1, 25), sales: 49627.19, cogs: 24938.55, profit: 24688.64 },
  { date: new Date(2023, 1, 26), sales: 19750.7, cogs: 12762.75, profit: 6987.95 },
  { date: new Date(2023, 1, 27), sales: 6184.48, cogs: 4824.44, profit: 1360.04 },
  { date: new Date(2023, 1, 28), sales: 21517.95, cogs: 11376.42, profit: 10141.53 },
  { date: new Date(2023, 2, 1), sales: 18574.16, cogs: 7408.86, profit: 11165.3 },
  { date: new Date(2023, 2, 2), sales: 18714.42, cogs: 13008.24, profit: 5706.18 },
  { date: new Date(2023, 2, 3), sales: 14980.52, cogs: 6372.6, profit: 8607.92 },
  { date: new Date(2023, 2, 4), sales: 65119.44, cogs: 29426.32, profit: 35693.12 },
  { date: new Date(2023, 2, 5), sales: 48081.64, cogs: 19109.2, profit: 28972.44 },
  { date: new Date(2023, 2, 6), sales: 26554.51, cogs: 13682.5, profit: 12872.01 },
  { date: new Date(2023, 2, 7), sales: 5620.87, cogs: 2936.85, profit: 2684.02 },
  { date: new Date(2023, 2, 8), sales: 27055.14, cogs: 14953.7, profit: 12101.44 },
  { date: new Date(2023, 2, 9), sales: 18730.06, cogs: 8668.53, profit: 10061.53 },
  { date: new Date(2023, 2, 10), sales: 10749.38, cogs: 7044.75, profit: 3704.63 },
  { date: new Date(2023, 2, 11), sales: 46099.2, cogs: 22930.88, profit: 23168.32 },
  { date: new Date(2023, 2, 12), sales: 54256.73, cogs: 29267.1, profit: 24989.63 },
  { date: new Date(2023, 2, 13), sales: 27643.73, cogs: 17919.36, profit: 9724.37 },
  { date: new Date(2023, 2, 14), sales: 17507.44, cogs: 7764.75, profit: 9742.69 },
  { date: new Date(2023, 2, 15), sales: 15972.12, cogs: 10582.09, profit: 5390.03 },
  { date: new Date(2023, 2, 16), sales: 10393.46, cogs: 6815.9, profit: 3577.56 }
];


function LineChart() {
    
    const [line_chart_type, setLineChartType] = useState('sales');

    return (
        <>
            <div className='line-chart-div'>
                <div className="line-chart-top-div">
                    <div className="line-chart-title-div">
                        <span>{line_chart_type.charAt(0).toUpperCase() + line_chart_type.slice(1)}</span>
                    </div>
                    <div className="line-chart-buttons-div">
                        <button className={line_chart_type === 'sales' ? 'active' : ''} onClick={() => setLineChartType('sales')}>Sales</button>
                        <button className={line_chart_type === 'cogs' ? 'active' : ''} onClick={() => setLineChartType('cogs')}>COGS</button>
                        <button className={line_chart_type === 'profit' ? 'active' : ''} onClick={() => setLineChartType('profit')}>Profit</button>
                    </div>
                </div>
                <ResponsiveContainer key={line_chart_type} width="90%" height="80%" className="line-chart-container">
                    <AreaChart data={updatedData}>
                        <CartesianGrid vertical={false} strokeDasharray="3 3"/>
                        <XAxis
                            dataKey="date"
                            scale="time"
                            tickFormatter={(tick) => format(tick, 'dd MMM')}
                            tick={{ fontSize: 12, fontFamily: 'Arial', fontWeight: 'bold', fill: 'gray' }}
                        />
                        
                        <YAxis
                            tick={{ fontSize: 12, fontFamily: 'Arial', fontWeight: 'bold', fill: 'gray' }}
                        />
                        
                        <Tooltip
                            labelFormatter={(value) => format(value, 'dd/MM/yy')}
                            labelStyle={{fontSize: "0.8rem", fontFamily: 'Poppins'}}
                            itemStyle={{ fontSize: "0.8rem", fontFamily: 'Poppins', fontWeight: 'bold', color: 'gray' }}
                        />
                        
                        <defs>
                            <linearGradient id="blue-gradient" x1="0" x2="0" y1="0" y2="1">
                                <stop offset="0%" stopColor="#e0f2fe"/>
                                <stop offset="100%" stopColor="#F0FFFF"/>
                            </linearGradient>
                        </defs>

                        <Area
                            type="monotone"
                            dataKey={line_chart_type}
                            stroke="#3498db"
                            fill="url(#blue-gradient)"
                            activeDot={{ r: 1 }}
                            isAnimationActive={true}
                            animationDuration={1000}
                            animationEasing="ease-in-out"
                        />
                    </AreaChart>
                </ResponsiveContainer>
            </div>
        </>
    );
};

export default LineChart;