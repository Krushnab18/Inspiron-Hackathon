import './navbar.css'
import Option from './option';
import { faChartSimple } from '@fortawesome/free-solid-svg-icons';
import { faDesktop } from '@fortawesome/free-solid-svg-icons';
import { faCommentDots } from '@fortawesome/free-solid-svg-icons';
import { useLocation } from "react-router-dom";
import { useState } from 'react';

function NavBarOptions() {

    const location = useLocation();
    const [selected, setSelected] = useState(null);

    const navbar_options = [
        {id : 1, icon : faChartSimple, text : "Dashboard", link : "/dashboard/"},
        {id : 2, icon : faDesktop, text : "Analytics", link : "/analytics/"},
        {id : 3, icon : faCommentDots, text : "AI Chat", link : "/aichat/"},
    ];

    return (
        <>
            {navbar_options.map((option) => (
                <Option
                    key={option.id}
                    icon={option.icon}
                    text={option.text}
                    link={option.link}
                    selected={location.pathname === option.link}
                    onClick={() => setSelected(option.id)}
                />
            ))}
        </>
    )
}

export default NavBarOptions