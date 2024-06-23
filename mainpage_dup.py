import streamlit as st
import subprocess


def main():
    st.title("Resume Screening and Analyzer")
    st.write("#")
    st.write("#")
   
    job_role_prediction = st.markdown(
        """
        <style>
        .button {
            background-color: #48e39b;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 10px;
        }
        .button:hover {
            background-color: #48e39b;
        }
        </style>
        <button class="button">job role prediction</button>
        """,
        unsafe_allow_html=True
    )

    # Check if the button is clicked
    if job_role_prediction:
        st.session_state.button_clicked = True
        subprocess.run(["streamlit", "run", "app1.py"])


if __name__ == "__main__":
    main()
