import React from 'react'

export default function About(props) {
    const pt_header = 'Sobre'
    const pt_text = 'Sou estudante de engenharia na Universidade Federal do ABC, tenho grande interesse em tecnologia, gosto de automação e de simplificar tarefas. Gosto de ajudar pessoas e compartilhar o que eu sei. Procuro sempre aprender mais e me aprofundar em novos tópicos.'

    const en_header = 'About'
    const en_text = 'I am an engineering student at Universidade Federal do ABC, I have great interest in technology, I like automation and simplifying tasks. I like helping people and sharing what I already know. I\'m always looking forward to learning more and delve myself deeper into new topics.'

    return (
      <div className='about-container'>
          <h1 className='about'>{props.language === 'pt' ? pt_header : en_header}</h1>
          <p className='about-text'>
              {props.language === 'pt' ? pt_text : en_text}
          </p>
      </div>
    )
}
