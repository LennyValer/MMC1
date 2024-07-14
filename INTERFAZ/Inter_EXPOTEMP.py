import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.integrate import odeint
import tkinter as tk
from tkinter import ttk

# Ecuación de crecimiento exponencial de temperaturas
def crecimiento_temperatura(T, t, Tm, k):
    return [k * (T[0] - Tm)]  # dT/dt = k * (T - Tm)

def actualizar_plot():
    T0 = float(entry_T0.get())
    Tm = float(entry_Tm.get())
    k = float(entry_k.get())
    T = float(entry_time.get())
    
    y0 = [T0]
    t = np.linspace(0, T, 500)
    params = (Tm, k)
    sol = odeint(crecimiento_temperatura, y0, t, args=params)
    
    T = sol.T[0]
    
    ax.clear()
    if plot_type.get() == 'T vs t':
        ax.plot(t, T, label='Temperatura (T)', color='blue')
        ax.set_xlabel('Tiempo (t)')
        ax.set_ylabel('Temperatura')
    else:
        # Para el modelo de temperaturas, la trayectoria en el plano de fase es trivial
        ax.plot(T, np.exp(T), label='Trayectoria', color='blue')  # Solo para visualización
        ax.set_xlabel('Temperatura (T)')
        ax.set_ylabel('Exponencial de T')

    ax.set_title('Modelo de Crecimiento Exponencial de Temperaturas')
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
root.title("Modelo de Crecimiento Exponencial de Temperaturas")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Parámetros iniciales
ttk.Label(frame, text="Parámetros iniciales").grid(row=0, column=0, columnspan=2)

ttk.Label(frame, text="T0:").grid(row=1, column=0, sticky=tk.E)
entry_T0 = ttk.Entry(frame)
entry_T0.grid(row=1, column=1)
ttk.Button(frame, text="↑", command=lambda: increment_entry(entry_T0)).grid(row=1, column=2)
ttk.Button(frame, text="↓", command=lambda: decrement_entry(entry_T0)).grid(row=1, column=3)

ttk.Label(frame, text="Tm:").grid(row=2, column=0, sticky=tk.E)
entry_Tm = ttk.Entry(frame)
entry_Tm.grid(row=2, column=1)
ttk.Button(frame, text="↑", command=lambda: increment_entry(entry_Tm)).grid(row=2, column=2)
ttk.Button(frame, text="↓", command=lambda: decrement_entry(entry_Tm)).grid(row=2, column=3)

ttk.Label(frame, text="k:").grid(row=3, column=0, sticky=tk.E)
entry_k = ttk.Entry(frame)
entry_k.grid(row=3, column=1)
ttk.Button(frame, text="↑", command=lambda: increment_entry(entry_k)).grid(row=3, column=2)
ttk.Button(frame, text="↓", command=lambda: decrement_entry(entry_k)).grid(row=3, column=3)

# Tiempo de simulación
ttk.Label(frame, text="Tiempo:").grid(row=4, column=0, sticky=tk.E)
entry_time = ttk.Entry(frame)
entry_time.grid(row=4, column=1)
ttk.Button(frame, text="↑", command=lambda: increment_entry(entry_time)).grid(row=4, column=2)
ttk.Button(frame, text="↓", command=lambda: decrement_entry(entry_time)).grid(row=4, column=3)

# Tipo de gráfica
plot_type = tk.StringVar(value='T vs t')
ttk.Radiobutton(frame, text='T vs t', variable=plot_type, value='T vs t').grid(row=5, column=0, columnspan=2)
ttk.Radiobutton(frame, text='Plano Fase (T vs exp(T))', variable=plot_type, value='Plano Fase').grid(row=5, column=2, columnspan=2)

# Botón para actualizar la gráfica
button = ttk.Button(frame, text="Graficar", command=actualizar_plot)
button.grid(row=6, column=0, columnspan=4)

# Configuración de la gráfica
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0)

root.mainloop()
