import streamlit as st
import os
import time
import glob
from gtts import gTTS
from PIL import Image
import base64


# =========================================================
# CONFIGURACIÓN DE LA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Conversión de Texto a Audio",
    page_icon=None,
    layout="wide"
)


# =========================================================
# ESTILOS VISUALES
# =========================================================

st.markdown("""
<style>

    /* =====================================================
       FONDO GENERAL
       ===================================================== */

    .stApp {
        background-color: #B8C48A;
    }


    /* =====================================================
       CONTENEDOR PRINCIPAL
       ===================================================== */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }


    /* =====================================================
       TÍTULO PRINCIPAL
       ===================================================== */

    h1 {
        color: #3E4630 !important;
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.2rem !important;
    }


    /* =====================================================
       SUBTÍTULOS
       ===================================================== */

    h2 {
        color: #4A5038 !important;
        font-size: 1.6rem !important;
        margin-top: 0.3rem !important;
        margin-bottom: 1rem !important;
    }

    h3 {
        color: #4A5038 !important;
    }


    /* =====================================================
       AUTOR
       ===================================================== */

    .autor {
        text-align: center;
        color: #596044;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }


    /* =====================================================
       TARJETAS DE LAS FÁBULAS
       ===================================================== */

    .card {
        background-color: #E8DCC3;
        padding: 1.4rem 2rem;
        border-radius: 18px;
        margin-top: 1.3rem;
        margin-bottom: 1.3rem;
        box-shadow: 0px 5px 15px rgba(60, 65, 40, 0.12);
        border: 1px solid rgba(90, 85, 60, 0.15);
    }


    /* =====================================================
       TEXTO DE LAS FÁBULAS
       ===================================================== */

    .cuento {
        color: #39382F;
        font-size: 1rem;
        line-height: 1.55;
        text-align: justify;
    }

    .cuento p {
        margin-top: 0;
        margin-bottom: 0.7rem;
    }


    /* =====================================================
       IMÁGENES
       ===================================================== */

    [data-testid="stImage"] {
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }


    /* =====================================================
       TARJETA DE AUDIO
       ===================================================== */

    .audio-card {
        background-color: #E8DCC3;
        padding: 1.5rem 2rem;
        border-radius: 18px;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0px 5px 15px rgba(60, 65, 40, 0.12);
        border: 1px solid rgba(90, 85, 60, 0.15);
    }


    /* =====================================================
       TEXTO DE INTRODUCCIÓN
       ===================================================== */

    .descripcion {
        color: #555441;
        font-size: 1rem;
        margin-bottom: 1rem;
    }


    /* =====================================================
       TEXT AREA
       ===================================================== */

    textarea {
        color: #222222 !important;
        background-color: #F4EBDD !important;
        border-radius: 10px !important;
    }

    textarea::placeholder {
        color: #77756B !important;
    }


    /* =====================================================
       SELECTBOX
       ===================================================== */

    div[data-baseweb="select"] > div {
        background-color: #F4EBDD !important;
        border-radius: 10px !important;
        color: #222222 !important;
    }


    /* =====================================================
       BOTÓN
       ===================================================== */

    .stButton > button {
        background-color: #69734A;
        color: #F4EBDD;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        transition: 0.2s;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #515A38;
        color: #F4EBDD;
    }


    /* =====================================================
       AUDIO
       ===================================================== */

    .audio-title {
        color: #4A5038;
        font-size: 1.4rem;
        font-weight: 700;
        margin-top: 1.2rem;
        margin-bottom: 0.5rem;
    }


    /* =====================================================
       SEPARADORES
       ===================================================== */

    hr {
        border: none;
        height: 1px;
        background-color: rgba(70, 75, 50, 0.25);
        margin: 1.5rem 0;
    }


    /* =====================================================
       SIDEBAR
       Se conserva el contenido original
       ===================================================== */

    section[data-testid="stSidebar"] {
        background-color: #AAB67D;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p {
        color: #3E4630 !important;
    }


    /* =====================================================
       PIE DE PÁGINA
       ===================================================== */

    .footer {
        text-align: center;
        color: #596044;
        margin-top: 2rem;
        font-size: 0.85rem;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# CARPETA TEMPORAL
# =========================================================

try:
    os.mkdir("temp")
except:
    pass


# =========================================================
# ENCABEZADO
# =========================================================

st.title("Conversión de Texto a Audio")

st.markdown(
    '<div class="autor">Hecho por: Simón Mesa Díaz</div>',
    unsafe_allow_html=True
)


# =========================================================
# IMAGEN LIEBRE Y TORTUGA
# =========================================================

image = Image.open("LiebreTortuga.jpg")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(image, use_container_width=True)


# =========================================================
# FÁBULA 1
# =========================================================

st.markdown("""
<div class="card">

<h2>Una pequeña Fábula: La Liebre y la Tortuga</h2>

<div class="cuento">

En el mundo de los animales vivía una liebre muy orgullosa,
porque ante todos decía que era la más veloz. Por eso,
constantemente se reía de la lenta tortuga.

<br>

—¡Miren la tortuga! ¡Eh, tortuga, no corras tanto que te vas
a cansar de ir tan de prisa! —decía la liebre riéndose de la tortuga.

<br>

Un día, conversando entre ellas, a la tortuga se le ocurrió
de pronto hacerle una rara apuesta a la liebre.

<br>

—Estoy segura de poder ganarte una carrera —le dijo.

<br>

—¿A mí? —preguntó, asombrada, la liebre.

<br>

—Pues sí, a ti. Pongamos nuestra apuesta en aquella piedra
y veamos quién gana la carrera.

<br>

La liebre, muy divertida, aceptó.

<br>

Todos los animales se reunieron para presenciar la carrera.
Se señaló cuál iba a ser el camino y la llegada.
Una vez estuvo listo, comenzó la carrera entre grandes aplausos.

<br>

Confiada en su ligereza, la liebre dejó partir a la tortuga
y se quedó remoloneando. ¡Vaya si le sobraba el tiempo para
ganarle a tan lerda criatura!

<br>

Luego, empezó a correr, corría veloz como el viento mientras
la tortuga iba despacio, pero, eso sí, sin parar.

<br>

Enseguida, la liebre se adelantó muchísimo. Se detuvo al lado
del camino y se sentó a descansar.

<br>

Cuando la tortuga pasó por su lado, la liebre aprovechó para
burlarse de ella una vez más. Le dejó ventaja y nuevamente
emprendió su veloz marcha.

<br>

Varias veces repitió lo mismo, pero, a pesar de sus risas,
la tortuga siguió caminando sin detenerse.

<br>

Confiada en su velocidad, la liebre se tumbó bajo un árbol
y ahí se quedó dormida.

<br>

Mientras tanto, pasito a pasito, y tan ligero como pudo,
la tortuga siguió su camino hasta llegar a la meta.

<br>

Cuando la liebre se despertó, corrió con todas sus fuerzas
pero ya era demasiado tarde, la tortuga había ganado la carrera.

<br>

Aquel día fue muy triste para la liebre y aprendió una lección
que no olvidaría jamás:

<br>

<b>No hay que burlarse jamás de los demás.</b>

</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# IMAGEN GATO Y RATÓN
# =========================================================

image = Image.open("gato_raton.png")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(image, use_container_width=True)


# =========================================================
# FÁBULA 2
# =========================================================

st.markdown("""
<div class="card">

<h2>Una pequeña Fábula: El Gato y el Ratón</h2>

<div class="cuento">

¡Ay! —dijo el ratón—. El mundo se hace cada día más pequeño.
Al principio era tan grande que le tenía miedo. Corría y corría
y por cierto que me alegraba ver esos muros, a diestra y siniestra,
en la distancia.

<br>

Pero esas paredes se estrechan tan rápido que me encuentro en
el último cuarto y ahí en el rincón está la trampa sobre la cual
debo pasar.

<br>

Todo lo que debes hacer es cambiar de rumbo —dijo el gato...
y se lo comió.

<br>

<i>Franz Kafka.</i>

</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# CONVERSIÓN A AUDIO
# =========================================================

st.markdown("""
<div class="audio-card">

<h2>Conversión de texto a audio</h2>

<div class="descripcion">
Quieres escucharlo? Copia el texto que deseas convertir en audio.
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# TEXT AREA
# =========================================================

text = st.text_area(
    "Ingrese El texto a escuchar.",
    height=180
)


# =========================================================
# IDIOMA
# =========================================================

option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English")
)

if option_lang == "Español":
    lg = "es"

if option_lang == "English":
    lg = "en"


# =========================================================
# TEXTO A AUDIO
# =========================================================

def text_to_speech(text, tld, lg):

    tts = gTTS(
        text=text,
        lang=lg
    )

    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"

    my_file_name = "".join(
        c for c in my_file_name
        if c.isalnum() or c in (" ", "_", "-")
    )

    if not my_file_name:
        my_file_name = "audio"

    tts.save(
        f"temp/{my_file_name}.mp3"
    )

    return my_file_name, text


# =========================================================
# BOTÓN
# =========================================================

if st.button("Convertir a Audio"):

    if text.strip() == "":
        st.warning(
            "Primero escribe o pega un texto para convertirlo en audio."
        )

    else:

        result, output_text = text_to_speech(
            text,
            "com",
            lg
        )

        audio_file = open(
            f"temp/{result}.mp3",
            "rb"
        )

        audio_bytes = audio_file.read()

        st.markdown(
            '<div class="audio-title">Tu audio:</div>',
            unsafe_allow_html=True
        )

        st.audio(
            audio_bytes,
            format="audio/mp3",
            start_time=0
        )


        # =================================================
        # DESCARGA
        # =================================================

        with open(
            f"temp/{result}.mp3",
            "rb"
        ) as f:

            data = f.read()


        def get_binary_file_downloader_html(
            bin_file,
            file_label="File"
        ):

            bin_str = base64.b64encode(data).decode()

            href = f'''
            <a href="data:application/octet-stream;base64,{bin_str}"
            download="{os.path.basename(bin_file)}">
            Descargar {file_label}
            </a>
            '''

            return href


        st.markdown(
            get_binary_file_downloader_html(
                f"temp/{result}.mp3",
                file_label="Audio"
            ),
            unsafe_allow_html=True
        )


# =========================================================
# ELIMINAR ARCHIVOS ANTIGUOS
# =========================================================

def remove_files(n):

    mp3_files = glob.glob("temp/*mp3")

    if len(mp3_files) != 0:

        now = time.time()
        n_days = n * 86400

        for f in mp3_files:

            if os.stat(f).st_mtime < now - n_days:

                os.remove(f)


remove_files(7)


# =========================================================
# SIDEBAR ORIGINAL
# =========================================================

with st.sidebar:

    st.subheader(
        "Esrcibe y/o selecciona texto para ser escuchado."
    )


# =========================================================
# PIE DE PÁGINA
# =========================================================

st.markdown(
    """
    <div class="footer">
        Proyecto de conversión de texto a audio · Simón Mesa Díaz
    </div>
    """,
    unsafe_allow_html=True
)
