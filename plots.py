import streamlit as st
import plotly.graph_objects as go
import numpy as np
# import matplotlib.pyplot as plt

def blatt_02_P_01():
        
        r_top = np.linspace(0, np.sqrt(7)/2, 100)
        r_bottom = np.linspace(0, np.sqrt(3), 100)
        phi = np.linspace(-np.pi/2, np.pi/4, 100)
        z = np.linspace(1 , 3/2, 100)

        r_top_matrix, phi_matrix = np.meshgrid(r_top, phi)
        r_bottom_matrix, phi_matrix = np.meshgrid(r_bottom, phi)

        x_top = r_top_matrix * np.cos(phi_matrix)
        y_top = r_top_matrix * np.sin(phi_matrix)
        z_top = (3/2)*np.ones_like(x_top)

        x_bottom = r_bottom_matrix * np.cos(phi_matrix)
        y_bottom = r_bottom_matrix * np.sin(phi_matrix)
        z_bottom = np.ones_like(x_bottom)

        y1 = np.linspace(-2, 0, 100)
        y2 = np.linspace(0, 2, 100)

        z_m, phi_m = np.meshgrid(z, phi)
        r_m1 = np.sqrt(4-z_m**2)
        r_m2 = np.zeros_like(z_m)
        x_m1 = r_m1 * np.cos(phi_m)
        y_m1 = r_m1 * np.sin(phi_m)
        x_m2 = r_m2 * np.cos(phi_m)
        y_m2 = r_m2 * np.sin(phi_m)

        y_m3, z_m3 = np.meshgrid(y1, z)
        x_m3 = np.zeros_like(y_m3)

        for i in range(100):
          for j in range(100):
            if y_m3[j,i] < -np.sqrt(4-z_m3[j,i]**2):
              y_m3[j,i] = -np.sqrt(4-z_m3[j,i]**2)

        y_m4, z_m4 = np.meshgrid(y2, z)
        for i in range(100):
          for j in range(100):
            if y_m4[j,i] > np.sqrt((4-z_m4[j,i]**2)/2):
              y_m4[j,i] = np.sqrt((4-z_m4[j,i]**2)/2)
        x_m4 = y_m4

        phi_k = np.linspace(0, 2*np.pi, 100)
        theta_k = np.linspace(0, np.pi, 100)

        phi_k_matrix, theta_k_matrix = np.meshgrid(phi_k, theta_k)
        x_k = 2*np.sin(theta_k_matrix)*np.cos(phi_k_matrix)
        y_k = 2*np.sin(theta_k_matrix)*np.sin(phi_k_matrix)
        z_k = 2*np.cos(theta_k_matrix)

        min_value = np.r_[z_k,z_top,z_bottom, z_m, z_m3, z_m4].min()
        max_value = np.r_[z_k,z_top,z_bottom, z_m, z_m3, z_m4].max()

        fig = go.Figure(data=[
          go.Surface(x=x_k, y=y_k, z=z_k, showscale=False, opacity=0.3, cmin=min_value, cmax=max_value),
          go.Surface(x=x_top, y=y_top, z=z_top, showscale=False, cmin=min_value, cmax=max_value),
          go.Surface(x=x_bottom, y=y_bottom, z=z_bottom, showscale=False, cmin=min_value, cmax=max_value),
          go.Surface(x=x_m1, y=y_m1, z=z_m, showscale=False, cmin=min_value, cmax=max_value),
          go.Surface(x=x_m2, y=y_m2, z=z_m, showscale=False, cmin=min_value, cmax=max_value),
          go.Surface(x=x_m3, y=y_m3, z=z_m3, showscale=False, cmin=min_value, cmax=max_value),
          go.Surface(x=x_m4, y=y_m4, z=z_m4, showscale=False, cmin=min_value, cmax=max_value),
          ])

        fig.update_layout(autosize=False,
                          width=500, height=500,
                          margin=dict(l=65, r=50, b=65, t=90),
                          hovermode=False)

        return fig

