import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
#image2 = Image.open('images/cancer in thailand2.jpg')
#st.image(image2,width=600)
st.subheader('''📖 This page provides Thailand's cancer screening program data in budget year 2025''')

if 'clicked1' not in st.session_state:
    st.session_state.clicked1 = False
if 'clicked2' not in st.session_state:
    st.session_state.clicked2 = False

def click_button1():
    st.session_state.clicked1 = True
    st.session_state.clicked2 = False
def click_button2():
    st.session_state.clicked2 = True
    st.session_state.clicked1 = False

st.button('Click me', on_click=click_button1)

if st.session_state.clicked1:
    with st.container():
     st.write("This is inside the container")
    # You can call any Streamlit command, including custom components:
     components.html(
    """
     <div class='tableauPlaceholder' id='viz1734327680763' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;nh&#47;nhso_mammo&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='nhso_mammo&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;nh&#47;nhso_mammo&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='th-TH' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1734327680763');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """, height=1000 , width =1200  )

st.button('Click me2', on_click=click_button2)
if st.session_state.clicked2:
    with st.container():
     st.write("This is inside the container")
    # You can call any Streamlit command, including custom components:
     components.html(
    """
    <div class='tableauPlaceholder' id='viz1734398166723' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;nh&#47;nhso_hpv&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='nhso_hpv&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;nh&#47;nhso_hpv&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='th-TH' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1734398166723');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1377px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

    """,height=1000 , width =1200  )

  
st.subheader('👈xx Please select the graphs from this sidebar.' )
st.subheader('📊 1. Mammogram screening for breast cancer in high risk group')
st.markdown('Update data every Monday')
st.subheader('📊 2. HPV test for cervical cancer')
st.markdown('Update data monthly')
st.text('')
st.markdown('ที่มุมขวาล่าง ท่านสามารถขยายหน้าจอ,save dashboard หรือส่งต่อลิงค์')
image1 = Image.open("Capture.JPG")
st.image(image1,width=200)

st.text('')
st.text('')
st.markdown('NOTE: Thank you NHSO for providing us the valuable data ')
#st.markdown('NOTE: Thank you Tableau public (https://public.tableau.com/app/discover) for nice data visualization tool ')
st.markdown('🏥 This page was created by Digital medicine department, National Cancer Institute of Thailand, Bangkok ')
st.markdown('💬 For any comment or suggestion, please email to : it.ncithailand@gmail.com     ')
