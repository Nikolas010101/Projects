import "../src/styles.css";
import foto from "../src/img/foto.jpg";
import linkedin from "../src/img/linkedin.svg";
import github from "../src/img/github.svg";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMapMarkerAlt } from "@fortawesome/free-solid-svg-icons";
import { faPhone } from "@fortawesome/free-solid-svg-icons";
import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
import challenger from "../src/img/challenger.jpg";
import scania from "../src/img/scania.jpg";
import etec from "../src/img/etec.jpg";
import ufabc from "../src/img/ufabc.png";
import Skill from "./components/Skill";

function App() {
    return (
        <div className="App">
            <div className="grid-container">
                <div className="header">
                    <img className="foto" src={foto} alt="" />
                    <div className="about-container">
                        <h1 className="about">About Me</h1>
                        <section>
                            <article className="about-text">
                                Electronics technician, control and automation engineering student at UFABC and an intern at Scania Latin
                                America. I have great interest in technology, data science, machine learning, programming, automation and
                                electronics in general. I am currently a data science and industrial automation intern at Scania in the
                                plant of São Bernardo, in which I extract, analyze, process and present data from the production process,
                                creating tools for data driven decision making.
                            </article>
                        </section>
                    </div>
                    <div className="links">
                        <h1>Links</h1>
                        <section className="link-img-container">
                            <a rel="noreferrer" target="_blank" href="https://www.linkedin.com/in/nikolas-avelino-grande-0953b8196/">
                                <img className="link-img" src={linkedin} alt="" />
                            </a>
                            <a rel="noreferrer" target="_blank" href="https://github.com/Nikolas010101">
                                <img className="link-img" src={github} alt="" />
                            </a>
                        </section>
                    </div>
                </div>
                <div className="content">
                    <section className="basic-info">
                        <div className="name-div">
                            <h1 className="name">Nikolas Avelino Grande</h1>
                            <h2 className="description">Engineering student, data science intern and tech savvy</h2>
                        </div>
                        <div className="infos">
                            <article className="info">
                                <FontAwesomeIcon icon={faMapMarkerAlt} color="#ffff" fontSize="24px" />
                                <p className="info-text">São Paulo, São Caetano do Sul</p>
                            </article>
                            <article className="info">
                                <FontAwesomeIcon icon={faPhone} color="#ffff" fontSize="24px" />
                                <a href="tel:11957896290" className="info-text">
                                    <p>11-95789-6290</p>
                                </a>
                            </article>
                            <article className="info">
                                <FontAwesomeIcon icon={faEnvelope} color="#ffff" fontSize="24px" />
                                <a href="mailto:nik.grande@hotmail.com" className="info-text">
                                    <p>nik.grande@hotmail.com</p>
                                </a>
                            </article>
                        </div>
                    </section>
                    <section className="skills">
                        <h2 className="sub-header">Experience</h2>
                        <div className="skill-container">
                            <article className="skill">
                                <img className="skill-img" src={challenger} alt="" />
                                <div className="inner-skill">
                                    <h3 className="skill-title">Head of Embedded Electronics</h3>
                                    <p className="skill-text">Developed circuits for control and measurement of the vehicle. Coordination and distribution of
                                        tasks to members of the department.</p>
                                </div>
                            </article>
                            <article className="skill">
                                <img className="skill-img" src={scania} alt="" />
                                <div className="inner-skill">
                                    <h3 className="skill-title">Industrial Automation and Data Science Intern</h3>
                                    <p className="skill-text">I extract, analyze, process and present data from the production process, creating tools for
                                        data driven decision making, I also support other areas with the information they need.</p>
                                </div>
                            </article>
                        </div>
                    </section>
                    <div className="skills-education">
                        <section className="skills">
                            <h2 className="sub-header">Education</h2>
                            <div className="skill-container">
                                <article className="skill">
                                    <img className="skill-img" src={etec} alt="" />
                                    <div className="inner-skill">
                                        <h3 className="skill-title">Electronics Technician</h3>
                                        <p className="skill-text">February 2016 - December 2018</p>
                                    </div>
                                </article>
                                <article className="skill">
                                    <img className="skill-img" src={ufabc} alt="" />
                                    <div className="inner-skill">
                                        <h3 className="skill-title">Control and Automation Engineering</h3>
                                        <p className="skill-text">June 2019 - December 2024</p>
                                    </div>
                                </article>
                            </div>
                        </section>
                        <section className="skills skills-grid">
                            <h2 className="sub-header">Skills</h2>
                            <div className="skill-container">
                                <Skill level={5} text="English" />
                                <Skill level={2} text="Chinese" />
                                <Skill level={4} text="Excel" />
                                <Skill level={4} text="Web Dev" />
                                <Skill level={5} text="Python" />
                                <Skill level={5} text="Ignition SCADA" />
                            </div>
                        </section>
                    </div>
                </div>
                {/* <div className="professional-skill">
                    <img className="prof-img" src={challenger} alt="" />
                    <h2>UFABC Challenger Racing Team</h2>
                    <h3>Member and Head of the Embedded Electronics department</h3>
                    <h4>January 2021 - March 2022</h4>
                    <p>
                        Developed circuits for control and measurement of the vehicle. Coordination and distribution of
                        tasks to members of the department.
                    </p>
                    <img className="prof-img" src={scania} alt="" />
                    <h2>Scania Latin America</h2>
                    <h3>Data Science and Industrial Automation Intern</h3>
                    <h4>February 2022 - Present</h4>
                    <p>
                        I extract, analyze, process and present data from the production process, creating tools for
                        data driven decision making, I also support other areas with the information they need.
                    </p>
                </div>
                <div>
                    <div className="lang-header">
                        <img className="lang-img" src={language} alt="" />
                        <h2>Languages</h2>
                    </div>
                    <Skill level={5} text="English" tagStyle="bar" />
                    <Skill level={2} text="Mandarin Chinese" tagStyle="bar" />
                </div>
            </div>
            <div>
                <div>
                    <img src={skillImg} alt="" />
                    <span>Skills</span>
                </div>
                <Skill level={4} text="Excel" />
                <Skill level={4} text="Web Dev" />
                <Skill level={5} text="Python" />
                <Skill level={5} text="Ignition SCADA" />
            </div>
            <div>
                <div>
                    <span>Education</span>
                </div>
                <div>
                    <img src={school} alt="" />
                    <div>
                        <p>ETEC Jorge Street</p>
                        <p>2016 - 2018</p>
                        <p>Electronics Technician</p>
                    </div>
                </div>
                <div>
                    <img src={school} alt="" />
                    <div>
                        <p>ETEC Jorge Street</p>
                        <p>2016 - 2018</p>
                        <p>Electronics Technician</p>
                    </div>
                </div>
                <div>
                    <img src={school} alt="" />
                    <div>
                        <p>ETEC Jorge Street</p>
                        <p>2016 - 2018</p>
                        <p>Electronics Technician</p>
                    </div>
                </div> */}
            </div>
        </div>
    );
}

export default App;
