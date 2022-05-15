import React from 'react'

function Togg(props) {

    function handleClick(event){
        props.setLanguage((prev)=> prev === 'pt' ? 'en' : 'pt')
    }

    return (
        <div className='togg-container'>
            <p className='p-toggle'><label className='label-toggle' htmlFor="toggle">{props.language === 'en' ? 'Português' : 'English'}</label></p>
            <label className="switch">
                <input type="checkbox" name='toggle' id='toggle' onClick={handleClick}/>
                <span className="slider round"></span>
            </label>
        </div>
    )
}

export default Togg