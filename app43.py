import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.special import erfc

st.set_page_config(page_title="Contaminant Concentration Dynamics", layout="centered")

st.title("📉 Contaminant Concentration Dynamics in Subsurface Layers")

st.markdown("""
This interactive tool simulates how contaminant concentration changes over time and depth 
in gravel layers using a simplified analytical solution.
""")

C0 = st.slider("Initial Concentration C₀ (mg/L)", 10, 200, 100)
D = st.slider("Dispersion Coefficient D (cm²/day)", 1, 100, 10)
z_values = st.multiselect("Select Depths z (cm)", [10, 30, 50, 70, 90], default=[10, 50, 90])
t_max = st.slider("Simulation Time (days)", 10, 200, 100)

t = np.linspace(1, t_max, 200)

fig, ax = plt.subplots()
for z in z_values:
    C_t = C0 * erfc(z / (2 * np.sqrt(D * t)))
    ax.plot(t, C_t, label=f"Depth {z} cm")

ax.set_title("Contaminant Concentration vs. Time")
ax.set_xlabel("Time (days)")
ax.set_ylabel("Concentration (mg/L)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.markdown("""
**Equation Used:**

\\[
C(z, t) = C_0 \\cdot \\text{erfc} \\left( \\frac{z}{2\\sqrt{D t}} \\right)
\\]

Where:
- \(C_0\) = Initial contaminant concentration
- \(D\) = Dispersion coefficient
- \(z\) = Depth
- \(t\) = Time
- \(\text{erfc}\) = Complementary error function
""")
