import streamlit as st
from collections import defaultdict


def add_title(title, color="blue", align="center", fontsize=40):
    return st.markdown(f"<h1 style='text-align: {align}; "f"color: {color}; font-size: {fontsize}px;'>{title}</h1>",
                       unsafe_allow_html=True)


def add_subtitle(title, color="red", align="center", fontsize=25):
    return st.markdown(f"<h1 style='text-align: {align}; color: {color}; font-size: {fontsize}px;'>{title}</h1>",
                       unsafe_allow_html=True)


def add_sheet(title, color="green", align="center", fontsize=30):
    return st.markdown(f"<h1 style='text-align: {align}; color: {color}; font-size: {fontsize}px;'> {title} </h1>",
                       unsafe_allow_html=True)


def add_exercise(title, color="black", align="left", fontsize=20):
    return st.markdown(f"<h1 style='text-align: {align}; color: {color}; font-size: {fontsize}px;'> {title} </h1>",
                       unsafe_allow_html=True)


def add_comment(comment):
    return st.markdown(f"{comment}")


def add_info(info):
    return st.info(f"{info}")


def add_equation_in_latex(equation):
    return st.latex(f"{equation}") 


def create_columns(num_columns):
    columns_tuple = st.columns(num_columns)
    return columns_tuple


def create_button(name, key, method=None, col=None):
    button_dict = defaultdict(lambda: st.button(name, key=key))
    button_dict["to_column"] = col.button(name, key=key)
    return button_dict[method]


def create_checkbox(name, key, method=None, col=None):
    button_dict = defaultdict(lambda: st.checkbox(name, key=key))
    button_dict["to_column"] = col.checkbox(name, key=key)
    return button_dict[method]


def add_slider(label, min_value, max_value, step, value, key):
    return st.slider(label=label, min_value=min_value, max_value=max_value, step=step, value=value, key=key)


def add_number_input(label, key):
    return st.number_input(label=label, key=key)


def add_seperation_line():
    return st.write('---')
