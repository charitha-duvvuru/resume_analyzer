import streamlit as st
import subprocess

def main():
    st.title("Resume Screening and Analyzer")
    st.write("#")
    st.write("#")


    if st.button("Job Role Prediction",use_container_width=True):
        subprocess.run(["streamlit", "run", "app1.py"])
    
    elif st.button("Resume Analysis",use_container_width=True):
        subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    main()
