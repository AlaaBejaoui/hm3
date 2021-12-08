import datetime

from plots import *
from utilities import *


def add_blatt_2():
    add_sheet(title="Blatt 2: Fubinisierst du noch oder transformierst du schon?")

    # Aufgabe P1
    add_exercise(title="Aufgabe P1:")
    add_equation_in_latex(
        "V = \left\{\left(x,y,z\\right) \in \R^{3} \ \\bigg \\vert \ x^{2}+y^{2}+z^{2} \leq 4, \ 1 \leq z"
        "\leq \\frac{3}{2}, \ x \geq 0, \ x \geq y \\right\}")
    _, col_b_2_p_1, _ = create_columns(3)
    button_b_2_p_1 = create_checkbox(method="to_column", col=col_b_2_p_1, name="3D Grafik zeigen", key="2p1")
    if button_b_2_p_1:
        add_plot(blatt_02_P_01())

    # Aufgabe H1
    add_exercise("Aufgabe H1:")
    add_equation_in_latex(
        "E=\left\{\left(x, y, z\\right) \in \R^{3} \ \\bigg \\vert \ \\frac{x^{2}}{9}+\\frac{y^{2}}{9}+"
        "\\frac{z^{2}}{4} \leq 1, \ x \leq 0, \ z \geq 0 \\right\}")
    _, col_b_2_h_1, _ = create_columns(3)
    button_b_2_h_1 = create_checkbox(method="to_column", col=col_b_2_h_1, name="3D Grafik zeigen", key="2h1")
    if button_b_2_h_1:
        add_plot(blatt_02_H_01())


def add_blatt_4():
    add_sheet(title="Blatt 4: Durchs wilde KuR3distan")

    # Aufgabe P2
    add_exercise("Aufgabe P2:")
    add_equation_in_latex(
        "V = \left\{\left(x,y,z\\right) \in \R^{3} \ \\big \\vert \ x^{2}+y^{2} \leq 1, \ 0 \leq z \leq "
        "1+xy \\right\} \\newline f: \R^{3} \\rightarrow \R^{3}:(x, y, z) \mapsto \left(0,0, z^{2} \\right)")
    _, col_b_4_p_2, _ = create_columns(3)
    button_b_4_p_2 = create_checkbox(method="to_column", col=col_b_4_p_2, name="3D Grafik zeigen", key="4p2")
    if button_b_4_p_2:
        add_plot(blatt_04_P_02())

    # Aufgabe P3
    add_exercise("Aufgabe P3:")
    add_equation_in_latex(
        "S = \left\{\left(x,y,z\\right) \in \R^{3} \ \\big \\vert \ 4x^{2}+y^{2} \leq 4, \ z = 4-4x^{2}-y^{2} "
        "\\right\} \\newline f: \R^{3} \\rightarrow \R^{3}:(x, y, z) \mapsto \left(y-z, 2x+z, xy \\right)")
    _, col_b_4_p_3, _ = create_columns(3)
    button_b_4_p_3 = create_checkbox(method="to_column", col=col_b_4_p_3, name="3D Grafik zeigen", key="4p3")
    if button_b_4_p_3:
        add_plot(blatt_04_P_03())

    # Aufgabe H1
    add_exercise("Aufgabe H1:")
    add_equation_in_latex(
        "V \subset \R^{3} \\text{ berandet durch die Flächen } x=1 \\text{ und } x=-1 \\text{ sowie } z=0 "
        "\\text{ und } z=2-2y^{2} \\newline f: \R^{3} \\rightarrow \R^{3}:(x, y, z) \mapsto \left(x(y+z),-2yz, z (x+y+z)\\right)")
    _, col_b_4_h_1, _ = create_columns(3)
    button_b_4_h_1 = create_checkbox(method="to_column", col=col_b_4_h_1, name="3D Grafik zeigen", key="4h1")
    if button_b_4_h_1:
        add_plot(blatt_04_H_01())


