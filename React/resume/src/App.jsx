import Info from "./components/Info";
import About from "./components/About";
import {useState} from 'react'
import ProfessionalExperience from "./components/ProfessionalExperience";
import TechnicalExperience from "./components/TechnicalExperience";
import Interests from "./components/Interests";
import Skills from "./components/Skills";
import Education from "./components/Education";
import Icons from "./components/Icons";
import './App.css'

function App() {
  const [language, setLanguage] = useState('pt')

  return (
    <div className="App">
      <Info language = {language} setLanguage = {setLanguage}/>
      <Icons/>
      <Education language = {language} />
      <hr />
      <About language = {language} />
      <hr />
      <ProfessionalExperience language = {language} />
      <hr />
      <TechnicalExperience language = {language} />
      <hr />
      <Interests language = {language} />
      <hr />
      <Skills language = {language} />
    </div>
  );
}

export default App;
