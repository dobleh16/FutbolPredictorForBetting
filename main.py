import tkinter as tk
from tkinter import messagebox
from itertools import cycle
import webbrowser

def ganadorpartidoFutbol(equipol, equipov, posTablal, posTablav, numpartidos, Rlocal, Rlocav, Rvisitantel, Rvisitante, golesl, golesv,
                         Ultimos5l, Ultimos5v, Ganadosl, Empatadosl, Perdidosl, Ganadosv, Empatadosv, Perdidosv, Cuotal, CuotaV,
                         cuotadl, cuotadv, totalgolesou, montoapuesta):
    sum1 = 0
    sum2 = 0
    tg = 0

    # Comparamos la posición en la tabla
    if posTablal < posTablav:
        sum1 += 2
        sum2 -= 1
    elif posTablav < posTablal:
        sum2 += 2
        sum1 -= 1

    # Comparamos el récord de local de ambos equipos
    if Rlocal > Rlocav:
        sum1 += 2
        sum2 -= 1
    elif Rlocav > Rlocal:
        sum2 += 2
        sum1 -= 1
    else:
        sum1 += 1
        sum2 += 1

    # Comparamos el récord de visitante
    if Rvisitantel > Rvisitante:
        sum1 += 2
        sum2 -= 1
    elif Rvisitante > Rvisitantel:
        sum2 += 2
        sum1 -= 1
    else:
        sum1 += 1
        sum2 += 1

    # Comparamos los últimos 5 partidos
    if Ultimos5l > Ultimos5v:
        sum1 += 2
        sum2 -= 1
    elif Ultimos5v > Ultimos5l:
        sum2 += 2
        sum1 -= 1
    else:
        sum1 += 1
        sum2 += 1

    # Comparamos partidos ganados
    if Ganadosl > Ganadosv:
        sum1 += 2
        sum2 -= 2
    elif Ganadosv > Ganadosl:
        sum2 += 2
        sum1 -= 2
    else:
        sum1 += 1
        sum2 += 1

    # Comparamos partidos empatados
    if Empatadosl > Empatadosv:
        sum1 -= 1
        sum2 += 2
    elif Empatadosv > Empatadosl:
        sum2 -= 1
        sum1 += 2
    else:
        sum1 -= 1
        sum2 -= 1

    # Comparamos partidos perdidos
    if Perdidosl > Perdidosv:
        sum1 -= 2
        sum2 += 2
    elif Perdidosv > Perdidosl:
        sum2 -= 2
        sum1 += 2
    else:
        sum1 -= 1
        sum2 -= 1

    # Comparamos goles
    if golesl > golesv:
        sum1 += 2
        sum2 -= 1
    elif golesv > golesl:
        sum2 += 2
        sum1 -= 1
    else:
        sum1 += 1
        sum2 += 1

    tg = (golesl + golesv) / numpartidos

    # Resultados
    if sum1 > sum2:
        probabilidad = (1 / Cuotal) * 100
        probabilidad1 = (1 / cuotadl) * 100
        totalcg = ((montoapuesta * Cuotal) - montoapuesta)
        totalchl = ((montoapuesta * cuotadl) - montoapuesta)
        resultado = f"""
        El equipo que debería ganar es: {equipol}
        Probabilidad de ganar: {probabilidad:.2f}%
        Probabilidad de empate o gane: {probabilidad1:.2f}%
        Estimado a ganar con victoria: {totalcg:.2f}
        Estimado a ganar con empate/gane: {totalchl:.2f}
        Opción de goles: {'OVER' if tg > totalgolesou else 'UNDER'} ({totalgolesou})
        """
    else:
        probabilidad = (1 / CuotaV) * 100
        probabilidad1 = (1 / cuotadv) * 100
        totalcg = ((montoapuesta * CuotaV) - montoapuesta)
        totalchl = ((montoapuesta * cuotadv) - montoapuesta)
        resultado = f"""
        El equipo que debería ganar es: {equipov}
        Probabilidad de ganar: {probabilidad:.2f}%
        Probabilidad de empate o gane: {probabilidad1:.2f}%
        Estimado a ganar con victoria: {totalcg:.2f}
        Estimado a ganar con empate/gane: {totalchl:.2f}
        Opción de goles: {'OVER' if tg > totalgolesou else 'UNDER'} ({totalgolesou})
        """

    messagebox.showinfo("Resultado", resultado)
    return resultado


