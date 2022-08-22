examen_m=float(input("Examen de matematicas: "))
tarea_1_m=float(input("digite primera tarea de matematicas: "))
tarea_2_m=float(input("digite segunda tarea de matematicas: "))
tarea_3_m=float(input("digite tercera tarea de matematicas: "))
examen_f=float(input("Examen de fisica: "))
tarea_1_f=float(input("digite primera tarea de fisica: "))
tarea_2_f=float(input("digite segunda tarea de fisica: "))
examen_q=float(input("Examen de quimica: "))
tarea_1_q=float(input("digite primera tarea de quimica: "))
tarea_2_q=float(input("digite segunda tarea de quimica: "))
tarea_3_q=float(input("digite tercera tarea de quimica: "))
ma=examen_m*0.90+((tarea_1_m)+(tarea_2_m)+(tarea_3_m)/3)*0.10
fi=examen_f*0.80+((tarea_1_f)+(tarea_2_f)/2)*0.15
qu=examen_q*0.85+((tarea_1_q)+(tarea_2_q)+(tarea_3_q)/3)*0.15
promedio=(ma+fi+qu)/3
print()
