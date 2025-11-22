# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC4.py
#  your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona la sección que deseas ver', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>El baúl de Mica</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("fotoperfil.jpg", caption='Sí, esa soy yo :)', width=300)
    col1.image("voluntariado.jpg", caption='En el voluntariado, dibujando', width=300)
    col1.image("amigosuno.jpg", caption='Aquí, con los que hacen la universidad más bonita', width=300)
    col1.image("amigosdos.jpg", caption='Aquí, con mi grupo de toda la vida', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = "¡Hola holaa! Soy Micaela, pero prefiero que me llamen Mica. Bienvenidos a mi diario, un espacio seguro donde podrás conocer un poquito más de mí :) Para quienes aún no me conocen, tengo 19 años y soy de Lima, Perú. Actualmente estudio Comunicación Audiovisual en la PUCP, una carrera que me encanta porque es súper visual, creativa y me permite dejar que mi imaginación vuele. Lo mejor es que esa creatividad se trabaja de muchas formas: programando, editando, fotografiando, grabando… ¡de todo un poco! Y eso hace que cada proyecto sea diferente y emocionante. Algo que también forma una parte muy importante de mí es que participo en un voluntariado donde apoyamos a niños con distintas realidades y necesidades. Estar con ellos me recuerda lo valioso que es acompañar, escuchar y compartir. Cada momento con esos pequeños me llena el corazón, me hace sentir útil y me enseña a ver la vida con más empatía, paciencia y amor. Es un espacio que me transforma y me inspira a ser una mejor versión de mí misma. Además, amo pasar tiempo con mi familia y mis amigos. Soy una persona que de verdad disfruta estar cerca de las personas que ama; compartir momentos, reírnos juntos, conversar o simplemente estar… todo eso me hace sentir completa y muy agradecida. En el futuro, me proyecto terminando mi carrera con mucho éxito y trabajar en una empresa grande, en un lugar donde realmente se valore el arte y la creatividad detrás de cada trabajo. También sueño con viajar por muchos lugares del mundo junto a mi familia <3 En mi tiempo libre me encanta ver series y escuchar música; sé que suena sencillo, pero de verdad me relaja muchísimo. Cuando tengo un ratito libre también me doy mi espacio para mí: me hago las uñas sola, y sí, yo solita. Además, me gusta ver tutoriales de maquillaje y aprovechar para practicar un poquito. Otra cosa que amo es hacer postres. Mis galletas y mi torta de tres leches me salen espectaculares; no lo digo por presumir, pero siempre desaparecen rapidísimo cuando las preparo. Cocinar dulce para mí es una forma de consentirme y consentir a los demás. Y bueno… por ahora ya no diré más. Prefiero dejar que ustedes entren a este baúl tan lindo y extenso que estoy creando, y lo descubran poco a poco."

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = "La verdad es que mi experiencia al inicio sí fue dura, no lo negaré. Tuve varias complicaciones y por momentos sentía que no entendía nada. Pero gracias a la enseñanza y la paciencia de mis compañeros, y sobre todo de mi jefa de práctica, Luisa, pude aprender mucho más y empezar a comprender realmente cómo funcionan los códigos✨ La programación me ha enseñado a ser mucho más cuidadosa. Suena raro, pero es real, había momentos en los que, solo por equivocarme en un punto o una letra, mi código no salía. Eso me enseñó a revisar con calma, a tener orden y a no rendirme tan rápido. Además, Python me enseñó paciencia, precisión y a confiar en mi proceso. Lo que me gusta de programar es que tú decides qué crear, cómo funciona y qué opciones dar. De chiquita siempre me preguntaba “¿qué hay detrás de los juegos?”, y ahora lo entiendo... es un proceso enorme, creativo, minucioso y súper divertido. Porque al final, es tu proyecto y tus reglas, y eso lo hace especial 😌 En el futuro me gustaría seguir usando la programación para crear más blogs de distintas categorías. Quiero hacer uno donde las chicas puedan entrar a ver tutoriales paso a paso de maquillaje, o aprender cómo hacer diferentes estilos de uñas, todo súper claro y bien explicado. Quiero que encuentren una variedad de respuestas, videos, guías y un espacio donde aprender sea bonito, fácil y divertido 😍"


    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>¿Te marean los códigos? Aquí va una guía para sobrevivir</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    st.video("https://youtu.be/w6zITFfYQVY")
    st.video("https://youtu.be/87s4m-YDsco")

    # st.video("https://youtu.be/w6zITFfYQVY"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://youtu.be/w6zITFfYQVY".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    # st.video("https://youtu.be/87s4m-YDsco"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://youtu.be/87s4m-YDsco".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    # O creamos un botón para ir al enlace del video con button
    # st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 

    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Mis primeros gráficos</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Comparación de tarjetas rojas entre equipos locales', 'Rendimiento ofensivo y defensivo del Barcelona', 'Resultados del Real Madrid como local y visitante', 'Ubicación geográfica de mis películas favoritas']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Comparación de tarjetas rojas entre equipos locales':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra que Alavés, Leganés y Sevilla son los equipos que más tarjetas rojas reciben como locales. En cambio, clubes como Barcelona, Osasuna y Real Madrid prácticamente no registran expulsiones en casa. En otras palabras, se observa que algunos equipos juegan con mayor intensidad o riesgo, mientras otros mantienen un estilo más disciplinado. </div>", unsafe_allow_html=True)
        st.image("barras.png", caption='Comparación de tarjetas rojas entre equipos locales', width=500)
        pass
    elif grafico_seleccionado == 'Rendimiento ofensivo y defensivo del Barcelona':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Barcelona anota más goles tanto de local como de visitante, con la mayoría de partidos marcando entre 2 y 4 goles. Además, recibe pocos goles en ambos casos, generalmente entre 0 y 2. El histograma muestra que el equipo mantiene un alto rendimiento ofensivo y una defensa sólida sin importar dónde juegue. </div>", unsafe_allow_html=True)
        st.image("histograma.png", caption='Rendimiento ofensivo y defensivo del Barcelona', width=500)
        pass
    elif grafico_seleccionado == 'Resultados del Real Madrid como local y visitante': 
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Como local, el Real Madrid gana casi todos sus partidos, con muy pocos empates o derrotas. Como visitante, su desempeño baja un poco, aunque gana la mayoría, sin embargo aparecen más empates y derrotas. </div>", unsafe_allow_html=True)
        st.image("pastel.png", caption='Resultados del Real Madrid como local y visitante', width=500)
        pass
    elif grafico_seleccionado == 'Ubicación geográfica de mis películas favoritas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El mapa muestra que las películas están distribuidas en distintos puntos de EE.UU. y el Reino Unido, concentrándose principalmente en ciudades estadounidenses como Nueva York, Tacoma, Florida y Atlanta. Solo una de ellas, Miss Peregrine y los niños peculiares, fue filmada en Europa. El mapa evidencia una predominancia de locaciones norteamericanas, especialmente en producciones de romance y drama.</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)
    