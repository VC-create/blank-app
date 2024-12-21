import streamlit as st

def button_click(col):
    speechContainer.audio(speechArr[col], format='audio/mpeg')

st.title("Soundboard App")
st.subheader(
    "Click on a person to hear their famous speech"
)

names = ['Martin Luther King Jr','Kamala Harris']
imgArr = ['mlk.jpg', 'kamalaharris.png']
speechArr = ['mlk.mp3', 'kamala.mp3']

cols=st.columns(2)
for c in range(0, len(names)):
    cols[c].image(imgArr[c])
    cols[c].button(names[c], on_click=button_click, args=(c,),use_container_width=True)

speechContainer=st.container(border=True)
speechContainer.write('Audio: ')


