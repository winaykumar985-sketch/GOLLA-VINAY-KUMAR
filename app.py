import streamlit as st

# Configure the page
st.set_page_config(page_title="Golla Vinay Kumar | Portfolio", page_icon="💼", layout="wide")

# Custom CSS for cleaner styling
st.markdown("""
    <style>
    .main-header { font-size: 2.5rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0px;}
    .sub-header { font-size: 1.25rem; font-weight: 400; color: #4B5563; margin-bottom: 20px;}
    .section-header { font-size: 1.5rem; font-weight: 600; color: #1F2937; margin-top: 20px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px;}
    </style>
""", unsafe_allow_html=True)

# Sidebar for Contact Info
with st.sidebar:
    st.header("Contact Info")
    st.write("📍 **Location:** Bengaluru, Karnataka")
    st.markdown("---")
    st.write("**Target Roles:**")
    st.write("Entry-level Technical, MIS, or Business Analytics")

# Main Content
st.markdown('<div class="main-header">Golla Vinay Kumar</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">MBA Candidate in Business Analytics | B.Com in Computer Applications</div>', unsafe_allow_html=True)

st.write(
    "I am a Bangalore-based professional with a strong foundation in computer applications and business operations. "
    "Currently pursuing an MBA specializing in Business Analytics, I am passionate about utilizing data management tools "
    "and process automation to solve practical business problems. I am seeking entry-level "
    "technical and MIS roles to leverage my analytical foundation."
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)
    st.write("**Master of Business Administration (MBA)** - Business Analytics")
    st.write("*Atria Institute of Technology, Bengaluru*")
    st.write("")
    st.write("**Bachelor of Commerce (B.Com)** - Computer Applications")
    st.write("*Sri Krishnadevaraya University* (Graduated: 2025)")

with col2:
    st.markdown('<div class="section-header">🛠️ Technical Skills</div>', unsafe_allow_html=True)
    st.write("- **Data Management:** Microsoft Excel (XLOOKUP, Pivot Tables, Power Query, SUMIFS), Oracle SQL*Plus, Google Apps Script.")
    st.write("- **Programming:** Python (Fundamentals, conditional logic, loops), HTML, CSS, JavaScript.")
    st.write("- **Software Testing:** Manual and foundational testing methodologies.")

st.markdown('<div class="section-header">🚀 Projects & Certifications</div>', unsafe_allow_html=True)

# Project and Certification Expanders
with st.expander("Educational & Interactive Web Applications"):
    st.write("Developed **PowerCall** using React and Tailwind CSS, and a 3-lane educational math runner game hosted via GitHub Pages covering curriculum for Class 1 to 10.")

with st.expander("Professional Certifications & Training"):
    st.write("- **Flipkart Supply Chain Operations Academy:** Achieved a 90% score on the digital assessment.")
    st.write("- **Software Testing Training:** Completed comprehensive testing training at QSpiders, Hebbal.")
    st.write("- **Financial & Business Training:** Completed Tally Prime Level 1 certification, Tata Capital Financial Literacy training, and BDE BFSI training at MITRAz Skills.")
