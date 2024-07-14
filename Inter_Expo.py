import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.integrate import odeint
import tkinter as tk
from tkinter import ttk

def crecimiento_exponencial(NP, t, r):
    N = NP[0]
    dN_dt = r * N  # Ecuación de crecimiento exponencial
    return [dN_dt]

def actualizar_plot():
    N0 = float(entry_N0.get())
    r = float(entry_r.get())
    T = float(entry_time.get())
    
    y0 = [N0]
    t = np.linspace(0, T, 500)
    params = (r,)
    sol = odeint(crecimiento_exponencial, y0, t, args=params)
    
    N = sol.T[0]
    
    ax.clear()
    if plot_type.get() == 'N vs t':
        ax.plot(t, N, label='Población (N)', color='blue')
        ax.set_xlabel('Tiempo (t)')
        ax.set_ylabel('Población')
    else:
        # Para el modelo exponencial, la trayectoria en el plano de fase es trivial (una línea)
        ax.plot(N, np.exp(N), label='Trayectoria', color='blue')  # Solo para visualización
        ax.set_xlabel('Especie (N)')
        ax.set_ylabel('Exponencial de N')

    ax.set_title('Modelo de Crecimiento Exponencial')
    ax.legend()
    ax.grid(True)
    canvas.draw()

def increment_entry(entry):
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(value + 1))

def decrement_entry(entry):
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(value - 1))

root = tk.Tk()
root.title("Modelo de Crecimiento Exponencial")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Parámetros iniciales
ttk.Label(frame, text="Parámetros iniciales").grid(row=0, column=0, columnspan=2)

ttk.Label(frame, text="N0:").grid(row=1, column=0, sticky=tk.E)
entry_N0 = ttk.Entry(frame)
entry_N0.grid(row=1, column=1)
ttk.Button(frame, text="↑", command=lambda: increment_entry(entry_N0)).grid(row=1, column=2)
ttk.Button(frame, text="↓", command=lambda: decrement_entry(entry_N0)).grid(row=1, column=3)

ttk.Label(frame, text="r:").grid(row=2, column=0, sticky=tk.E)
entry_r = ttk.Entry(frame)
entry_r.grid(row=2, column=1)
ttk.Button(frame, text="↑", command=lambda: increment_entry(entry_r)).grid(row=2, column=2)
ttk.Button(frame, text="↓", command=lambda: decrement_entry(entry_r)).grid(row=2, column=3)

# Tiempo de simulación
ttk.Label(frame, text="Tiempo:").grid(row=3, column=0, sticky=tk.E)
entry_time = ttk.Entry(frame)
entry_time.grid(row=3, column=1)
ttk.Button(frame, text="↑", command=lambda: increment_entry(entry_time)).grid(row=3, column=2)
ttk.Button(frame, text="↓", command=lambda: decrement_entry(entry_time)).grid(row=3, column=3)

# Tipo de gráfica
plot_type = tk.StringVar(value='N vs t')
ttk.Radiobutton(frame, text='N vs t', variable=plot_type, value='N vs t').grid(row=4, column=0, columnspan=2)
ttk.Radiobutton(frame, text='Plano Fase (N vs exp(N))', variable=plot_type, value='Plano Fase').grid(row=4, column=2, columnspan=2)

# Botón para actualizar la gráfica
button = ttk.Button(frame, text="Graficar", command=actualizar_plot)
button.grid(row=5, column=0, columnspan=4)

# Configuración de la gráfica
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0)

root.mainloop()