def blatt_02_H_01():
        
        phi = np.linspace(0, 2*np.pi, 100)
        theta = np.linspace(0, np.pi, 100)

        phi_matrix, theta_matrix = np.meshgrid(phi, theta)

        x_e = 3*np.sin(theta_matrix)*np.cos(phi_matrix)
        y_e = 3*np.sin(theta_matrix)*np.sin(phi_matrix)
        z_e = 2*np.cos(theta_matrix)

        phi_m = np.linspace(np.pi/2, 3*np.pi/2, 100)
        theta_m = np.linspace(0, np.pi/2, 100)

        phi_m_matrix, theta_m_matrix = np.meshgrid(phi_m, theta_m)

        x_m1 = 3*np.sin(theta_m_matrix)*np.cos(phi_m_matrix)
        y_m1 = 3*np.sin(theta_m_matrix)*np.sin(phi_m_matrix)
        z_m1 = 2*np.cos(theta_m_matrix)

        y = np.linspace(-3, 3, 100)
        z = np.linspace(0, 2, 100)

        y_m2, z_m2 = np.meshgrid(y, z)
        x_m2 = np.zeros_like(y_m2)

        for i in range(100):
          for j in range(100):
            if z_m2[j,i] > np.sqrt(4-(4/9)*y_m2[j,i]**2):
              z_m2[j,i] = np.sqrt(4-(4/9)*y_m2[j,i]**2)

        x = np.linspace(-3, 0, 100)
        x_b, y_b = np.meshgrid(x, y)
        z_b = np.zeros_like(x_b)

        for i in range(100):
          for j in range(100):
            if x_b[j,i] < -np.sqrt(9-y_b[j,i]**2):
              x_b[j,i] = -np.sqrt(9-y_b[j,i]**2)

        min_value = np.r_[z_e,z_m1,z_m2, z_b].min()
        max_value = np.r_[z_e,z_m1,z_m2, z_b].max()

        fig = go.Figure(data=[
          go.Surface(x=x_e, y=y_e, z=z_e, showscale=False, opacity=0.3, cmin=min_value, cmax=max_value),
          go.Surface(x=x_m1, y=y_m1, z=z_m1, showscale=False, cmin=min_value, cmax=max_value),
          go.Surface(x=x_m2, y=y_m2, z=z_m2, showscale=False, cmin=min_value, cmax=max_value),
          go.Surface(x=x_b, y=y_b, z=z_b, showscale=False, cmin=min_value, cmax=max_value)
        ])

        fig.update_layout(autosize=False,
                          width=500, height=500,
                          margin=dict(l=65, r=50, b=65, t=90),
                          hovermode=False)

        return fig

def blatt_04_P_02():
        r = np.linspace(0, 1, 100)
        phi = np.linspace(0, 2*np.pi, 100)

        radius_matrix, phi_matrix = np.meshgrid(r, phi)

        x = radius_matrix * np.cos(phi_matrix)
        y = radius_matrix * np.sin(phi_matrix)

        z_bottom = 0*x + 0*y
        z_top = 1 + x*y

        z = np.linspace(0, 2, 100)

        phi_m, z_m = np.meshgrid(phi, z)

        for i in range(100):
                for j in range(100):
                        if z_m[j,i] > 1+np.cos(phi_m[j,i])*np.sin(phi_m[j,i]):
                                z_m[j,i] = 1+np.cos(phi_m[j,i])*np.sin(phi_m[j,i])

        x_m = np.cos(phi_m)     
        y_m = np.sin(phi_m)
        x_v, y_v, z_v = np.meshgrid(np.linspace(-1, 1, 5),
                            np.linspace(-1, 1, 5),
                            np.linspace(0, 2, 5))
        x_v = x_v.reshape(-1)
        y_v = y_v.reshape(-1)
        z_v = z_v.reshape(-1)

        u_v, v_v = np.zeros_like(x_v), np.zeros_like(y_v)
        w_v = z_v**2

        min_value = np.r_[z_bottom,z_top,z_m].min()
        max_value = np.r_[z_bottom,z_top,z_m].max()

        fig = go.FigureWidget(data=[
            go.Surface(x=x, y=y, z=z_bottom, showscale=False, cmin=min_value, cmax=max_value),
            go.Surface(x=x, y=y, z=z_top, showscale=False, cmin=min_value, cmax=max_value),
            go.Surface(x=x_m, y=y_m, z=z_m, showscale=False, cmin=min_value, cmax=max_value),
            go.Cone(
                x=list(x_v),
                y=list(y_v),
                z=list(z_v),
                u=list(u_v),
                v=list(v_v),
                w=list(w_v), showscale=False, cmin=min_value, cmax=max_value)
        ])

        fig.update_layout(autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90), 
                  hovermode=False)
        return fig 

