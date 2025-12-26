# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 19:47:31 2025

@author: martp
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Interactive Cottrell Simulator")

# User inputs
n = st.number_input("Electrons transferred (n)", value=1)
A = st.number_input("Electrode area (cm²)", value=0.0707)
c0 = st.number_input("Concentration (mol/cm³)", value=1e-6, format="%.6e")
D = st.number_input("Diffusion coefficient (cm²/s)", value=7e-6, format="%.6e")
t_end = st.slider("Simulation time (s)", 1, 60, 30)

F = 96485
k = (n * F * A * c0 * np.sqrt(D)) / np.sqrt(np.pi)

t = np.linspace(0.001, t_end, 2000)
i = k / np.sqrt(t)
Q = np.cumsum(i * np.diff(np.hstack(([0], t))))

fig, ax1 = plt.subplots()
ax1.plot(t, i, color='tab:blue')
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Current (A)", color='tab:blue')

ax2 = ax1.twinx()
ax2.plot(t, Q, color='tab:red')
ax2.set_ylabel("Charge (C)", color='tab:red')

st.pyplot(fig)