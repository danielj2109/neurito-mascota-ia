# Neurito: experimentos 2
 
## Experimentos 2

*1. Prueba el juego sin entrenar. Anota colisiones y obstáculos esquivados.*

Sin entrenar, no aprende como saltar

![alt text](assets/SinEntrenar.png)

*2. Entrena de cien en cien épocas; compara la pérdida, la precisión y el comportamiento.*

![alt text](assets/100.png) ![alt text](assets/200.png) ![alt text](assets/300.png) ![alt text](assets/400.png) ![alt text](assets/500.png) ![alt text](assets/600.png) ![alt text](assets/700.png) ![alt text](assets/800.png)


En este caso, cada 100 se fue aumentando el porcentaje de precisión de la prueba, pero en la epoca 500 se noto que su porcentaje subio a 95.0%, pero al realizar sus 10 saltos con esta epoca subio progresivamente hasta llegar a 96.3%

*3. Cambia `ocultas=12` por `ocultas=3` o `ocultas=24`; compara generalización.*

- **3 neuronas:** pérdida de 0.2086, precisión de 93.5 % en entrenamiento y 93.1 % en prueba.
- **12 neuronas:** pérdida de 0.0730, precisión de 97.6 % en entrenamiento y 97.0 % en prueba.
- **24 neuronas:** pérdida de 0.0607, precisión de 98.0 % en entrenamiento y 97.7 % en prueba.

*4. Modifica la tasa de aprendizaje `0.8` a `0.01` o `1.2` y estudia la convergencia.*
 
Con 800 épocas:
 
- **Tasa 0.01:** converge muy lento. La pérdida solo baja de 0.7099 a 0.4583 y la precisión queda en 85.9 %. En el juego no esquivó ningún obstáculo y chocó 15 veces.
- **Tasa 0.8 (original):** la pérdida baja a 0.0730 y la precisión llega a 97.0 %. No chocó.
- **Tasa 1.2:** converge más rápido. La pérdida baja a 0.0481 y la precisión llega a 98.1 %. No chocó.