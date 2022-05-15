import React from 'react'

export default function Education(props) {
    const pt_header = 'Educação'
    const en_header = 'Education'
    const pt_univ1 = 'Bacharelado em Ciência e Tecnologia'
    const pt_univ2 = 'Engenharia de instrumentação, automação e robótica'
    const pt_hs = 'Técnico em eletrônica integrado ao ensino médio'
    const en_univ1 = 'Bachelor\'s degree in Science and Technology'
    const en_univ2 = 'Control and Automation Engineering'
    const en_hs = 'Electronics technician and High School'
    const pt_date = 'Fev/2016 - 2018'
    const en_date = 'Feb/2016 - 2018'
    return (
        <div className='education-container'>
            <h1 className="education">{props.language === 'pt' ? pt_header : en_header}</h1>
            <div className='educ-item'><span className='univ1'>{props.language === 'pt' ? pt_univ1 : en_univ1}</span><span className='period'>Jun/2019 - 2023</span></div>
            <br />
            <div className="educ-item"><span className="univ2">{props.language === 'pt' ? pt_univ2 : en_univ2}</span><span className='period'>Jun/2019 - 2024</span></div>
            <br />
            <div className="educ-item"><span className='hs'>{props.language === 'pt' ? pt_hs : en_hs}</span><span className='period'>{props.language === 'pt' ? pt_date : en_date}</span></div>
            <br />
        </div>
    )
}
