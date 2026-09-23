import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")
image = Image.open('LiebreTortuga.jpg')
st.image(image, width=600)

try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula: La Liebre y la Tortuga")
st.write('En el mundo de los animales vivía una liebre muy orgullosa, porque ante todos decía que era la más veloz.'  
         'Por eso, constantemente se reía de la lenta tortuga.\n\n' 
         '  '
         '-¡Miren la tortuga! ¡Eh, tortuga, no corras tanto que te vas a cansar de ir tan de prisa! -decía la liebre riéndose de la tortuga.\n\n' 
         '  '
         'Un día, conversando entre ellas, a la tortuga se le ocurrió de pronto hacerle una rara apuesta a la liebre.' 
         'Estoy segura de poder ganarte una carrera -le dijo.\n\n' 
         '  '
         '-¿A mí? -preguntó, asombrada, la liebre.\n\n'
         '  '
         '-Pues sí, a ti. Pongamos nuestra apuesta en aquella piedra y veamos quién gana la carrera.'
         'La liebre, muy divertida, aceptó.\n\n'
         '  '
         'Todos los animales se reunieron para presenciar la carrera. Se señaló cuál iba a ser elcamino y la llegada.'
         'Una vez estuvo listo, comenzó la carrera entre grandes aplausos.\n\n'
         '  '
         'Confiada en su ligereza, la liebre dejó partir a la tortuga y se quedó remoloneando. ¡Vaya si le sobraba'
         'el tiempo para ganarle a tan lerda criatura!\n\n'
         '  '
         'Luego, empezó a correr, corría veloz como el viento mientras la tortuga iba despacio, pero, eso sí, sin parar.'
         'Enseguida, la liebre se adelantó muchísimo.Se detuvo al lado del camino y se sentó a descansar.'
         'Cuando la tortuga pasó por su lado, la liebre aprovechó para burlarse de ella una vez más. Le dejó ventaja y nuevamente emprendió'
         'su veloz marcha.'
         'Varias veces repitió lo mismo, pero, a pesar de sus risas, la tortuga siguió caminando sin detenerse. Confiada en su velocidad,'
         'la liebre se tumbó bajo un árbol y ahí se quedó dormida.\n\n'
         '  '
         'Mientras tanto, pasito a pasito, y tan ligero como pudo, la tortuga siguió su camino hasta llegar a la meta.'
         'Cuando la liebre se despertó, corrió con todas sus fuerzas pero ya era demasiado tarde, la tortuga había ganado la carrera.'
         'Aquel día fue muy triste para la liebre y aprendió una lección que no olvidaría jamás: No hay que burlarse jamás de los demás.'
        )

image = Image.open('gato_raton.png')
st.image(image, width=600)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula: El Gato y el Ratón.")
st.write('¡Ay! -dijo el ratón-. El mundo se hace cada día más pequeño. Al principio era tan grande que le tenía miedo. '  
         ' Corría y corría y por cierto que me alegraba ver esos muros, a diestra y siniestra, en la distancia. ' 
         ' Pero esas paredes se estrechan tan rápido que me encuentro en el último cuarto y ahí en el rincón está '  
         ' la trampa sobre la cual debo pasar. Todo lo que debes hacer es cambiar de rumbo dijo el gato...y se lo comió. ' 
         '  '
         ' Franz Kafka.'
        
        )

           
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
