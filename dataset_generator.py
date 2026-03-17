import random
import csv

max_vert = 10

# Implementing Erdos-Renyi model of random graph
def build_random_graph(n,p):
    verts = list(range(n))
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                edges.append((i, j))
    print(verts, edges)

for i in range(1,100):
    n = random.randint(1, max_vert)
    p = 0.5
    build_random_graph(n,p)
