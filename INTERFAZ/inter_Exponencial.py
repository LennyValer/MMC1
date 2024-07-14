import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.integrate import odeint
import numpy as np

def modelo_exponencial(A, t, k):
    dA_dt = k * A
    return dA_dt

def actualizar_grafica():
    A0 = float(entry_A0.get())
    k = float(entry_k.get())
    T = float(entry_tiempo.get())
    
    condiciones_iniciales = [A0]
    t = np.linspace(0, T, 100)
    solucion = odeint(modelo_exponencial, condiciones_iniciales, t, args=(k,))
    
    A = solucion[:, 0]
    
    ax.clear()
    ax.plot(t, A, label='Población (A)', color='blue')
    ax.set_xlabel('Tiempo (t)')
    ax.set_ylabel('Población (A)')
    ax.set_title('Modelo Exponencial')
    ax.legend()
    ax.grid(True)
    canvas.draw()

def incrementar_valor(entry):
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(value + 1))

def decrementar_valor(entry):
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(value - 1))

root = tk.Tk()
root.title("Modelo Exponencial")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Parámetros del modelo
ttk.Label(frame, text="Población inicial (A0):").grid(row=0, column=0, sticky=tk.E)
entry_A0 = ttk.Entry(frame)
entry_A0.grid(row=0, column=1)
ttk.Button(frame, text="↑", command=lambda: incrementar_valor(entry_A0)).grid(row=0, column=2)
ttk.Button(frame, text="↓", command=lambda: decrementar_valor(entry_A0)).grid(row=0, column=3)

ttk.Label(frame, text="Tasa de crecimiento (k):").grid(row=1, column=0, sticky=tk.E)
entry_k = ttk.Entry(frame)
entry_k.grid(row=1, column=1)
ttk.Button(frame, text="↑", command=lambda: incrementar_valor(entry_k)).grid(row=1, column=2)
ttk.Button(frame, text="↓", command=lambda: decrementar_valor(entry_k)).grid(row=1, column=3)

# Tiempo de simulación
ttk.Label(frame, text="Tiempo:").grid(row=2, column=0, sticky=tk.E)
entry_tiempo = ttk.Entry(frame)
entry_tiempo.grid(row=2, column=1)
ttk.Button(frame, text="↑", command=lambda: incrementar_valor(entry_tiempo)).grid(row=2, column=2)
ttk.Button(frame, text="↓", command=lambda: decrementar_valor(entry_tiempo)).grid(row=2, column=3)

# Botón para actualizar la gráfica
boton = ttk.Button(frame, text="Graficar", command=actualizar_grafica)
boton.grid(row=3, column=0, columnspan=4)

# Configuración de la gráfica
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0)

root.mainloop()
