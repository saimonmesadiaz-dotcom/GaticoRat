import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.markdown("""
<style>
    .stApp {
        background-color: #16516e;
    }
</style>
""", unsafe_allow_html=True)

st.title("Cuenta historias a partir de fotos")
st.subheader("Repositorio realizado por: Simon Mesa Diaz")
image = Image.open('PeriquitosCiudad.jpeg')
st.image(image, width=550)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña interpretación de la foto y la historia detrás de estos pequeños periquitos.")
st.write('Un amor que se ganó con valentía. En lo alto de los árboles, una batalla silenciosa de alas,'
         'instinto y coraje terminó uniendo a dos pequeños periquitos. Él, el de matices azules, se enfrentó'
         'a otro macho por el amor de ella, y aunque no fue el más fuerte, metafóricamente fue quien mostró'
         'su mejor versión. Hoy comparten una rama, un refugio y la tranquilidad de estar juntos. La imagen'
         'representa el amor, el valor y la compañía, recordándonos que, a veces, el amor no se encuentra… se conquista.'
         'Esta fotografía fue tomada el 19 de agosto de 2026, al salir de la universidad mientras regresaba a casa, en'
         'un encuentro inesperado con una pequeña historia de amor en medio del camino. ')
        
st.write('Autoría: Simón Mesa Díaz')
        
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
