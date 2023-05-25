from tkinter import *

#---------------------
# VARIABLES GLOBALES
#--------------------

BASE = 460
ALTURA = 220

#--------------------
# VENTANA PRINCIPAL
#--------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#----------------------
# Frame de graficacion
#----------------------

frame_graficacion = Frame(ventana_principal)    
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# creacion canvas 

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)
        
linea_central_horizontal = c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="green")
linea_central_vertical = c.create_line(BASE/2,0,BASE/2,ALTURA, fill= "green")


cuerpo_del_tren = c.create_rectangle(BASE/2-75,ALTURA/2+30,BASE/2+75,ALTURA/2-25, fill="red")
cabeza_del_tren = c.create_rectangle(BASE/2+65,ALTURA/2-25,BASE/2-5,ALTURA/2-75, fill="white")
ventana_del_tren = c.create_rectangle(BASE/2+55,ALTURA/2-35,BASE/2+5,ALTURA/2-65, fill="black")
tubo_de_escape_tren = c.create_rectangle(BASE/2-65,ALTURA/2-25,BASE/2-40,ALTURA/2-50, fill="pink")
tubo_de_escape_tren_2 = c.create_rectangle(BASE/2-27,ALTURA/2-65,BASE/2-75,ALTURA/2-50, fill="gray")
sombrero_de_tren_1 = c.create_rectangle(BASE/2+75,ALTURA/2-70,BASE/2-15,ALTURA/2-85, fill="blue")
sombrero_de_tren_2 = c.create_rectangle(BASE/2+65,ALTURA/2-85,BASE/2-5,ALTURA/2-95, fill="gold")
rueda_de_tren_1 = c.create_oval(BASE/2+30,ALTURA/2+60,BASE/2+75,ALTURA/2+15, fill="brown")
rueda_de_tren_2 = c.create_oval(BASE/2-80,ALTURA/2+60,BASE/2-30,ALTURA/2+15, fill="brown")
rueda_de_tren_3 = c.create_oval(BASE/2-25,ALTURA/2+60,BASE/2+25,ALTURA/2+15, fill="brown")
unidor_de_ruedas_1 = c.create_rectangle(BASE/2-50,ALTURA/2+40,BASE/2+1,ALTURA/2+50, fill="SeaGreen1")
unidor_de_ruedas_2 = c.create_rectangle(BASE/2+10,ALTURA/2+40,BASE/2+60,ALTURA/2+50, fill="SeaGreen1")
parachoques_1 = c.create_oval(BASE/2-130,ALTURA/2+25,BASE/2-75,ALTURA/2-20, fill="purple")
parachoques_tren_2 = c.create_rectangle(BASE/2-75,ALTURA/2+30,BASE/2-90,ALTURA/2-25, fill="white")
parachoques_tren_3 = c.create_rectangle(BASE/2-105,ALTURA/2+35,BASE/2-85,ALTURA/2-30, fill="gray")
nombre_ñero = c.create_text(BASE/2,ALTURA/2, text="El Ñero Manuelito", font=10)
carita_pŕo = c.create_oval(BASE/2+55,ALTURA/2-35,BASE/2+5,ALTURA/2-65, fill="yellow")
ojitos_Carita = c.create_oval(BASE/2+30,ALTURA/2-45,BASE/2+45,ALTURA/2-55, fill="white")
ojitos_Carita_2 = c.create_oval(BASE/2+10,ALTURA/2-45,BASE/2+25,ALTURA/2-55, fill="white")
pupilas_1 = c.create_oval(BASE/2+10,ALTURA/2-50,BASE/2+20,ALTURA/2-45, fill="red")
pupilas_2 = c.create_oval(BASE/2+30,ALTURA/2-50,BASE/2+40,ALTURA/2-45, fill="red")


#--------------------
#----CONTROLES------
#--------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

# desplegar ventana

ventana_principal.mainloop()

