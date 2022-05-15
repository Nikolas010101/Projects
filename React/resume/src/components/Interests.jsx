import React from 'react'

export default function Interests(props) {
    const pt_header = 'Interesses'
    const pt_interests = ['Automação industrial', 'Programação', 'Ciência de dados', 'Inteligência artificial', 'Indústria 4.0']
    const en_header = 'Interests'
    const en_interests = ['Industrial automation', 'Programming', 'Data science', 'Artificial inteligence', 'Industry 4.0']
    const pt_list = pt_interests.map((interest, i)=>{
      return <li className='interest-item' key = {i}>{interest}</li>
    })
    const en_list = en_interests.map((interest, i)=>{
      return <li className='interest-item' key = {i}>{interest}</li>
    })
  return (
    <div className='interests-container'>
      <h1 className='interests'>{props.language === 'pt' ? pt_header : en_header}</h1>
      <ul>
        {props.language === 'pt' ? pt_list : en_list}
      </ul>
    </div>
  )
}
