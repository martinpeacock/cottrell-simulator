# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 10:54:49 2025

@author: martp
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

# -----------------------------
# ZP Branding: Logo + Title
# -----------------------------
logo = Image.open("zp_logo.png")
st.image(logo, width=150)

st.title("Interactive Electrochemistry Simulator")
st.markdown("<p style='color: #009639; font-weight: bold;'>Version 1.3.0</p>", unsafe_allow_html=True)

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Simulation Controls")

# Electrode area in mm² (user-facing)
A_mm2 = st.sidebar.slider("Electrode area (mm²)", 0.50, 5.00, 1.96, 0.01)
A = A_mm2 * 0.01  # convert mm² → cm²

n = st.sidebar.number_input("Electrons transferred (n)", value=1)

# Concentration in mM (user-facing)
c0_mM = st.sidebar.number_input("Concentration (mM)", value=1.0)
c0 = c0_mM * 1e-6  # convert mM → mol/cm³

D = st.sidebar.number_input("Diffusion coefficient (cm²/s)", value=7e-6, format="%.6e")
t_end = st.sidebar.slider("Simulation time (s)", 1, 60, 30)

t_pause = st.sidebar.slider("Skip first X seconds", 0.0, 5.0, 0.0, 0.1)

# -----------------------------
# Tabs for simulations
# -----------------------------
tab1, tab2, tab3 = st.tabs(["Cottrell", "Future Simulation 1", "Future Simulation 2"])

# -----------------------------
# TAB 1: Cottrell Simulation
# -----------------------------
with tab1:

    st.subheader("Cottrell Chronoamperometry Simulation")

    # Cottrell Calculation
    F = 96485
    k = (n * F * A * c0 * np.sqrt(D)) / np.sqrt(np.pi)

    t = np.linspace(0.001, t_end, 2000)
    i = k / np.sqrt(t)
    Q = np.cumsum(i * np.diff(np.hstack(([0], t))))

    mask = t >= t_pause
    t_plot = t[mask]
    i_plot = i[mask]
    Q_plot = Q[mask]

    # Plotting
    fig, ax1 = plt.subplots()

    ax1.plot(t_plot, i_plot, color='tab:blue')
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Current (A)", color='tab:blue')

    ax2 = ax1.twinx()
    ax2.plot(t_plot, Q_plot, color='tab:red')
    ax2.set_ylabel("Charge (C)", color='tab:red')

    ax1.relim()
    ax1.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()

    st.pyplot(fig)

    # -----------------------------
    # Downloadable Plot
    # -----------------------------
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300)
    st.download_button(
        label="Download Plot (PNG)",
        data=buf.getvalue(),
        file_name="cottrell_plot.png",
        mime="image/png"
    )

# -----------------------------
# TAB 2: Placeholder
# -----------------------------
with tab2:
    st.subheader("Future Simulation 1")
    st.info("This tab is reserved for your next electrochemical model.")

# -----------------------------
# TAB 3: Placeholder
# -----------------------------
with tab3:
    st.subheader("Future Simulation 2")
    st.info("This tab will host another simulation in the future.")

# -----------------------------
# ZP Footer (Green)
# -----------------------------
st.markdown(
    """
    <hr>
    <div style='text-align: center; font-size: 14px; color: #009639;'>
        <p>
            <a href='https://www.zimmerpeacock.com/contact/' target='_blank' 
               style='color: #009639; text-decoration: none;'>
                Contact Zimmer & Peacock
            </a>
        </p>
        <p>© 2026 Zimmer & Peacock</p>
    </div>
    """,
    unsafe_allow_html=True
)