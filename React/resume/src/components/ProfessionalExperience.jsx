import React from 'react'

export default function ProfessionalExperience(props) {
    const pt_header = "Experiência profissional"
    const pt_text = "Estágio em Data Science e automação industrial"
    const en_header = "Professional experience"
    const en_text = "Internship in Data Science and industrial automation"
    const pt_company = "Scania Latin America Fev/2022 - Atualmente"
    const en_company = "Scania Latin America Feb/2022 - Currently"
  return (
    <div className='professional-container'>
        <h1 className='professional'>
            {props.language === 'pt' ? pt_header : en_header}
        </h1>
        <h2 className='company'>{props.language === 'pt' ? pt_company : en_company}</h2>
        <p className='prof-text'>{props.language === 'pt' ? pt_text : en_text}</p>
    </div>
  )
}
