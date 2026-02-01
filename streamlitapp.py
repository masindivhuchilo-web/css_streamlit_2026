import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Researcher Profile",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Researcher Profile")

# Subheading
st.subheader("Masindi Vhutshilo")

# Short bio
st.write("""
I am a Mathematics and Applied Mathematics student at the **University of Venda**.
My academic interests lie in numerical methods, partial differential equations,
computational modelling, and data-driven approaches to real-world problems.

My current research focuses on **integrating Machine Learning techniques
to predict infectious disease dynamics**, with a specific focus on
**Hookworm infection**.
""")

# Divider
st.divider()

# Research Topic
st.header("🧠 Research Topic")
st.write("""
**Integrating Machine Learning in Predicting Infectious Disease Dynamics
(Focus: Hookworm Infection)**
""")

# Research Interests
st.header("🔬 Research Interests")
st.markdown("""
- Mathematical modelling of infectious diseases  
- Machine learning applications in epidemiology  
- Numerical methods for ODEs and PDEs  
- Computational and multiscale modelling  
- Environmental and health-related data analysis  
""")

# Projects section
st.header("📂 Selected Academic Work")
st.write("""
- Machine Learning Models for Hookworm Infection Dynamics  
- Numerical Solutions of Competing Species Models  
- Multiscale Modelling of Infectious Disease Systems  
- Drought Level Prediction in Farming Across Africa  
""")

# Skills
st.header("🛠 Skills")
st.markdown("""
- Python, MATLAB  
- Streamlit  
- LaTeX  
- Numerical Analysis  
- Data Visualization  
- Scientific Computing  
""")

# Contact information
st.header("📧 Contact Information")
st.write("""
**Personal Email:** masindivhuchilo@gmail.com  
**Student Email:** 21010520@mvula.univen.ac.za  
**Phone:** 071 406 2209 / 076 533 0429  
**Institution:** University of Venda  
""")





