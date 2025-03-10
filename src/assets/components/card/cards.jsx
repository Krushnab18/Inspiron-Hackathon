import Card from "./card";
import { FaMoneyBillWave } from "react-icons/fa";
import { FaChartLine } from "react-icons/fa";
import { BsBarChartFill } from "react-icons/bs";
import { FaBox } from "react-icons/fa";
import  './card.css'

function Cards() {

    const dashboard_cards = [
        { id: 1, text: "Total Sales", amount: "$824,246,00", profit: true, icon: FaMoneyBillWave },
        { id: 2, text: "Total Profit", amount: "$10,000,000", profit: false, icon: FaChartLine },
        { id: 3, text: "Gross Profit Margin", amount: "$974,598,264", profit: true, icon: BsBarChartFill },
        { id: 4, text: "Units Sold", amount: "1000", profit: false, icon: FaBox }
    ];

    return (
        <>
            <div className="dashboard-cards">
                {dashboard_cards.map(option => (
                    <Card
                        key={option.id}
                        text={option.text}
                        amount={option.amount}
                        profit={option.profit}
                        icon={option.icon}
                    />
                ))}
            </div>
        </>
    )
}

export default Cards