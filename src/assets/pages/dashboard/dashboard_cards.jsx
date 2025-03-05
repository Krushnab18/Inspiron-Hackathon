import Card from "./card"

//TODO : Add links to cards

function Cards() {

    const dashboard_cards = [
        { id : 1, text : "Total Sales", amount : "$824,246,00" , profit : true },
        { id : 2, text : "Total Profit", amount : "$10000000", profit : false },
        { id : 3, text : "Gross Profit Margin", amount : "$974598264" , profit : true },
        { id : 4, text : "Units Sold" , amount : "1000", profit : false }
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
                        // link={option.link}
                    />
                ))}
            </div>
        </>
    )
}

export default Cards