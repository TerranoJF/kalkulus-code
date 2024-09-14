import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk plot grafik tunggal
def plot_single_graph(x, y, x_label, y_label, title, xlim=None, ylim=None, color='b'):
    plt.figure(figsize=(6,6))
    plt.plot(x, y, 'o-', color=color, linewidth=2, markersize=8)
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    plt.axhline(0, color='black', linewidth=2)
    plt.axvline(0, color='black', linewidth=2)
    plt.grid(True)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    st.pyplot(plt)

# Fungsi untuk plot grafik dengan beberapa set data
def plot_combined_graph(data_sets, x_label, y_label, title, xlim=None, ylim=None):
    plt.figure(figsize=(6,6))
    
    # Plot setiap set data dengan warna berbeda
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, (x, y, label) in enumerate(data_sets):
        plt.plot(x, y, 'o-', color=colors[i % len(colors)], linewidth=2, markersize=8, label=label)
    
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    
    plt.axhline(0, color='black', linewidth=2)
    plt.axvline(0, color='black', linewidth=2)
    plt.grid(True)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    st.pyplot(plt)

# Titik-titik asli
x = [-2, -1, 0, 1, 2]
y = [3, 0, 3, 0, 3]

# Header untuk aplikasi Streamlit
st.title('Visualisasi Fungsi Transformasi')

# Data untuk grafik asli dan transformasi
data_sets = []

# Grafik asli f(x)
data_sets.append((x, y, 'f(x)'))

# Grafik f(x - 2)
x_shifted = np.array(x) + 2
data_sets.append((x_shifted, y, 'f(x - 2)'))

# Grafik f(x + 1)
x_shifted = np.array(x) - 1
data_sets.append((x_shifted, y, 'f(x + 1)'))

# Grafik f(2x)
x_scaled = np.array(x) / 2
data_sets.append((x_scaled, y, 'f(2x)'))

# Grafik (1/2)f(x)
y_scaled = np.array(y) / 2
data_sets.append((x, y_scaled, '(1/2)f(x)'))

# Grafik 2f(x)
y_scaled = np.array(y) * 2
data_sets.append((x, y_scaled, '2f(x)'))

# Grafik f(x/2)
x_scaled = np.array(x) * 2
data_sets.append((x_scaled, y, 'f(x/2)'))

# Plot semua grafik dalam satu plot
st.header("Semua Grafik Digabungkan")
plot_combined_graph(data_sets, 'x', 'y', 'Grafik Semua Fungsi', xlim=(-5, 5), ylim=(-1, 7))

# Plot masing-masing grafik untuk memperjelas
st.header("Grafik Setiap Fungsi")

# Grafik asli f(x)
st.subheader("Grafik f(x)")
plot_single_graph(x, y, 'x', 'y', 'f(x)', xlim=(-5, 5), ylim=(-1, 7), color='b')

# Grafik f(x - 2)
st.subheader("Grafik f(x - 2)")
x_shifted = np.array(x) + 2
plot_single_graph(x_shifted, y, 'x', 'y', 'f(x - 2)', xlim=(-5, 5), ylim=(-1, 7), color='g')

# Grafik f(x + 1)
st.subheader("Grafik f(x + 1)")
x_shifted = np.array(x) - 1
plot_single_graph(x_shifted, y, 'x', 'y', 'f(x + 1)', xlim=(-5, 5), ylim=(-1, 7), color='r')

# Grafik f(2x)
st.subheader("Grafik f(2x)")
x_scaled = np.array(x) / 2
plot_single_graph(x_scaled, y, 'x', 'y', 'f(2x)', xlim=(-5, 5), ylim=(-1, 7), color='c')

# Grafik (1/2)f(x)
st.subheader("Grafik (1/2)f(x)")
y_scaled = np.array(y) / 2
plot_single_graph(x, y_scaled, 'x', 'y', '(1/2)f(x)', xlim=(-5, 5), ylim=(-1, 7), color='m')

# Grafik 2f(x)
st.subheader("Grafik 2f(x)")
y_scaled = np.array(y) * 2
plot_single_graph(x, y_scaled, 'x', 'y', '2f(x)', xlim=(-5, 5), ylim=(-1, 7), color='y')

# Grafik f(x/2)
st.subheader("Grafik f(x/2)")
x_scaled = np.array(x) * 2
plot_single_graph(x_scaled, y, 'x', 'y', 'f(x/2)', xlim=(-5, 5), ylim=(-1, 7), color='k')
