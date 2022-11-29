import React from 'react'

export default function Skill({ level, text }) {
    const size = 24
    const svgArray = Array.from(Array(5)).map((_, i) => {
        const color = i < level ? "#356258" : "#78909c"
        return (
            <svg className={i < level ? "level-active" : ""} key={i} height={size} width={size} style={{ alignSelf: "center" }}>
                <circle key={i * 10} cx={size / 2} cy={size / 2} stroke="#607d8b" strokeWidth="4" r={size / 3} fill={color}></circle>
            </svg>
        )
    })
    const containerStyle = {
        display: "grid",
        gridTemplateRows: "auto auto",
        placeItems: "center"
    }
    const labelStyle = {
        fontSize: "1.5em",
        color: "white",
        margin: "0px 50px 0px 50px"
    }
    return (
        <div style={containerStyle}>
            <p style={labelStyle}>{text}</p>
            <div>
                {svgArray}
            </div>
        </div>
    )
}