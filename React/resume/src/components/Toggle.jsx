import React from 'react'

export default function Toggle(props) {
    const toggle_pt = 'Português'
    const toggle_en = 'English'

    function handleChange(){
        props.setLanguage((prevLang)=>{
            if(prevLang === 'pt') return 'en'
            else return 'pt'
        })
    }

    return (
    <div className="toggle-container">
        <div className='toggle'>
            <span className='toggle-text'>{props.language === 'pt' ? toggle_en : toggle_pt}</span>
            <label className="toggle" htmlFor="toggle">
                <input className="toggle__input" type="checkbox" id="toggle" onChange={handleChange}/>
                <div className="toggle__fill"></div>
            </label>
        </div>
    </div>
    )
}
