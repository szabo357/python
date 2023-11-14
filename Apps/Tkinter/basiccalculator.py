import tkinter as tk

def calcular(operacion):
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicacion":
        resultado = num1 * num2
    elif operacion == "division":
        if num2 !=0 :
            resultado = num1 / num2
        else:
            resultado = 'Error: División por cero'
    result_label.config(text = "Resultado: " + str(resultado))
    
root = tk.Tk()
root.title("calculadora")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

suma_button = tk.Button(root,text="Suma",command=lambda:calcular('suma'))
suma_button.pack()


resta_button = tk.Button(root,text="Resta",command=lambda:
                         calcular('resta'))
resta_button.pack()


multiplicacion_button = tk.Button(root,text="multiplicación",command=lambda:
                               calcular('multiplicacion'))
multiplicacion_button.pack()


division_button = tk.Button(root,text="División",command=lambda:
                            calcular('division'))
division_button.pack()

result_label = tk.Label(root,text="Resultado: ")
result_label.pack()

root.mainloop()