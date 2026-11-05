"""Compara BFS, DFS y A* como profesores de Neurito en el laberinto."""
import heapq
import random

import numpy as np

from laberinto_mundo import MAPAS, Laberinto, distancias_bfs, elegir_accion, libres, valido, vecino
from laberinto_red import RedLaberinto, codificar


# Profesores: cada uno dice el primer movimiento hacia la comida

def paso_bfs(mapa, origen, meta):
    """BFS: camino más corto, revisando por niveles."""
    dist = distancias_bfs(mapa, meta)
    opciones = [(dist.get(vecino(origen, a), 10**9), a) for a in range(4)]
    return min(opciones)[1]


def paso_dfs(mapa, origen, meta):
    """DFS: sigue un camino hasta el fondo antes de probar otro."""
    visitadas = {origen}

    def buscar(posicion, primero):
        if posicion == meta:
            return primero
        for a in range(4):
            siguiente = vecino(posicion, a)
            if valido(mapa, siguiente) and siguiente not in visitadas:
                visitadas.add(siguiente)
                resultado = buscar(siguiente, a if primero is None else primero)
                if resultado is not None:
                    return resultado
        return None

    return buscar(origen, None)


def paso_astar(mapa, origen, meta):
    """A*: camino más corto usando la distancia Manhattan como guía."""
    def h(p):
        return abs(p[0] - meta[0]) + abs(p[1] - meta[1])

    abiertos = [(h(origen), 0, origen, None)]
    mejor = {origen: 0}
    while abiertos:
        _, g, posicion, primero = heapq.heappop(abiertos)
        if posicion == meta:
            return primero
        for a in range(4):
            siguiente = vecino(posicion, a)
            if valido(mapa, siguiente) and g + 1 < mejor.get(siguiente, 10**9):
                mejor[siguiente] = g + 1
                heapq.heappush(abiertos, (
                    g + 1 + h(siguiente), g + 1, siguiente,
                    a if primero is None else primero,
                ))
    return None


# Datos de entrenamiento con cada profesor

def generar_datos(paso, semilla=42):
    muestras = []
    for indice, mapa in enumerate(MAPAS):
        celdas = libres(mapa)
        for meta in celdas:
            for posicion in celdas:
                if posicion != meta:
                    muestras.append((indice, posicion, meta, paso(mapa, posicion, meta)))
    rng = np.random.default_rng(semilla)
    rng.shuffle(muestras)
    corte = int(len(muestras) * 0.8)

    def arrays(filas):
        X = np.stack([codificar(i, p, m) for i, p, m, a in filas])
        y = np.asarray([a for i, p, m, a in filas])
        return X, y

    return arrays(muestras[:corte]), arrays(muestras[corte:])


# Jugar: igual que el juego, 45 intentos por reto

def jugar(red, asistido, retos=300, semilla=7):
    azar = random.Random(semilla)
    comidas = 0
    for k in range(retos):
        indice = k % len(MAPAS)
        mundo = Laberinto(indice)
        celdas = libres(MAPAS[indice])
        mundo.meta = azar.choice(celdas)
        mundo.posicion = azar.choice([p for p in celdas if p != mundo.meta])
        mundo.visitadas = {mundo.posicion: 1}
        mundo.intentos = 0
        while mundo.intentos < 45:
            accion, _ = elegir_accion(red, mundo, mundo.visitadas, asistido)
            if mundo.mover(accion) == "comida":
                comidas += 1
                break
    return comidas


if __name__ == "__main__":
    RETOS = 300
    EPOCAS = 200
    for nombre, paso in (("BFS", paso_bfs), ("DFS", paso_dfs), ("A*", paso_astar)):
        (X, y), (Xt, yt) = generar_datos(paso)
        red = RedLaberinto()
        for _ in range(EPOCAS):
            red.entrenar_epoca(X, y)
        print(f"\n{nombre}")
        print(f"  Pérdida: {red.historial[-1]:.4f}")
        print(f"  Exactitud prueba: {red.exactitud(Xt, yt):.1%}")
        print(f"  Comidas red pura: {jugar(red, False, RETOS)}/{RETOS}")
        print(f"  Comidas asistido: {jugar(red, True, RETOS)}/{RETOS}")
