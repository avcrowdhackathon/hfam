import React from "react";

export function ItemList(items, handleClick) {
    
    return (
        <div>
            <ul>
                {items.map(({name, count}) => (
                    <li>
                        {name} - {count}
                    </li>
                ))}
            </ul>
        </div>
    )
}