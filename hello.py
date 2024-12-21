import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
#image2 = Image.open('images/cancer in thailand2.jpg')
#st.image(image2,width=600)
st.subheader('''📖 This page provides Thailand's cancer screening program data in budget year 2025''')


st.subheader('📊 1. Mammogram screening for breast cancer in high risk group')
col1, col2 = st.columns([1, 5])
with col2:
    st.markdown(' 👈🏻 Click here (Update data every Monday)')
with col1:
    if st.button("Mammogram 👧🏻📝"):
       st.switch_page("pages/1_screening_mammogram.py")

st.subheader('📊 2. HPV test for cervical cancer')
st.markdown('Click here 🡻 (Update data monthly)')
if st.button("HPV 🦠👩‍⚕🧬🩺💉"):
    st.switch_page("pages/2_screening_hpv.py")
    
st.text('')
st.text('')
st.markdown('📌 ที่มุมขวาล่าง ท่านสามารถขยายหน้าจอ,save dashboard หรือส่งต่อลิงค์')
image1 = Image.open("Capture.JPG")
st.image(image1,width=200)

st.text('')
st.text('')
st.markdown('📌 NOTE: Thank you NHSO for providing us the valuable data ')
#st.markdown('NOTE: Thank you Tableau public (https://public.tableau.com/app/discover) for nice data visualization tool ')
st.markdown('🏥 This page was created by Digital medicine department, National Cancer Institute of Thailand, Bangkok ')
st.markdown('💬 For any comment or suggestion, please email to : it.ncithailand@gmail.com     ')
