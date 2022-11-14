import React from 'react'

export default function Skill({ level, text, tagStyle }) {
    const size = 24
    let svgArray;
    switch (tagStyle) {
        case 'bar':
            svgArray = Array.from(Array(5)).map((_, i) => {
                const color = i < level ? "#92D050" : "#4E6773"
                const invColor = i < level ? "#4E6773" : "#92D050"
                return (
                    <svg key={i} height={size} width={size} style={{ alignSelf: "center" }}>
                        <rect key={i * 10} width={size} height={size} stroke={invColor} strokeWidth="3" fill={color}></rect>
                    </svg>
                )
            })
            break;
        default:
            svgArray = Array.from(Array(5)).map((_, i) => {
                const color = i < level ? "#92D050" : "#4E6773"
                const invColor = i < level ? "#4E6773" : "#92D050"
                return (
                    <svg key={i} height={size} width={size} style={{ alignSelf: "center" }}>
                        <circle key={i * 10} cx={size / 2} cy={size / 2} stroke={invColor} strokeWidth="2" r={size / 3} fill={color}></circle>
                    </svg>
                )
            })
            break;
    }
    const containerStyle = {
        display: "grid"
    }
    const svgContainerStyle = {
        gridRow: "1",
        gridColumn: "1",
        justifySelf: "start",
        alignSelf: "center",
        marginLeft: "10px"
    }
    const labelStyle = {
        fontSize: "1.75em",
        fontWeight: "bold",
        fontFamily: "Arial, Helvetica, sans-serif",
        color: "white",
        gridRow: "1",
        gridColumn: "2",
        marginRight: "10px"
    }
    return (
        <div style={containerStyle}>
            <div style={svgContainerStyle}>
                {svgArray}
            </div>
            <p style={labelStyle}>{text}</p>
        </div>
    )
}