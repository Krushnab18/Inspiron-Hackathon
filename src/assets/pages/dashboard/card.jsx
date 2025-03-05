import './card.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowUp, faArrowDown } from '@fortawesome/free-solid-svg-icons';

function Card({ text, amount, profit }) {
    return (
        <>
            <div className="card-container">
                <div className="card-header">
                    <h2 className="card-title">{text}</h2>
                </div>
                <div className="card-amount">
                    <p className="amount">{amount}</p>
                </div>
                <div className="card-footer">
                    <FontAwesomeIcon icon={profit ? faArrowUp : faArrowDown} style={{color: profit ? "#3B82F6" : "#FF574A" }} className="arrow-icon" />
                    <span className="percentage" style={{color: profit ? "#3B82F6" : "#FF574A"}}>12%</span>
                    <span className="footer-text">from the last month</span>
                </div>
            </div>
        </>
    )
}

export default Card