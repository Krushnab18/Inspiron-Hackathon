import './card.css'
import React from 'react';
import { FaArrowTrendUp } from "react-icons/fa6";
import { FaArrowTrendDown } from 'react-icons/fa6';

function Card({ text, amount, profit, icon }) {
    return (
        <>
            <div className="card">
                <div className="div2"></div>
                <div className="card-top-div">
                    <div className="card-top-icon-div">
                        {React.createElement(icon, {className:'card-top-icon'})}
                    </div>
                    <div className="card-top-title-div">
                        <span>{text}</span>
                    </div>
                </div>
                <div className='card-bottom-div'>
                    <div className='card-bottom-title-div'>
                        <span>{amount}</span>
                    </div>
                    <div className="card-bottom-icon-div" style={{color: profit ? "#48bb78" : "#EC2301"}} >
                        {profit ? <FaArrowTrendUp /> : <FaArrowTrendDown /> }
                        <span>40%</span>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Card