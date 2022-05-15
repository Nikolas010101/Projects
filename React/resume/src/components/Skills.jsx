import React from 'react'

export default function Skills(props) {
    const pt_header = 'Habilidades'
    const en_header = 'Skills'
    const pt_skills = ['Inglês fluente', 'Mandarim básico', 'Python intermediário', 'C/C++ intermediário', 'Java básico', 'Microsoft Excel avançado', 'HTML/CSS e JavaScript intermediários', 'ReactJS básico', 'Ignition básico']
    const en_skills = ['Fluent English', 'Basic Chinese', 'Intermediate Python', 'Intermediate C/C++', 'Basic Java', 'Advanced Microsoft Excel', 'Intermediate HTML/CSS and JavaScript', 'Basic ReactJS', 'Basic Ignition']
    const pt_list = pt_skills.map((skill, i)=>{
        return <li className='skill-item' key = {i+10}>{skill}</li>
    })
    const en_list = en_skills.map((skill, i)=>{
        return <li className='skill-item' key = {i}>{skill}</li>
    })
    return (
        <div className='skills-container'>
            <h1 className='skills'>{props.language === 'pt' ? pt_header : en_header}</h1>
            <ul className='skills-list'>
                {props.language === 'pt' ? pt_list : en_list}
            </ul>
        </div>
    )
}
