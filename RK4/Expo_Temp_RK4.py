import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Solución analítica para el modelo exponencial de temperaturas
def temperature_analytical(t, Tm, A0, k):
    return Tm + (A0 - Tm) * np.exp(k * t)

# Implementación del método de Runge-Kutta de orden 4 (RK4)
def temperature_rk4(t0, tf, h, Tm, A0, k):
    t_valores = np.arange(t0, tf + h, h)
    T_valores = np.zeros_like(t_valores)
    T_valores[0] = A0

    for i in range(1, len(t_valores)):
        t = t_valores[i-1]
        T = T_valores[i-1]

        k1 = k * (T - Tm)
        k2 = k * (T + 0.5 * h * k1 - Tm)
        k3 = k * (T + 0.5 * h * k2 - Tm)
        k4 = k * (T + h * k3 - Tm)

        T_valores[i] = T + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return t_valores, T_valores

# Función para ejecutar la simulación
def run_simulation():
    try:
        A0 = float(entry_A0.get())
        Tm = float(entry_Tm.get())
        k = float(entry_k.get())
        t0 = 0
        tf = 10
        h = 0.1

        # Limpiar la gráfica anterior
        ax.clear()

        # Solución numérica - RK4
        t_rk4, T_rk4 = temperature_rk4(t0, tf, h, Tm, A0, k)

        # Solución analítica
        t_analytical = np.arange(t0, tf + h, h)
        T_analytical = temperature_analytical(t_analytical, Tm, A0, k)

        # Actualizar la gráfica
        ax.plot(t_rk4, T_rk4, 's', label='Solución Numérica (RK4)', color='cyan')
        ax.plot(t_analytical, T_analytical, '-', label='Solución Analítica', color='blue')
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Temperatura (T)')
        ax.set_title('Modelo Exponencial de Temperaturas: Comparación de Soluciones')
        ax.legend()
        ax.grid(True)

        # Mostrar la gráfica actualizada
        canvas.draw()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Modelo Exponencial de Temperaturas")

# Crear un marco para organizar los widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Entradas de parámetros
tk.Label(frame, text="Temperatura inicial (A0):").grid(row=0, column=0)
entry_A0 = tk.Entry(frame)
entry_A0.grid(row=0, column=1)

tk.Label(frame, text="Temperatura del medio (Tm):").grid(row=1, column=0)
entry_Tm = tk.Entry(frame)
entry_Tm.grid(row=1, column=1)

tk.Label(frame, text="Tasa de cambio (k):").grid(row=2, column=0)
entry_k = tk.Entry(frame)
entry_k.grid(row=2, column=1)

# Botón para ejecutar la simulación
button_run = tk.Button(frame, text="Ejecutar Simulación", command=run_simulation)
button_run.grid(row=3, columnspan=2, pady=10)

# Crear la figura y el canvas para la gráfica
fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Iniciar la interfaz
root.mainloop()
