import foto from "../src/img/foto.jpg";
import challenger from "../src/img/challenger.jpg";
import scania from "../src/img/scania.jpg";
import school from "../src/img/school.svg";
import language from "../src/img/language.svg";
import skillImg from "../src/img/skill.svg";
import styles from "../src/styles.module.css";
import Skill from "../src/components/Skill";

function App() {
    return (
        <div className="App">
            <div className={styles.gridContainer}>
                <div className={styles.header}>
                    <h1 className={styles.name}>Nikolas Avelino Grande</h1>
                    <img className={styles.personalImage} src={foto} alt="" />
                </div>
                <div className={styles.experienceContainer}>
                    <div className={styles.singleExperience}>
                        <img src={challenger} className={styles.jobIcon} alt="" />
                        <h2 className={styles.companyTitle}>UFABC Challenger Racing Team</h2>
                        <h3 className={styles.jobRole}>Member and Head of the Embedded Electronics department</h3>
                        <h4 className={styles.jobPeriod}>January 2021 - March 2022</h4>
                        <p className={styles.jobDescription}>
                            Developed circuits for control and measurement of the vehicle. Coordination and distribution
                            of tasks to members of the department.
                        </p>
                    </div>
                    <div className={styles.singleExperience}>
                        <img src={scania} className={styles.jobIcon} alt="" />
                        <h2 className={styles.companyTitle}>Scania Latin America</h2>
                        <h3 className={styles.jobRole}>Data Science and Industrial Automation Intern</h3>
                        <h4 className={styles.jobPeriod}>February 2022 - Present</h4>
                        <p className={styles.jobDescription}>
                            I extract, analyze, process and present data from the production process, creating tools for
                            data driven decision making, I also support other areas with the information they need.
                        </p>
                    </div>
                </div>
                <div className={styles.skillsContainer}>
                    <div className={styles.skillsHeader}>
                        <img className={styles.skillsImg} src={skillImg} alt="" />
                        <span className={styles.skillsTitle}>Skills</span>
                    </div>
                    <Skill level={4} text="Excel" />
                    <Skill level={4} text="Web Dev" />
                    <Skill level={5} text="Python" />
                    <Skill level={5} text="Ignition SCADA" />
                </div>
                <div className={styles.languagesContainer}>
                    <div className={styles.skillsHeader}>
                        <img className={styles.skillsImg} src={language} alt="" />
                        <span className={styles.skillsTitle}>Languages</span>
                    </div>
                    <Skill level={5} text="English" tagStyle="bar" />
                    <Skill level={2} text="Mandarin Chinese" tagStyle="bar" />
                </div>
                <div className={styles.educationContainer}>
                    <div className={styles.skillsHeader}>
                        <span className={styles.skillsTitle}>Education</span>
                    </div>
                    <div className={styles.singleEducation}>
                        <img className={styles.educationImg} src={school} alt="" />
                        <div className={styles.educationSubDiv}>
                            <p className={styles.educationInstitution}>ETEC Jorge Street</p>
                            <p className={styles.educationPeriod}>2016 - 2018</p>
                            <p className={styles.educationDegree}>Electronics Technician</p>
                        </div>
                    </div>
                    <div className={styles.singleEducation}>
                        <img className={styles.educationImg} src={school} alt="" />
                        <div className={styles.educationSubDiv}>
                            <p className={styles.educationInstitution}>ETEC Jorge Street</p>
                            <p className={styles.educationPeriod}>2016 - 2018</p>
                            <p className={styles.educationDegree}>Electronics Technician</p>
                        </div>
                    </div>
                    <div className={styles.singleEducation}>
                        <img className={styles.educationImg} src={school} alt="" />
                        <div className={styles.educationSubDiv}>
                            <p className={styles.educationInstitution}>ETEC Jorge Street</p>
                            <p className={styles.educationPeriod}>2016 - 2018</p>
                            <p className={styles.educationDegree}>Electronics Technician</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default App;
