import Card from "./card";
import { IoCartOutline } from "react-icons/io5";
import  './card.css'

function Cards() {

    const dashboard_cards = [
        { id: 1, text: "Total Sales", amount: "$824,246,00", profit: true, icon: IoCartOutline },
        { id: 2, text: "Total Profit", amount: "$10,000,000", profit: false, icon: IoCartOutline },
        { id: 3, text: "Gross Profit Margin", amount: "$974,598,264", profit: true, icon: IoCartOutline },
        { id: 4, text: "Units Sold", amount: "1000", profit: false, icon: IoCartOutline }
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