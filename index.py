import tkinter as tk
import random

#Definir una pregunta y respuesta

pregunta = [
    {
        'pregunta':'¿Como se dice 1 en ingles?:',
        'opciones': ['eight', 'one', 'ten'],
        'respuesta_correcta':'one'
    },
    {
        'pregunta':'¿Como se dice 2 en ingles?:',
        'opciones': ['two', 'twenty-two', 'three'],
        'respuesta_correcta':'two'
    },
    {
        'pregunta':'¿Como se dice 3 en ingles?:',
        'opciones': ['four', 'twenty-six', 'three'],
        'respuesta_correcta':'three'
    },
    {
        'pregunta':'¿Como se dice 4 en ingles?:',
        'opciones': ['four', 'thirty', 'forty-four'],
        'respuesta_correcta':'four'
    },
    {
        'pregunta':'¿Como se dice 5 en ingles?:',
        'opciones': ['seventeen', 'five', 'six'],
        'respuesta_correcta':'five'
    },
    {
        'pregunta':'¿Como se dice 6 en ingles?:',
        'opciones': ['seventeen', 'seven', 'six'],
        'respuesta_correcta':'six'
    },
    {
        'pregunta':'¿Como se dice 7 en ingles?:',
        'opciones': ['fifteen', 'seven', 'nineteen'],
        'respuesta_correcta':'seven'
    },
    {
        'pregunta':'¿Como se dice 8 en ingles?:',
        'opciones': ['eight', 'fifty', 'thirty-six'],
        'respuesta_correcta':'eight'
    },
    {
        'pregunta':'¿Como se dice 9 en ingles?:',
        'opciones': ['five', 'eighteen', 'nine'],
        'respuesta_correcta':'nine'
    },
    {
        'pregunta':'¿Como se dice 10 en ingles?:',
        'opciones': ['thirty-six', 'ten', 'fifteen'],
        'respuesta_correcta':'ten'
    },
    {
        'pregunta':'¿Como se dice 11 en ingles?:',
        'opciones': ['ten', 'eleven', 'five'],
        'respuesta_correcta':'eleven'
    },
    {
        'pregunta':'¿Como se dice 12 en ingles?:',
        'opciones': ['fifteen', 'fifty', 'twelve'],
        'respuesta_correcta':'twelve'
    },
    {
        'pregunta':'¿Como se dice 13 en ingles?:',
        'opciones': ['thirteen', 'fifteen', 'twelve'],
        'respuesta_correcta':'thirteen'
    },
    {
        'pregunta':'¿Como se dice 14 en ingles?:',
        'opciones': ['nine', 'fourteen', 'ten'],
        'respuesta_correcta':'fourteen'
    },
    {
        'pregunta':'¿Como se dice 15 en ingles?:',
        'opciones': ['sixteen', 'five', 'fifteen'],
        'respuesta_correcta':'fifteen'
    },
    {
        'pregunta':'¿Como se dice 16 en ingles?:',
        'opciones': ['sixteen', 'thirty-six', 'twenty-nine'],
        'respuesta_correcta':'sixteen'
    },
    {
        'pregunta':'¿Como se dice 17 en ingles?:',
        'opciones': ['eight', 'seventeen', 'twenty-nine'],
        'respuesta_correcta':'seventeen'
    },
    {
        'pregunta':'¿Como se dice 18 en ingles?:',
        'opciones': ['eighteen', 'ten', 'thirty-six'],
        'respuesta_correcta':'eighteen'
    },
    {
        'pregunta':'¿Como se dice 19 en ingles?:',
        'opciones': ['seventeen', 'fifteen', 'nineteen'],
        'respuesta_correcta':'nineteen'
    },
    {
        'pregunta':'¿Como se dice 20 en ingles?:',
        'opciones': ['sixteen', 'twenty', 'five'],
        'respuesta_correcta':'twenty'
    },
    {
        'pregunta':'¿Como se dice 21 en ingles?:',
        'opciones': ['twenty-one', 'nineteen', 'fifteen'],
        'respuesta_correcta':'twenty-one'
    },
    {
        'pregunta':'¿Como se dice 22 en ingles?:',
        'opciones': ['nineteen', 'ten', 'twenty-two'],
        'respuesta_correcta':'twenty-two'
    },
    {
        'pregunta':'¿Como se dice 23 en ingles?:',
        'opciones': ['fifteen', 'twenty-three', 'sixteen'],
        'respuesta_correcta':'twenty-three'
    },
    {
        'pregunta':'¿Como se dice 24 en ingles?:',
        'opciones': ['five', 'twenty-four', 'fifteen'],
        'respuesta_correcta':'twenty-four'
    },
    {
        'pregunta':'¿Como se dice 25 en ingles?:',
        'opciones': ['twenty-five', 'thirty-six', 'nineteen'],
        'respuesta_correcta':'twenty-five'
    },
    {
        'pregunta':'¿Como se dice 26 en ingles?:',
        'opciones': ['five', 'fifty', 'twenty-six'],
        'respuesta_correcta':'twenty-six'
    },
    {
        'pregunta':'¿Como se dice 27 en ingles?:',
        'opciones': ['twenty-seven', 'thirty-six', 'seventeen'],
        'respuesta_correcta':'twenty-seven'
    },
    {
        'pregunta':'¿Como se dice 28 en ingles?:',
        'opciones': ['ten', 'twenty-eight', 'thirty-six'],
        'respuesta_correcta':'twenty-eight'
    },
    {
        'pregunta':'¿Como se dice 29 en ingles?:',
        'opciones': ['fifty', 'thirty-six', 'twenty-nine'],
        'respuesta_correcta':'twenty-nine'
    },
    {
        'pregunta':'¿Como se dice 30 en ingles?:',
        'opciones': ['nineteen', 'thirty', 'five'],
        'respuesta_correcta':'thirty'
    },
    {
        'pregunta':'¿Como se dice 31 en ingles?:',
        'opciones': ['thirty-one', 'seventeen', 'fifty'],
        'respuesta_correcta':'thirty-one'
    },
    {
        'pregunta':'¿Como se dice 32 en ingles?:',
        'opciones': ['sixteen', 'thirty-two', 'thirty-three'],
        'respuesta_correcta':'thirty-two'
    },
    {
        'pregunta':'¿Como se dice 33 en ingles?:',
        'opciones': ['nineteen', 'five', 'thirty-three'],
        'respuesta_correcta':'thirty-three'
    },
    {
        'pregunta':'¿Como se dice 34 en ingles?:',
        'opciones': ['thirty-four', 'eighteen', 'ten'],
        'respuesta_correcta':'thirty-four'
    },
    {
        'pregunta':'¿Como se dice 35 en ingles?:',
        'opciones': ['nineteen', 'thirty-five', 'eighteen'],
        'respuesta_correcta':'thirty-five'
    },
    {
        'pregunta':'¿Como se dice 36 en ingles?:',
        'opciones': ['fifty', 'five', 'thirty-six'],
        'respuesta_correcta':'thirty-six'
    },
    {
        'pregunta':'¿Como se dice 37 en ingles?:',
        'opciones': ['nineteen', 'thirty-seven', 'sixteen'],
        'respuesta_correcta':'thirty-seven'
    },
    {
        'pregunta':'¿Como se dice 38 en ingles?:',
        'opciones': ['thirty-eight', 'nineteen', 'eighteen'],
        'respuesta_correcta':'thirty-eight'
    },
    {
        'pregunta':'¿Como se dice 39 en ingles?:',
        'opciones': ['ten', 'thirty-nine', 'nineteen'],
        'respuesta_correcta':'thirty-nine'
    },
    {
        'pregunta':'¿Como se dice 40 en ingles?:',
        'opciones': ['fifty', 'forty', 'five'],
        'respuesta_correcta':'forty'
    },
    {
        'pregunta':'¿Como se dice 41 en ingles?:',
        'opciones': ['sixteen', 'ten', 'forty-one'],
        'respuesta_correcta':'forty-one'
    },
    {
        'pregunta':'¿Como se dice 42 en ingles?:',
        'opciones': ['nineteen', 'forty-two', 'seventeen'],
        'respuesta_correcta':'forty-two'
    },
    {
        'pregunta':'¿Como se dice 43 en ingles?:',
        'opciones': ['forty-three', 'nineteen', 'fifty'],
        'respuesta_correcta':'forty-three'
    },
    {
        'pregunta':'¿Como se dice 44 en ingles?:',
        'opciones': ['nineteen', 'forty-four', 'nineteen'],
        'respuesta_correcta':'forty-four'
    },
    {
        'pregunta':'¿Como se dice 45 en ingles?:',
        'opciones': ['five', 'nineteen', 'forty-five'],
        'respuesta_correcta':'forty-five'
    },
    {
        'pregunta':'¿Como se dice 46 en ingles?:',
        'opciones': ['seventeen', 'forty-six', 'ten'],
        'respuesta_correcta':'forty-six'
    },
    {
        'pregunta':'¿Como se dice 47 en ingles?:',
        'opciones': ['forty-seven', 'nineteen', 'seventeen'],
        'respuesta_correcta':'forty-seven'
    },
    {
        'pregunta':'¿Como se dice 48 en ingles?:',
        'opciones': ['nineteen', 'forty-eight', 'five'],
        'respuesta_correcta':'forty-eight'
    },
    {
        'pregunta':'¿Como se dice 49 en ingles?:',
        'opciones': ['five', 'forty-nine', 'nineteen'],
        'respuesta_correcta':'forty-nine'
    },
    {
        'pregunta':'¿Como se dice 50 en ingles?:',
        'opciones': ['five', 'nineteen', 'fifty'],
        'respuesta_correcta':'fifty'
    },
]

