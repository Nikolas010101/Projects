import Mail from '../img/Mail.svg'
import LinkedIn from '../img/linkedin.svg'
import GitHub from '../img/GitHub Icon.svg'

export default function Icons(){
    return (
        <div className = "icon-container">
            <a href = "mailto:nikgrande01@gmail.com" className = "mail"><img src = {Mail} alt='' width = "16px" className = "icon-img"/> Email</a>
            <a href = "https://github.com/Nikolas010101" className = "github"><img src = {GitHub} alt='' width = "18px" className = "icon-img"/> GitHub</a>
            <a href = "https://www.linkedin.com/in/nikolas-avelino-grande-0953b8196/" className = "linkedin"><img src = {LinkedIn} alt='' width = "16px" className = "icon-img"/> LinkedIn</a>
        </div>
    )
}