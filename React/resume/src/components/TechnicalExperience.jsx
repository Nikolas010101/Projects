import React from 'react'

export default function TechnicalExperience(props) {
    const pt_header = "Experiência técnica"
    const en_header = "Technical experience"
    const pt_text = "Membro e coordenador do departamento de eletrônica embarcada, desenvolvi e melhorei circuitos eletrônicos, programei microcontroladores (Arduino) e coordenei um time com outros estudantes da área."
    const en_text = "Member and coordinator of the embedded electronics department, I developed and improved electronic circuits, programmed microcontrollers (Arduino) and managed a team with other students from the department."
    return (
        <div className='technical-container'>
            <h1 className="technical">{props.language === 'pt' ? pt_header : en_header}</h1>
            <h2 className='sub-technical'>Challenger UFABC (Ballard Student H2 Challenge) Jan/2021 - Mar/2022</h2>
            <p className="technical-text">{props.language === 'pt' ? pt_text : en_text}</p>
        </div>
    )
}