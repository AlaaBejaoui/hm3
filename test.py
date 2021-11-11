import streamlit as st
from collections import namedtuple, defaultdict
import datetime
import pandas as pd
import calendar

def plot_1():
    
    import plotly.graph_objects as go
    import numpy as np

    r = np.linspace(0, 1, 100)
    phi = np.linspace(0, 2*np.pi, 100)

    radius_matrix, phi_matrix = np.meshgrid(r, phi)

    x = radius_matrix * np.cos(phi_matrix)
    y = radius_matrix * np.sin(phi_matrix)

    bottom = 0*x + 0*y
    top = 1 + x*y

    fig = go.Figure(data=[
        go.Surface(x=x, y=y, z=bottom),
        go.Surface(x=x, y=y, z=top)
        ])

    fig.update_layout(autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

    return fig



st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Uni_stuttgart_logo.svg/768px-Uni_stuttgart_logo.svg.png", width=200)

st.markdown("<h1 style='text-align: center; color: blue;'>Blatt 4</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: blue;'> Durchs wilde Ku R3 distan </h1>", unsafe_allow_html=True)
st.write('---')

### Aufgabe 1

st.markdown("<h1 style='text-align: center; color: green; font-size: 30px;'> Back To The Residues! </h1>", unsafe_allow_html=True)
st.header('Aufgabe 1:') 

st.write('...')
st.write('---')

### Aufgabe 2

# 2.1

st.markdown("<h1 style='text-align: center; color: green; font-size: 30px;'> Mit Integralsätzen Immer Fest Im Sattel. </h1>", unsafe_allow_html=True)
st.header('Aufgabe 2:')

st.markdown("""
1. Skizzieren Sie den Körper
""")
st.latex(r''' 
V = (x,y,z) \in \R^{3} \mid x^{2}+y^{2} \leq 1, 0 \leq z \leq 1+xy  
''')
col1_2_1, col2_2_1, col3_2_1 = st.columns(3)
help_button_2_1 = col1_2_1.button("Hinweis", key="1")
solution_button_2_1 = col2_2_1.button("Lösung", key="2")
full_solution_button_2_1 = col3_2_1.button("Ausführliche Lösung", key="22")

if help_button_2_1:
    st.info("""
    Die Übersetzung zwischen Bild und Formel, Anschauung und Rechnung, Intuition und Präzision ist zentral 
    für alle technischen Anwendungen. Sie brauchen beides! \n
    Für die analystische Geometrie nutzen Sie die Grundlagen Ihrer HM1, insbesondere Geraden und Ebenen und Quadriken wie z = 1 +xy.
    """)

if solution_button_2_1:
    fig_1 = plot_1()
    st.plotly_chart(fig_1, use_container_width=True)

st.write('---')

# 2.2

st.markdown("""
2. Die Randfläche $∂V$ besteht aus drei Teilen: Parametrisieren Sie die Bodenfläche $B$ (mit
$z = 0$), die Mantelfläche $M$ (mit $x^{2} +y^{2} = 1$) und die Deckfläche $D$ (mit $z = 1 + xy$).
""")

col1_2_2, col2_2_2, col3_2_2 = st.columns(3)
help_button_2_2 = col1_2_2.button("Hinweis",key="3")
solution_button_2_2 = col2_2_2.button("Lösung",key="4")
full_solution_button_2_2 = col3_2_2.button("Ausführliche Lösung",key="44")


if help_button_2_2:
    st.info("""
    Wenn Sie den Körper V verstehen und zeichnen können (1), dann können
    Sie auch V und seine Randfläche ∂V parametrisieren (2). Umgekehrt erleichtert eine geschickte
    Parametrisierung (2) die Skizze (1), etwa in Polarkoordinaten.
    """)

if solution_button_2_2:
    st.info("""
    $\phi_B$ : $[0,1]$ x $[0,2\pi]$ → $\R^3$ : ($r$, $\phi$) = ($r$$\cos$($\phi$), $r$$\sin$($\phi$), 0) \n
    ...
    """)

st.write('---')

# 2.3
st.markdown("""
3. Berechnen Sie den Flächeninhalt $vol_2(D)$ der Deckfläche $D$.
""")

col1_2_3, col2_2_3, col3_2_3 = st.columns(3)
help_button_2_3 =col1_2_3.button("Hinweis",key="5")
solution_button_2_3 =col2_2_3.button("Lösung",key="6")
full_solution_button_2_3 = col3_2_3.button("Ausführliche Lösung",key="66")

if help_button_2_3:
    st.info("""
    Nach diesen Vorbereitungen sind die Berechnungen (3–5) dann Routine: Sie setzen die Daten
    aus (1,2) in das jeweilige Integral ein und rechnen es sorgsam aus, so wie Sie es gelernt haben.
    Das wollen Sie möglichst effizient erledigen, genau hierzu erklärt Ihnen die HM3 die passenden
    Begriffe und Techniken, Definitionen und Sätze. 
    """)

if solution_button_2_3:
    st.info("""
    $(2\pi/3)(2\sqrt{2}-1)$
    """)
    

st.write('---')

# 2.4

st.markdown("""
4. Wir betrachten das Vektorfeld 
""")
st.latex(r''' 
f : \R^3 \to \R^3 \\ 
(x,y,z) \to (0,0,z^2)  
''')

st.markdown("""
Berechnen Sie das Flussintegral $\int_{D}^{} f \cdot dD$ von $f$ durch $D$ nach außen. \n
_Hinweis_: Es gilt $2\cos(\phi)\sin(\phi) = \sin(2\phi)$.
""")

col1_2_4, col2_2_4, col3_2_4 = st.columns(3)
help_button_2_4 =col1_2_4.button("Hinweis",key="7")
solution_button_2_4 =col2_2_4.button("Lösung",key="8")
full_solution_button_2_4 = col3_2_4.button("Ausführliche Lösung",key="88")


if help_button_2_4:
    st.info("""
    Nach diesen Vorbereitungen sind die Berechnungen (3–5) dann Routine: Sie setzen die Daten
    aus (1,2) in das jeweilige Integral ein und rechnen es sorgsam aus, so wie Sie es gelernt haben.
    Das wollen Sie möglichst effizient erledigen, genau hierzu erklärt Ihnen die HM3 die passenden
    Begriffe und Techniken, Definitionen und Sätze. 
    """)

if solution_button_2_4:
    st.info("""
    $(25/24)\pi$
    """)
    

st.write('---')


# 2.5

st.markdown("""
5. Bestimmen Sie $\int_{B}^{} f \cdot dB$ und $\int_{M}^{} f \cdot dM$ sowie $\int_{V}^{} z dV$ mit möglichst wenig Rechnung 
""")

col1_2_5, col2_2_5, col3_2_5 = st.columns(3)
help_button_2_5 =col1_2_5.button("Hinweis",key="9")
solution_button_2_5 =col2_2_5.button("Lösung",key="10")
full_solution_button_2_5 = col3_2_5.button("Ausführliche Lösung",key="1010")


if help_button_2_5:
    st.info("""
    In (5) helfen Ihnen geometrisches Verständnisund Ihre Integralsätze: Sie dürfen ausführlich rechnen, aber es gelingt auch ohne. 
    """)

if solution_button_2_5:
    st.info("""
    $\int_{B}^{} f \cdot dB$ = $0$ \n  
    $\int_{M}^{} f \cdot dM$ = $(25/24) \pi$ \n
    $\int_{V}^{} z dV$ = $(25/48) \pi$ \n
    """)
    

st.write('---')


### Aufgabe 3
st.markdown("<h1 style='text-align: center; color: green; font-size: 30px;'> Mein Unsichtbarer Freund Stockes. </h1>", unsafe_allow_html=True)
st.header('Aufgabe 3:')
st.write('...')
st.write('---')