def blatt_04_P_03():
        r = np.linspace(0, 1, 100)
        phi = np.linspace(0, 2*np.pi, 100)

        radius_matrix, phi_matrix = np.meshgrid(r, phi)

        x = radius_matrix * np.cos(phi_matrix)
        y = 2* radius_matrix * np.sin(phi_matrix)
        z = 4-4*radius_matrix**2

        x_v, y_v, z_v = np.meshgrid(np.linspace(-1, 1, 5),
                            np.linspace(-2, 2, 5),
                            np.linspace(0, 4, 5))
        x_v = x_v.reshape(-1)
        y_v = y_v.reshape(-1)
        z_v = z_v.reshape(-1)

        u_v = y_v - z_v
        v_v = 2*x_v + z_v
        w_v = x_v*y_v

        min_value = np.r_[z].min()
        max_value = np.r_[z].max()

        fig = go.Figure(data=[
        go.Surface(x=x, y=y, z=z, showscale=False, cmin=min_value, cmax=max_value),
            go.Cone(
                x=list(x_v),
                y=list(y_v),
                z=list(z_v),
                u=list(u_v),
                v=list(v_v),
                w=list(w_v),
                showscale=False,
            cmin=min_value, cmax=max_value)
        ])

        fig.update_layout(autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90),
                  hovermode=False)
        return fig

def blatt_04_H_01():

        x = np.linspace(-1, 1, 100)
        y = np.linspace(-1, 1, 100)

        x_matrix, y_matrix = np.meshgrid(x, y)
        z_bottom = np.zeros_like(x_matrix)
        z_top = 2 - 2*y_matrix**2

        z = np.linspace(0, 2, 100)

        y_m, z_m = np.meshgrid(y, z)

        for i in range(100):
                for j in range(100):
                        if z_m[j,i] > 2-2*y_m[j,i]**2:
                                z_m[j,i] = 2-2*y_m[j,i]**2

        x_m = np.ones_like(y_m)

        x_v, y_v, z_v = np.meshgrid(np.linspace(-1, 1, 5),
                            np.linspace(-1, 1, 5),
                            np.linspace(0, 2, 5))
        x_v = x_v.reshape(-1)
        y_v = y_v.reshape(-1)
        z_v = z_v.reshape(-1)

        u_v = x_v*(y_v + z_v)
        v_v = -2*y_v*z_v
        w_v = z_v*(x_v+y_v+z_v)

        min_value = np.r_[z_bottom,z_top,z_m].min()
        max_value = np.r_[z_bottom,z_top,z_m].max()

        fig = go.Figure(data=[
        go.Surface(x=x_matrix, y=y_matrix, z=z_top, showscale=False, cmin=min_value, cmax=max_value),
        go.Surface(x=x_matrix, y=y_matrix, z=z_bottom, showscale=False, cmin=min_value, cmax=max_value),
        go.Surface(x=x_m, y=y_m, z=z_m, showscale=False, cmin=min_value, cmax=max_value),
        go.Surface(x=-x_m, y=y_m, z=z_m, showscale=False, cmin=min_value, cmax=max_value),
            go.Cone(
                x=list(x_v),
                y=list(y_v),
                z=list(z_v),
                u=list(u_v),
                v=list(v_v),
                w=list(w_v),
                showscale=False, cmin=min_value, cmax=max_value)
        ])

        fig.update_layout(autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90),
                  hovermode=False)
        return fig