def mostrar_pregunta():
    #Función para mostrar una nueva pregunta y opciones de respuesta
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    resultado_texto.set('')
    if not preguntas_disponibles:
        #Si no hay más preguntas disponibles, mostrar mensaje y finalizar el juego.
        pregunta_texto.set('No hay más preguntas disponibles.')
        siguiente_boton.config(state=tk.DISABLED)
        terminar_juego()
        return
    pregunta_actual = random.choice(preguntas_disponibles)
    pregunta_texto.set(pregunta_actual['pregunta'])
    for i, opcion in enumerate(pregunta_actual['opciones']):
        botones_opciones[i].config(text=opcion)
    siguiente_boton.config(state=tk.DISABLED)
    puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

def verificar_respuesta(respuesta):
    #Función para verificar la respuesta seleccionada por el usuario
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    if pregunta_actual['respuesta_correcta'] == respuesta:
        resultado_texto.set('¡Respuesta Correcta!')
        puntaje_actual += 10
    else:
        resultado_texto.set('Respuesta Incorrecta')
    siguiente_boton.config(state=tk.NORMAL)
    #Eliminar la pregunta actual de la lsita de preguntas disponibles
    preguntas_disponibles.remove(pregunta_actual)
    
def terminar_juego():
    #Funcion para finalizar el juego y mostrar el puntaje final
    global puntaje_actual
    pregunta_texto.set('Juego Terminado')
    for boton in botones_opciones:
        boton.config(state=tk.DISABLED)
    resultado_texto.set(f'Puntaje final:{puntaje_actual}')
    