def add_blatt_5():
    add_sheet(title="Blatt 5: Rechnen wie die Fourien")

    # Aufgabe P2
    add_exercise("Aufgabe P2:")
    add_equation_in_latex(
        "f: \R \\rightarrow \R \ 2\pi \\text{-periodisch, mit } \\newline f(x) = 0  \\text {, falls } "
        "-\pi<x<0 \\text{ und } \mathrm{e}^{-x}  \\text {, falls } 0 \leq x \leq \pi")
    _, col_b_5_p_2, _ = create_columns(3)
    button_b_5_p_2 = create_checkbox(method="to_column", col=col_b_5_p_2, name="Grafik zeigen", key="5p2")
    if button_b_5_p_2:
        n = add_slider(label="Bitte n auswählen", min_value=0, max_value=50, step=1, value=10, key="5p2")
        add_plot(blatt_05_P_02(n))

    # Aufgabe P3
    add_exercise("Aufgabe P3:")
    add_equation_in_latex(
        "f: \R \\rightarrow \R \ \\text{ gerade und }  2\pi \\text{-periodisch, mit } \\newline f(x) = "
        "\pi - x  \\text {, für }  0 \leq x \leq \pi")
    _, col_b_5_p_3, _ = create_columns(3)
    button_b_5_p_3 = create_checkbox(method="to_column", col=col_b_5_p_3, name="Grafik zeigen", key="5p3")
    if button_b_5_p_3:
        n = add_slider(label="Bitte n auswählen", min_value=0, max_value=50, step=1, value=10, key="5p3")
        add_plot(blatt_05_P_03(n))

    # Aufgabe H1 Teil 1
    add_exercise("Aufgabe H1:")
    add_equation_in_latex("f: \R \\rightarrow \R \ \\text{ gerade und }  P \\text{-periodisch, mit } \\newline f(x) = "
                          "\\frac{2}{L} \ x  \\text {, falls } 0 \leq x< \\frac{L}{2} \\text{ und } \\frac{2}{L} \left( L-x "
                          "\\right)  \\text {, falls } \\frac{L}{2} \leq x \leq L")
    _, col_b_5_h_1_1, _ = create_columns(3)
    button_b_5_h_1_1 = create_checkbox(method="to_column", col=col_b_5_h_1_1, name="Grafik zeigen", key="5h11")
    if button_b_5_h_1_1:
        if datetime.datetime.now() >= datetime.datetime(2021, 11, 30, 18, 00):
            n = add_slider(label="Bitte n auswählen", min_value=0, max_value=50, step=1, value=10, key="5h11")
            add_plot(blatt_05_H_01_1(n))
        else:
            add_info(f"Grafik wird am {datetime.datetime(2021, 11, 30, 18, 00).date().strftime(format='%d.%m.%y')}"
                     f" um {datetime.datetime(2021, 11, 30, 18, 00).time().strftime(format='%H:%M')} freigeschaltet!")

    # Aufgabe H1 Teil 2
    add_equation_in_latex(
        "g: \R \\rightarrow \R \ \\text{ ungerade und }  P \\text{-periodisch, mit } \\newline g(x) = "
        "\\frac{2}{L} \ x  \\text {, falls } 0 \leq x< \\frac{L}{2} \\text{ und } \\frac{2}{L} \left( L-x "
        "\\right)  \\text {, falls } \\frac{L}{2} \leq x \leq L")
    _, col_b_5_h_1_2, _ = create_columns(3)
    button_b_5_h_1_2 = create_checkbox(method="to_column", col=col_b_5_h_1_2, name="Grafik zeigen", key="5h12")
    if button_b_5_h_1_2:
        if datetime.datetime.now() >= datetime.datetime(2021, 11, 30, 18, 00):
            n = add_slider(label="Bitte n auswählen", min_value=0, max_value=50, step=1, value=10, key="5h12")
            add_plot(blatt_05_H_01_2(n))
        else:
            add_info(f"Grafik wird am {datetime.datetime(2021, 11, 30, 18, 00).date().strftime(format='%d.%m.%y')}"
                     f" um {datetime.datetime(2021, 11, 30, 18, 00).time().strftime(format='%H:%M')} freigeschaltet!")


def add_blatt_6():
    add_sheet(title="Blatt 6: Fast and Fourier")

    # Aufgabe P1
    add_exercise("Aufgabe P1:")
    add_equation_in_latex("f(x) = \cos^2(x)")
    _, col_b_6_p_1, _ = create_columns(3)
    button_b_6_p_1 = create_checkbox(method="to_column", col=col_b_6_p_1, name="Grafik zeigen", key="6p1")
    if button_b_6_p_1:
        n = add_slider(label="Bitte n auswählen", min_value=0, max_value=10, step=1, value=2, key="6p1")
        add_plot(blatt_06_P_01(n))

    # Aufgabe H2
    add_exercise("Aufgabe H2:")
    add_equation_in_latex("f(x) = \sin^4(x)")
    _, col_b_6_h_2, _ = create_columns(3)
    button_b_6_h_2 = create_checkbox(method="to_column", col=col_b_6_h_2, name="Grafik zeigen", key="6h2")
    if button_b_6_h_2:
        if datetime.datetime.now() >= datetime.datetime(2021, 12, 7, 18, 00):
            n = add_slider(label="Bitte n auswählen", min_value=1, max_value=10, step=1, value=3, key="6h2")
            add_plot(blatt_06_H_02(n))
        else:
            add_info(f"Grafik wird am {datetime.datetime(2021, 12, 7, 18, 00).date().strftime(format='%d.%m.%y')}"
                     f" um {datetime.datetime(2021, 12, 7, 18, 00).time().strftime(format='%H:%M')} freigeschaltet!")


def add_blatt_7():
    add_sheet(title="Blatt 7: ODE an Laplace")

    # Aufgabe P2
    add_exercise("Aufgabe P2:")
    add_equation_in_latex("yy^{\prime} + 2*\sin(x) = 0")
    _, col_b_7_p_2_1, _ = create_columns(3)
    button_b_7_p_2_1 = create_checkbox(method="to_column", col=col_b_7_p_2_1, name="Grafik zeigen", key="7p21")
    if button_b_7_p_2_1:
        y_0 = add_number_input(label="Bitte y(0) eingeben", key="7p21")
        add_plot(blatt_07_P_02(y_0))


if __name__ == '__main__':
    # Title and subtitle
    add_title(title="HM3 - interaktive Graphiken")
    add_subtitle(title="Alaa Bejaoui & Maha Badri")

    # Blatt 2
    add_blatt_2()
    add_seperation_line()

    # Blatt 4
    add_blatt_4()
    add_seperation_line()

    # Blatt 5
    add_blatt_5()
    add_seperation_line()

    # Blatt 6
    add_blatt_6()
    add_seperation_line()

    # Blatt 7
    # add_blatt_7()
    # add_seperation_line()
