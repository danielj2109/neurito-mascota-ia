# Neurito: experimentos
 
## Experimentos
 
**1.** Con hambre 0.5 y energía 0.5, la acción cambia a jugar cuando el aburrimiento pasa de 0.5. La acción cambia cuando la necesidad que cambia supera a las otras dos.
 
**2.** Con las tres necesidades en 0.5, Softmax da casi lo mismo a cada acción (35 %, 33 % y 31 %). Si el hambre sube un poco, a 0.6, comer sube a 78 %.
 
**3.**
- 3 neuronas: pérdida de 0.16 y precisión de 96.3 %.
- 6 neuronas: pérdida de 0.12 y precisión de 99.4 %.
- 10 neuronas: pérdida de 0.13 y precisión de 99.3 %.
- 20 neuronas: pérdida de 0.12 y precisión de 98.8 %.
 
Con 3 neuronas aprende peor. Con más de 6 casi no mejora.
 
**4.**
- Con 200 épocas no alcanza a aprender (91.8 %).
- Con 5000 épocas mejora muy poco: se estanca (99.6 %).
- Con tasa 0.01 aprende muy lento (82.9 %).
- Con tasa 5.0 o más se vuelve inestable y no aprende (33.8 %).

**5.** Una cuarta necesidad como entrada, por ejemplo "suciedad", y una cuarta etiqueta, por ejemplo "bañarse", que se escoja cuando la suciedad sea la necesidad más alta. La red tendría 4 entradas y 4 salidas.
 
## Explica tus resultados
 
**1. ¿En qué se diferencian pesos y sesgos?**
 
Los pesos multiplican las entradas y dicen qué tan importante es cada una. El sesgo es un valor que se suma para ajustar el resultado.
 
**2. ¿Por qué el cansancio es `1 - energía`?**
 
Porque son opuestos: a menos energía, más cansancio. Así un valor alto significa más necesidad de dormir, igual que con el hambre y el aburrimiento.
 
**3. ¿Qué hace ReLU y qué hace Softmax?**
 
ReLU convierte los valores negativos en 0 y deja los positivos igual. Softmax convierte las salidas en probabilidades que suman 100 %.
 
**4. ¿Por qué una precisión alta puede ser engañosa?**
 
Porque se mide contra una regla inventada y fácil, no contra situaciones reales. La red copia esa regla, pero eso no significa que tome buenas decisiones en la vida real.
 