def cornersprediction(equipol, equipov, cornersl, cornersv, numpartidos, cornersou):
    tc = (cornersl + cornersv) / numpartidos
    if tc > cornersou:
        return f"De acuerdo a la estadística ingresada, el OVER de CORNERS es buena opción. {cornersou}"
    else:
        return f"De acuerdo a la estadística ingresada, el UNDER de CORNERS es buena opción. {cornersou}"


# Lógica de la interfaz gráfica
def datosUno():
    def procesar_datos():
        try:
            # Entradas locales
            equipol = entry_equipol.get()
            posTablal = int(entry_posTablal.get())
            Rlocal = int(entry_Rlocal.get())
            golesl = float(entry_golesl.get())
            Ultimos5l = entry_Ultimos5l.get()
            Ganadosl = int(entry_Ganadosl.get())
            Empatadosl = int(entry_Empatadosl.get())
            Perdidosl = int(entry_Perdidosl.get())
            cornersl = float(entry_cornersl.get())

            # Entradas visitantes
            equipov = entry_equipov.get()
            posTablav = int(entry_posTablav.get())
            Rvisitante = int(entry_Rvisitante.get())
            golesv = float(entry_golesv.get())
            Ultimos5v = entry_Ultimos5v.get()
            Ganadosv = int(entry_Ganadosv.get())
            Empatadosv = int(entry_Empatadosv.get())
            Perdidosv = int(entry_Perdidosv.get())
            cornersv = float(entry_cornersv.get())

            # Datos generales
            numpartidos = float(entry_numpartidos.get())
            Cuotal = float(entry_Cuotal.get())
            CuotaV = float(entry_CuotaV.get())
            cuotadl = float(entry_cuotadl.get())
            cuotadv = float(entry_cuotadv.get())
            totalgolesou = float(entry_totalgolesou.get())
            montoapuesta = float(entry_montoapuesta.get())
            cornersou = float(entry_cornersou.get())

            # Predicciones
            resultado = ganadorpartidoFutbol(
                equipol, equipov, posTablal, posTablav, numpartidos, Rlocal, 0,
                0, Rvisitante, golesl, golesv, Ultimos5l, Ultimos5v,
                Ganadosl, Empatadosl, Perdidosl, Ganadosv, Empatadosv, Perdidosv,
                Cuotal, CuotaV, cuotadl, cuotadv, totalgolesou, montoapuesta
            )
            resultado_corners = cornersprediction(equipol, equipov, cornersl, cornersv, numpartidos, cornersou)

            # Mostrar resultados
            messagebox.showinfo("Resultado", f"{resultado}\n\n{resultado_corners}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    import tkinter as tk

    # Función de ejemplo para procesar los datos
    def procesar_datos():
        print("Procesando datos...")

    # Función para actualizar los consejos
    def actualizar_consejos():
        consejo_label.config(text=next(consejos))
        window.after(6000, actualizar_consejos)  # Cambia cada 3 segundos

    # Interfaz gráfica
    window = tk.Tk()
    window.title("Bienvenido a tu Predictor de Apuestas")

    frame = tk.Frame(window)
    frame.pack(pady=20, padx=20)

    # Preguntas para equipo local
    tk.Label(frame, text="Nombre Equipo Local").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_equipol = tk.Entry(frame)
    entry_equipol.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Posición en la Tabla Local").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_posTablal = tk.Entry(frame)
    entry_posTablal.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="Partidos Ganados en casa del Local").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_Rlocal = tk.Entry(frame)
    entry_Rlocal.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame, text="Goles Marcados en total por el Local").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entry_golesl = tk.Entry(frame)
    entry_golesl.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame, text="Record Últimos 5 partidos del Local").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    entry_Ultimos5l = tk.Entry(frame)
    entry_Ultimos5l.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(frame, text="Promedio de Corners Local").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    entry_cornersl = tk.Entry(frame)
    entry_cornersl.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(frame, text="Total de Partidos Ganados del Local").grid(row=6, column=0, padx=5, pady=5, sticky="e")
    entry_Ganadosl = tk.Entry(frame)
    entry_Ganadosl.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(frame, text="Total de Partidos Empatados del Local").grid(row=7, column=0, padx=5, pady=5, sticky="e")
    entry_Empatadosl = tk.Entry(frame)
    entry_Empatadosl.grid(row=7, column=1, padx=5, pady=5)

    tk.Label(frame, text="Total de Partidos Perdidos del Local").grid(row=8, column=0, padx=5, pady=5, sticky="e")
    entry_Perdidosl = tk.Entry(frame)
    entry_Perdidosl.grid(row=8, column=1, padx=5, pady=5)

    # Preguntas para equipo visitante
    tk.Label(frame, text="Nombre Equipo Visitante").grid(row=0, column=2, padx=5, pady=5, sticky="e")
    entry_equipov = tk.Entry(frame)
    entry_equipov.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(frame, text="Posición en la Tabla Visitante").grid(row=1, column=2, padx=5, pady=5, sticky="e")
    entry_posTablav = tk.Entry(frame)
    entry_posTablav.grid(row=1, column=3, padx=5, pady=5)

    tk.Label(frame, text="Partidos Ganados de local del Visitante").grid(row=2, column=2, padx=5, pady=5, sticky="e")
    entry_Rvisitante = tk.Entry(frame)
    entry_Rvisitante.grid(row=2, column=3, padx=5, pady=5)

    tk.Label(frame, text="Goles Marcados en total por el Visitante").grid(row=3, column=2, padx=5, pady=5, sticky="e")
    entry_golesv = tk.Entry(frame)
    entry_golesv.grid(row=3, column=3, padx=5, pady=5)

    tk.Label(frame, text="Record Últimos 5 partidos del Visitante").grid(row=4, column=2, padx=5, pady=5, sticky="e")
    entry_Ultimos5v = tk.Entry(frame)
    entry_Ultimos5v.grid(row=4, column=3, padx=5, pady=5)

    tk.Label(frame, text="Promedio de Corners Visitante").grid(row=5, column=2, padx=5, pady=5, sticky="e")
    entry_cornersv = tk.Entry(frame)
    entry_cornersv.grid(row=5, column=3, padx=5, pady=5)

    tk.Label(frame, text="Total de Partidos Ganados del Visitante").grid(row=6, column=2, padx=5, pady=5, sticky="e")
    entry_Ganadosv = tk.Entry(frame)
    entry_Ganadosv.grid(row=6, column=3, padx=5, pady=5)

    tk.Label(frame, text="Total de Partidos Empatados del Visitante").grid(row=7, column=2, padx=5, pady=5, sticky="e")
    entry_Empatadosv = tk.Entry(frame)
    entry_Empatadosv.grid(row=7, column=3, padx=5, pady=5)

    tk.Label(frame, text="Total de Partidos Perdidos del Visitante").grid(row=8, column=2, padx=5, pady=5, sticky="e")
    entry_Perdidosv = tk.Entry(frame)
    entry_Perdidosv.grid(row=8, column=3, padx=5, pady=5)

    # Datos generales
    tk.Label(frame, text="Mismo Número de Partidos Jugados en total por ambos equipos").grid(row=9, column=0, padx=5,
                                                                                             pady=5, sticky="e")
    entry_numpartidos = tk.Entry(frame)
    entry_numpartidos.grid(row=9, column=1, padx=5, pady=5)

    tk.Label(frame, text="Cuota en la casa de apuesta que ganará el Local").grid(row=10, column=0, padx=5, pady=5,
                                                                                 sticky="e")
    entry_Cuotal = tk.Entry(frame)
    entry_Cuotal.grid(row=10, column=1, padx=5, pady=5)

    tk.Label(frame, text="Cuota en la casa de apuestas que ganará el Visitante").grid(row=10, column=2, padx=5, pady=5,
                                                                                      sticky="e")
    entry_CuotaV = tk.Entry(frame)
    entry_CuotaV.grid(row=10, column=3, padx=5, pady=5)

    tk.Label(frame, text="Cuota enl casa de apuestas de el Empate/gana del Local").grid(row=11, column=0, padx=5, pady=5, sticky="e")
    entry_cuotadl = tk.Entry(frame)
    entry_cuotadl.grid(row=11, column=1, padx=5, pady=5)

    tk.Label(frame, text="Cuota enl casa de apuestas de el Empate/gana del Visitante").grid(row=11, column=2, padx=5, pady=5, sticky="e")
    entry_cuotadv = tk.Entry(frame)
    entry_cuotadv.grid(row=11, column=3, padx=5, pady=5)

    tk.Label(frame, text="Cual es el Over/Under de goles en la casa de apuestas").grid(row=12, column=0, padx=5, pady=5,
                                                                            sticky="e")
    entry_totalgolesou = tk.Entry(frame)
    entry_totalgolesou.grid(row=12, column=1, padx=5, pady=5)

    tk.Label(frame, text="Monto de Apuesta").grid(row=12, column=2, padx=5, pady=5, sticky="e")
    entry_montoapuesta = tk.Entry(frame)
    entry_montoapuesta.grid(row=12, column=3, padx=5, pady=5)

    tk.Label(frame, text="Corners Over/Under en la Casa de Apuestas").grid(row=13, column=0, padx=5, pady=5, sticky="e")
    entry_cornersou = tk.Entry(frame)
    entry_cornersou.grid(row=13, column=1, padx=5, pady=5)

    # Botón de acción
    tk.Button(window, text="Calcular Predicción", command=procesar_datos).pack(pady=10)

    # Cuadro de texto para consejos
    consejos_frame = tk.Frame(window)
    consejos_frame.pack(pady=10)

    consejos = cycle([
        "Este programa funciona con cualquier liga del mundo",
        "No apuestes dinero que necesites",
        "No hagas parleys, solo apuestas sencillas",
        "Busca valor en las cuotas, la mínima ideal es 1.60"
    ])

    consejo_label = tk.Label(consejos_frame, text="", font=("Arial", 12), wraplength=400, justify="center")
    consejo_label.pack()
    actualizar_consejos()

    def abrir_enlace(url):
        webbrowser.open(url)

    # Recuadro para enlaces
    enlaces_frame = tk.Frame(window)
    enlaces_frame.pack(pady=10)

    tk.Label(enlaces_frame, text="Enlaces útiles para Estadísticas:", font=("Time New Roman", 15, "bold")).pack()

    enlace_general = tk.Label(enlaces_frame, text="Estadística General: Sofascore", fg="Blue", cursor="hand2")
    enlace_general.pack()
    enlace_general.bind("<Button-1>", lambda e: abrir_enlace("https://www.sofascore.com/"))

    enlace_corners = tk.Label(enlaces_frame, text="Corners: Footystats", fg="red", cursor="hand2")
    enlace_corners.pack()
    enlace_corners.bind("<Button-1>", lambda e: abrir_enlace("https://footystats.org/es/stats/corner-stats"))

    window.mainloop()


datosUno()
