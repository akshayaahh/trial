# This script uses Streamlit, which must be installed and run in a supported environment.
# Please run this code using `streamlit run ancient_signup_app.py` in your local environment.

try:
    import streamlit as st

    # Page config
    st.set_page_config(page_title="ChronoQuest Sign-Up", page_icon="📜", layout="centered")

    # Background color
    st.markdown("""
        <style>
        body {
            background-color: #fdf6e3;
        }
        .title {
            font-family: 'Cinzel', serif;
            color: #4b2e2e;
            font-size: 36px;
            text-align: center;
            margin-bottom: 0;
        }
        .subtitle {
            font-family: 'IM Fell English', serif;
            color: #5a3e36;
            font-size: 20px;
            text-align: center;
            margin-top: 0;
            margin-bottom: 30px;
        }
        .form {
            background-color: #fffaf0;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.15);
        }
        </style>
    """, unsafe_allow_html=True)

    # Fonts from Google
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel&family=IM+Fell+English&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="title">Hark, Seeker of Ages!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Etch thy name upon the scroll eternal, and begin thy journey through forgotten years.</div>', unsafe_allow_html=True)

    # Sign-up Form
    with st.form("signup_form"):
        st.markdown('<div class="form">', unsafe_allow_html=True)
        name = st.text_input("🕋 Thy Name")
        email = st.text_input("📜 Thy Scroll Address (Email)")
        age = st.number_input("🌒 Years Thou Hast Walked (Age)", min_value=6, max_value=120)
        consent = st.checkbox("☑ I vow to wield knowledge with honor.")
        submit = st.form_submit_button("📜 Inscribe My Name")

        if submit:
            if not name or not email or not consent:
                st.warning("Speak truly, and fill all fields, noble one.")
            else:
                st.success(f"Hail, {name}! Thy passage through time now beginneth. 🕰️")
        st.markdown('</div>', unsafe_allow_html=True)

except ModuleNotFoundError as e:
    print("Streamlit is not available in this environment. Please run this script using 'streamlit run ancient_signup_app.py' in a local Python environment.")
