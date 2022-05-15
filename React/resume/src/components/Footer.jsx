import React from 'react'

export default function Footer(props) {
    const pt_footer = 'Feito por Nikolas'
    const en_footer = 'Designed by Nikolas'
    return (
        <div className='footer-container'>
            <footer className='footer'>
                <p>{props.language === 'pt' ? pt_footer : en_footer}</p>
            </footer>
        </div>
    )
}
