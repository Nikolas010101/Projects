import React from 'react'
import foto from '../img/foto.jpg'
import Togg from './Togg'

export default function Info(props) {
  const pt_course = 'UFABC: Estudante de engenharia de instrumentação, automação e robótica'
  const en_course = 'UFABC: Control and automation engineering student'
  return (
    <div className='info-container'>
      <div className="side">
        <h1 className='name'>Nikolas Avelino Grande</h1>
        <h2 className='location'>São Caetano do Sul - SP</h2>
        <h2 className='course'>{props.language === 'pt'? pt_course : en_course}</h2>
      </div>
      <div className='img'>
        <img src={foto} alt='' className='foto'/>
        <Togg language = {props.language} setLanguage = {props.setLanguage}/>
      </div>
    </div>
  )
}