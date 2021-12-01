# Regular Programming
def celsiusToFahrenheit(C):
    return C * 1.8 + 32

print(celsiusToFahrenheit(100))

#### Machine Learning
# Aplicaciones: Valor de una casa, Clasificacion de correos SPAM, Deteccion de fraudes, Calculo de tiempos
# Input and output are known but algorithm is unknown

# Arquitectura (al menos 1 capa de entrada y otra de salida)
# Pueden tener capas intermedias (ocultas)
# Capas y neuronas
# Cada capa se conecta con conexiones 
# Cada conexion tiene un peso (weight) que representa la importancia de la conexion entre las neuronas
# Sesgo de la neurona (bias) valor de la neurona

import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8 , 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# capa = tf.keras.layers.Dense(units=1, input_shape=[1])
# modelo = tf.keras.Sequential([capa])

#Cambiando de una capa visible a tres ocultas

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=600, verbose=False)

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.savefig('ml_celToFah.png')

print("Hagamos una prediccion")
resultado = modelo.predict([100.0])
print("El resultado es " + str(resultado) + " fahrenheit")

print("Variables internas del modelo")
#print(capa.get_weights())



# Weight and bias ( Peso y sesgo)
# Variables internas del modelo
# [array([[1.8084855]], dtype=float32), array([30.707108], dtype=float32)]

# Funcion lineal y = mx + b  Fahrenheit = Celsius * 1.8 + 32

# Redes neuronales convolucional
