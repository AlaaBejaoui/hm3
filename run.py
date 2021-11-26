from utilities import *
from plots import *

add_title(title="hm-interactive", color="blue", align="center", fontsize=40)

### Blatt 2 ###

add_sheet(title="Blatt 2: Fubinisierst du noch oder transformierst du schon?", color="green", align="center", fontsize=30)

### Aufgabe P1

add_exercise(title="Aufgabe P1:", color="black", align="left", fontsize=20) 

add_equation_in_latex("V = \left\{\left(x,y,z\\right) \in \R^{3} \ \\bigg \\vert \ x^{2}+y^{2}+z^{2} \leq 4, \ 1 \leq z \leq \\frac{3}{2}, \ x \geq 0, \ x \geq y \\right\}")

_, col_b_2_p_1, _ = create_columns(3)

button_b_2_p_1 = create_checkbox(method="to_column", col=col_b_2_p_1, name="3D Graphik zeigen", key="2p1")

if button_b_2_p_1:
    add_plot(blatt_02_P_01())

### Aufgabe H1

add_exercise('Aufgabe H1:', color="black", align="left", fontsize=20)

add_equation_in_latex("E=\left\{\left(x, y, z\\right) \in \R^{3} \ \\bigg \\vert \ \\frac{x^{2}}{9}+\\frac{y^{2}}{9}+\\frac{z^{2}}{4} \leq 1, \ x \leq 0, \ z \geq 0 \\right\}")

_, col_b_2_h_1, _ = create_columns(3)

button_b_2_h_1 = create_checkbox(method="to_column", col=col_b_2_h_1, name="3D Graphik zeigen", key="2h1")

if button_b_2_h_1:
    add_plot(blatt_02_H_01())

add_seperation_line()

### Blatt 4 ###

add_sheet(title="Blatt 4: Durchs wilde KuRdistan", color="green", align="center", fontsize=30)

### Aufgabe P2

add_exercise('Aufgabe P2:', color="black", align="left", fontsize=20) 

add_equation_in_latex("V = \left\{\left(x,y,z\\right) \in \R^{3} \ \\big \\vert \ x^{2}+y^{2} \leq 1, \ 0 \leq z \leq 1+xy \\right\}")

_, col_b_4_p_2, _ = create_columns(3)

button_b_4_p_2 = create_checkbox(method="to_column", col=col_b_4_p_2, name="3D Graphik zeigen", key="4p2")

if button_b_4_p_2:
    add_plot(blatt_04_P_02())

### Aufgabe P3

add_exercise('Aufgabe P3:', color="black", align="left", fontsize=20) 

add_equation_in_latex("S = \left\{\left(x,y,z\\right) \in \R^{3} \ \\big \\vert \ 4x^{2}+y^{2} \leq 4, \ z = 4-4x^{2}-y^{2} \\right\}")

_, col_b_4_p_3, _ = create_columns(3)

button_b_4_p_3 = create_checkbox(method="to_column", col=col_b_4_p_3, name="3D Graphik zeigen", key="4p3")

if button_b_4_p_3:
    add_plot(blatt_04_P_03())

### Aufgabe H1

add_exercise('Aufgabe H1:', color="black", align="left", fontsize=20) 

add_equation_in_latex("V \subset \R^{3} \\text{ berandet durch die Flächen } x=1 \\text{ und } x=-1 \\text{ sowie } z=0 \\text{ und } z=2-2y^{2}")

_, col_b_4_h_1, _ = create_columns(3)

button_b_4_h_1 = create_checkbox(method="to_column", col=col_b_4_h_1, name="3D Graphik zeigen", key="4h1")

if button_b_4_h_1:
    add_plot(blatt_04_H_01())

add_seperation_line()

### Blatt 5 ###

add_sheet(title="Blatt 5: Rechnen wie die Fourien", color="green", align="center", fontsize=30)

### Aufgabe P2

add_exercise('Aufgabe P2:', color="black", align="left", fontsize=20) 

add_equation_in_latex("V \subset \R^{3} \\text{ berandet durch die Flächen } x=1 \\text{ und } x=-1 \\text{ sowie } z=0 \\text{ und } z=2-2y^{2}")

_, col_b_5_p_2, _ = create_columns(3)

button_b_5_p_2 = create_checkbox(method="to_column", col=col_b_5_p_2, name="Graphik zeigen", key="5p2")

if button_b_5_p_2:
    n = add_slider(label="Wählen Sie n", min_value=1, max_value=100, step=1, value=10)

    add_matplotlib_plot(blatt_05_P_02(n))

add_seperation_line()

### Aufgabe P3

add_exercise('Aufgabe P3:', color="black", align="left", fontsize=20) 

add_equation_in_latex("V \subset \R^{3} \\text{ berandet durch die Flächen } x=1 \\text{ und } x=-1 \\text{ sowie } z=0 \\text{ und } z=2-2y^{2}")

_, col_b_5_p_3, _ = create_columns(3)

button_b_5_p_3 = create_checkbox(method="to_column", col=col_b_5_p_3, name="Graphik zeigen", key="5p3")

if button_b_5_p_3:
    n = add_slider(label="Wählen Sie n", min_value=1, max_value=100, step=1, value=10)

    add_matplotlib_plot(blatt_05_P_03(n))

add_seperation_line()