def blatt_05_P_02(n):
    
        x_ = np.linspace(-np.pi, np.pi, 300)
        y_ = 0 * (x_<0) + np.exp(-x_) * (x_>0)

        x = np.linspace(-3*np.pi, 3*np.pi, 3*300)
        f = np.array([y_ for _ in range(3)]).reshape(-1)

        a_0 = (1/np.pi) * (1-np.exp(-np.pi))
        a_k = lambda k: (1/(np.pi*(1+k**2))) * (1-((-1)**k)*np.exp(-np.pi))
        b_k = lambda k: (k/(np.pi*(1+k**2))) * (1-((-1)**k)*np.exp(-np.pi)) 

        f_tilde = np.zeros_like(x)
        for i in range(1, n):
          a_i = a_k(i)
          b_i = b_k(i)
          f_tilde += (a_i*np.cos(i*x) + b_i*np.sin(i*x))
        f_tilde += (a_0/2)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=f, name="f(x)", line_shape='linear'))
        fig.add_trace(go.Scatter(x=x, y=f_tilde, name= r"F(f)(x)", line_shape='linear')) 
        fig.update_layout(title={'text': f"n = {n}",
                                 'y': 0.9,
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                          xaxis_title="x",
                          yaxis_title="y")


        
        # fig = plt.figure(figsize=(4, 2))
        # plt.plot(x, f, label="f(x)")
        # plt.plot(x, f_tilde, label="Fourier Reihe")
        # plt.legend(loc="upper right")
        
        return fig

def blatt_05_P_03(n):

        x_ = np.linspace(-np.pi, np.pi, 300)
        y_ = (np.pi+x_) * (x_<0) + (np.pi-x_) * (x_>0)

        x = np.linspace(-3*np.pi, 3*np.pi, 3*300)
        f = np.array([y_ for _ in range(3)]).reshape(-1)

        a_0 = np.pi
        a_k = lambda k: (2/(np.pi*(k**2))) * (1-(-1)**k)
        b_k = lambda k: 0 

        
        f_tilde = np.zeros_like(x)
        for i in range(1, n):
                a_i = a_k(i)
                b_i = b_k(i)
                f_tilde += (a_i*np.cos(i*x) + b_i*np.sin(i*x))
        
        f_tilde += (a_0/2)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=f, name="f(x)", line_shape='linear'))
        fig.add_trace(go.Scatter(x=x, y=f_tilde, name=" F(f)(x)", line_shape='linear'))
        fig.update_layout(title={'text': f"n = {n}",
                                 'y': 0.9,
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                          xaxis_title="x",
                          yaxis_title="y")


        # fig = plt.figure(figsize=(4, 2))
        # plt.plot(x, f, label="f(x)")
        # plt.plot(x, f_tilde, label="Fourier Reihe")
        # plt.legend(loc="upper right")
        
        return fig


def blatt_05_H_01_1(n):
    x_ = np.linspace(0, 2, 300)
    y_ = (2*x_) * np.logical_and((x_ >= 0), (x_ <= 1/2)) + (2*(1-x_)) * np.logical_and((x_ >= 1/2), (x_<= 1)) \
         + (-2 + 2*x_) * np.logical_and((x_ >= 1), (x_<= 3/2)) + (4-2*x_) * np.logical_and((x_ >= 3/2), (x_<= 2))

    x = np.linspace(-4, 4, 4 * 300)
    f = np.array([y_ for _ in range(4)]).reshape(-1)

    a_0 = 1
    a_k = lambda k: (4 / ((np.pi**2) * (k ** 2))) * ((2*np.cos((k*np.pi)/2)) - np.cos(k*np.pi) -1)
    b_k = lambda k: 0

    f_tilde = np.zeros_like(x)
    for i in range(1, n):
        a_i = a_k(i)
        b_i = b_k(i)
        f_tilde += (a_i * np.cos(i*np.pi * x) + b_i * np.sin(i*np.pi* x))

    f_tilde += (a_0 / 2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=f, name="f(x)", line_shape='linear'))
    fig.add_trace(go.Scatter(x=x, y=f_tilde, name=" F(f)(x)", line_shape='linear'))
    fig.update_layout(title={'text': f"L = 1, P = 2, n = {n}",
                             'y': 0.9,
                             'x': 0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'},
                      xaxis_title="x",
                      yaxis_title="y")


    # fig = plt.figure(figsize=(4, 2))
    # plt.plot(x, f, label="f(x)")
    # plt.plot(x, f_tilde, label="Fourier Reihe")
    # plt.legend(loc="upper right")

    return fig

def blatt_05_H_01_2(n):
    x_ = np.linspace(0, 2, 300)
    y_ = (2*x_) * np.logical_and((x_ >= 0), (x_ <= 1/2)) + (2*(1-x_)) * np.logical_and((x_ >= 1/2), (x_<= 1)) \
         + (2 - 2*x_) * np.logical_and((x_ >= 1), (x_<= 3/2)) + (-4+2*x_) * np.logical_and((x_ >= 3/2), (x_<= 2))

    x = np.linspace(-4, 4, 4 * 300)
    f = np.array([y_ for _ in range(4)]).reshape(-1)

    a_0 = 0
    a_k = lambda k: 0
    b_k = lambda k: (-4 / ((np.pi**2) * (k ** 2))) * (np.sin((3*k*np.pi)/2)-np.sin((k*np.pi)/2))

    f_tilde = np.zeros_like(x)
    for i in range(1, n):
        a_i = a_k(i)
        b_i = b_k(i)
        f_tilde += (a_i * np.cos(i*np.pi * x) + b_i * np.sin(i*np.pi* x))

    f_tilde += (a_0 / 2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=f, name="g(x)", line_shape='linear'))
    fig.add_trace(go.Scatter(x=x, y=f_tilde, name=" F(g)(x)", line_shape='linear'))
    fig.update_layout(title={'text': f"L = 1, P = 2, n = {n}",
                             'y': 0.9,
                             'x': 0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'},
                      xaxis_title="x",
                      yaxis_title="y")


    # fig = plt.figure(figsize=(4, 2))
    # plt.plot(x, f, label="f(x)")
    # plt.plot(x, f_tilde, label="Fourier Reihe")
    # plt.legend(loc="upper right")

    return fig

def add_plot(plot_ref):
        return st.plotly_chart(plot_ref, use_container_width=True)

def add_matplotlib_plot(plot_ref):
        return st.pyplot(plot_ref, use_container_width=True)