import streamlit as st
import PyPDF2
import pandas as pd

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title(" AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

skills_database = [
    "Python",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "Data Analysis",
    "Pandas",
    "NumPy",
    "OpenCV",
    "Streamlit",
    "Flask",
    "FastAPI",
    "Java",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "MySQL",
    "MongoDB",
    "Git",
    "GitHub",
    "APIs",
    "TensorFlow",
    "Power BI",
    "Excel"
]

st.sidebar.header(" Add Custom Skills")

new_skill = st.sidebar.text_input(
    "Enter New Skill"
)

if st.sidebar.button("Add Skill"):

    if new_skill != "":

        if new_skill not in skills_database:

            skills_database.append(new_skill)

            st.sidebar.success(
                f"{new_skill} Added Successfully"
            )

        else:

            st.sidebar.warning(
                "Skill Already Exists"
            )

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:

        text = page.extract_text()

        if text:

            resume_text += text

    st.subheader(" Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )

    detected_skills = []

    for skill in skills_database:

        if skill.lower() in resume_text.lower():

            detected_skills.append(skill)

    st.subheader(" Detected Skills")

    if len(detected_skills) > 0:

        skills_df = pd.DataFrame(
            detected_skills,
            columns=["Detected Skills"]
        )

        st.dataframe(skills_df)

    else:

        st.warning("No Skills Detected")


    ats_score = min(len(detected_skills) * 5, 100)

    st.subheader(" ATS Score")

    st.progress(ats_score)

    st.success(f"ATS Score: {ats_score}%")


    if ats_score >= 80:

        st.success("Excellent Resume")

    elif ats_score >= 60:

        st.info("Good Resume But Can Improve")

    else:

        st.warning("Resume Needs Improvement")

    important_skills = [
        "Python",
        "SQL",
        "Git",
        "GitHub",
        "Machine Learning",
        "APIs"
    ]

    missing_skills = []

    for skill in important_skills:

        if skill not in detected_skills:

            missing_skills.append(skill)


    st.subheader("⚠ Missing Important Skills")

    if len(missing_skills) > 0:

        missing_df = pd.DataFrame(
            missing_skills,
            columns=["Missing Skills"]
        )

        st.dataframe(missing_df)

    else:

        st.success("No Important Skills Missing")


    st.subheader(" Resume Suggestions")

    suggestions = []

    if "Python" not in detected_skills:

        suggestions.append(
            "Add Python Projects"
        )

    if "SQL" not in detected_skills:

        suggestions.append(
            "Add SQL Skills"
        )

    if "GitHub" not in detected_skills:

        suggestions.append(
            "Add GitHub Profile"
        )

    if "Machine Learning" not in detected_skills:

        suggestions.append(
            "Add Machine Learning Projects"
        )

    if ats_score < 60:

        suggestions.append(
            "Improve Technical Skills Section"
        )

    if len(suggestions) > 0:

        for suggestion in suggestions:

            st.write(f" {suggestion}")

    else:

        st.success(
            "Your Resume Looks Strong"
        )

    st.subheader(" Skills Database")

    skills_database_df = pd.DataFrame(
        skills_database,
        columns=["Available Skills"]
    )

    st.dataframe(skills_database_df)

else:

    st.info(" Please Upload Resume PDF")
