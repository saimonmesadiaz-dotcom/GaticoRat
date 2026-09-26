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
    page_title="Fábulas a Audio",
    page_icon="🐢",
    layout="wide"
)

# =========================================================
# ESTILOS VISUALES
# =========================================================

st.markdown("""
<style>

    /* ===== FONDO GENERAL ===== */

    .stApp {
        background: linear-gradient(
            135deg,
            #FFF8E7 0%,
            #F6E7CB 45%,
            #E8D5B7 100%
        );
    }

    /* ===== QUITAR ESPACIO SUPERIOR EXCESIVO ===== */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* ===== TÍTULO PRINCIPAL ===== */

    h1 {
        color: #4A3520 !important;
        text-align: center;
        font-size: 3rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.2rem;
    }

    /* ===== SUBTÍTULOS ===== */

    h2, h3 {
        color: #5B4028 !important;
    }

    /* ===== AUTOR ===== */

    .autor {
        text-align: center;
        color: #876B4A;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* ===== TARJETAS ===== */

    .card {
        background: rgba(255, 255, 255, 0.88);
        padding: 2rem;
        border-radius: 24px;
        margin-top: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0px 8px 25px rgba(74, 53, 32, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.7);
    }

    /* ===== TEXTO DE LAS FÁBULAS ===== */

    .cuento {
        color: #3F3328;
        font-size: 1.05rem;
        line-height: 1.8;
        text-align: justify;
    }

    /* ===== CAJA DE CONVERSIÓN ===== */

    .audio-card {
        background: rgba(255, 255, 255, 0.94);
        padding: 2rem;
        border-radius: 24px;
        margin-top: 2rem;
        box-shadow: 0px 8px 25px rgba(74, 53, 32, 0.14);
    }

    /* ===== ÁREA DE TEXTO ===== */

    textarea {
        color: #222222 !important;
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
    }

    textarea::placeholder {
        color: #777777 !important;
    }

    /* ===== BOTÓN ===== */

    .stButton > button {
        background-color: #8B5E3C;
        color: white;
        border: none;
        border-radius: 14px;
        padding: 0.65rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        transition: 0.2s;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #6F472C;
        color: white;
        transform: translateY(-2px);
    }

    /* ===== SELECTBOX ===== */

    div[data-baseweb="select"] > div {
        background-color: white !important;
        border-radius: 12px !important;
        color: #222222 !important;
    }

    /* ===== SIDEBAR ===== */

    section[data-testid="stSidebar"] {
        background: #E8D5B7;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p {
        color: #4A3520 !important;
    }

    /* ===== SEPARADORES ===== */

    hr {
        border: none;
        height: 1px;
        background: rgba(91, 64, 40, 0.2);
        margin: 2.5rem 0;
    }

    /* ===== TEXTO DE AUDIO ===== */

    .audio-title {
        color: #5B4028;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 1.5rem;
    }

    /* ===== PIE ===== */

    .footer {
        text-align: center;
        color: #876B4A;
        margin-top: 3rem;
        font-size: 0.9rem;
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

st.markdown(
    '<h1>🐢 Fábulas a Audio 🐇</h1>',
    unsafe_allow_html=True
)

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
    <h2>🐇 La Liebre y la Tortuga</h2>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cuento">

En el mundo de los animales vivía una liebre muy orgullosa,
porque ante todos decía que era la más veloz. Por eso,
constantemente se reía de la lenta tortuga.

<br><br>

—¡Miren la tortuga! ¡Eh, tortuga, no corras tanto que te vas
a cansar de ir tan de prisa! —decía la liebre riéndose de la tortuga.

<br><br>

Un día, conversando entre ellas, a la tortuga se le ocurrió
de pronto hacerle una rara apuesta a la liebre.

<br><br>

—Estoy segura de poder ganarte una carrera —le dijo.

<br><br>

—¿A mí? —preguntó, asombrada, la liebre.

<br><br>

—Pues sí, a ti. Pongamos nuestra apuesta en aquella piedra
y veamos quién gana la carrera.

<br><br>

La liebre, muy divertida, aceptó.

<br><br>

Todos los animales se reunieron para presenciar la carrera.
Se señaló cuál iba a ser el camino y la llegada. Una vez estuvo
listo, comenzó la carrera entre grandes aplausos.

<br><br>

Confiada en su ligereza, la liebre dejó partir a la tortuga
y se quedó remoloneando. ¡Vaya si le sobraba el tiempo para
ganarle a tan lerda criatura!

<br><br>

Luego, empezó a correr, corría veloz como el viento mientras
la tortuga iba despacio, pero, eso sí, sin parar.

<br><br>

Enseguida, la liebre se adelantó muchísimo. Se detuvo al lado
del camino y se sentó a descansar.

<br><br>

Cuando la tortuga pasó por su lado, la liebre aprovechó para
burlarse de ella una vez más. Le dejó ventaja y nuevamente
emprendió su veloz marcha.

<br><br>

Varias veces repitió lo mismo, pero, a pesar de sus risas,
la tortuga siguió caminando sin detenerse.

<br><br>

Confiada en su velocidad, la liebre se tumbó bajo un árbol
y ahí se quedó dormida.

<br><br>

Mientras tanto, pasito a pasito, y tan ligero como pudo,
la tortuga siguió su camino hasta llegar a la meta.

<br><br>

Cuando la liebre se despertó, corrió con todas sus fuerzas
pero ya era demasiado tarde, la tortuga había ganado la carrera.

<br><br>

Aquel día fue muy triste para la liebre y aprendió una lección
que no olvidaría jamás:

<br><br>

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
    <h2>🐱 El Gato y el Ratón</h2>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cuento">

¡Ay! —dijo el ratón—. El mundo se hace cada día más pequeño.

<br><br>

Al principio era tan grande que le tenía miedo. Corría y corría
y por cierto que me alegraba ver esos muros, a diestra y siniestra,
en la distancia.

<br><br>

Pero esas paredes se estrechan tan rápido que me encuentro en
el último cuarto y ahí en el rincón está la trampa sobre la cual
debo pasar.

<br><br>

Todo lo que debes hacer es cambiar de rumbo —dijo el gato...

<br><br>

<b>...y se lo comió.</b>

<br><br>

<i>Franz Kafka.</i>

</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# CONVERSIÓN A AUDIO
# =========================================================

st.markdown("""
<div class="audio-card">
    <h2>🎧 Convierte una fábula en audio</h2>
    <p style="color:#6B5745;">
        Copia o escribe un texto y selecciona el idioma
        en el que quieres escucharlo.
    </p>
</div>
""", unsafe_allow_html=True)


text = st.text_area(
    "Texto para escuchar",
    placeholder="Escribe o pega aquí el texto de la fábula...",
    height=200
)


option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English")
)


if option_lang == "Español":
    lg = "es"
else:
    lg = "en"


# =========================================================
# FUNCIÓN TEXTO A AUDIO
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

    # Evitar caracteres problemáticos en el nombre
    my_file_name = "".join(
        c for c in my_file_name
        if c.isalnum() or c in (" ", "_", "-")
    )

    if not my_file_name:
        my_file_name = "audio"

    tts.save(f"temp/{my_file_name}.mp3")

    return my_file_name, text


# =========================================================
# BOTÓN DE CONVERSIÓN
# =========================================================

if st.button("🔊 Convertir a Audio"):

    if text.strip() == "":
        st.warning("Primero escribe o pega un texto para convertirlo en audio.")

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
            '<div class="audio-title">🎵 Tu audio:</div>',
            unsafe_allow_html=True
        )

        st.audio(
            audio_bytes,
            format="audio/mp3",
            start_time=0
        )


        # =================================================
        # DESCARGA DEL AUDIO
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
            ⬇️ Descargar {file_label}
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
# ELIMINAR AUDIOS ANTIGUOS
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
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <h2>📖 Fábulas a Audio</h2>

        <p>
        Escribe o copia un texto y conviértelo
        en una narración de audio.
        </p>

        <hr>

        <p>
        🐇 La Liebre y la Tortuga
        </p>

        <p>
        🐱 El Gato y el Ratón
        </p>
        """,
        unsafe_allow_html=True
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