#Configuar la ventana principal
ventana= tk.Tk()
ventana.title('Juego de Preguntas y Respuestas en ingles')

#Crear una copia de la lista de preguntas disponibles al inicio del juego
preguntas_disponibles = pregunta.copy()

#Variable para llevar un registro de la pregunta actual
pregunta_actual = None

#Variable para mostrar la pregunta actual
pregunta_texto = tk.StringVar()
pregunta_label = tk.Label(ventana, textvariable=pregunta_texto, font=('Arial',14))
pregunta_label.pack(pady=10)

#Botones para opciones de respuesta
botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text='', font=('Arial',12), command=lambda i=i:verificar_respuesta(pregunta_actual['opciones'][i]))
    botones_opciones.append(boton)
    boton.pack(pady=5)
    
#Variable para mostrar si la respuesta fue correcta o incorrecta
resultado_texto = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_texto,font=('Arial',12))
resultado_label.pack(pady=10)

#Botón "Siguiente"
siguiente_boton = tk.Button(ventana, text='Siguiente', font=('Arial',12),command=mostrar_pregunta)
siguiente_boton.pack(pady=10)
siguiente_boton.config(state=tk.DISABLED)

#Puntaje Actual
puntaje_actual = 0
puntaje_label = tk.Label(ventana, text=f"Puntaje actual: {puntaje_actual}",font=('Arial',12))
puntaje_label.pack(pady=10)

#Botón "Terminar Juego"
terminar_boton = tk.Button(ventana, text='Terminar Juego', font=('Arial',12), command=terminar_juego)
terminar_boton.pack(pady=10)

#Iniciar el juego
mostrar_pregunta()

#Iniciar el bucle principal de la aplicación
ventana.mainloop()