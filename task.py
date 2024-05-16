import math
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex].keys()) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited


def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(list(graph[vertex].keys())))


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph[current_vertex].keys():
            if graph[current_vertex][neighbor]["weight"]:
                weight = graph[current_vertex][neighbor]["weight"]
            else:
                weight = 1
            #print(f"{current_vertex}<--[{weight}]-->{neighbor}")
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
            
            #print(f"{distances}")

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


# Вузли –– обласні центри з координатами
cities = {
    'Вінниця': (28.4682, 49.2331),
    'Дніпро': (35.0462, 48.4647),
    'Донецьк': (37.8028, 48.0159),
    'Житомир': (28.6587, 50.2547),
    'Запоріжжя': (35.1396, 47.8388),
    'Івано-Франківськ': (24.7111, 48.9226),
    'Київ': (30.5234, 50.4501),
    'Кропивницький': (32.2597, 48.5132),
    'Луганськ': (39.3078, 48.5740),
    'Луцьк': (25.3424, 50.7593),
    'Львів': (24.0297, 49.8397),
    'Миколаїв': (31.9946, 46.9750),
    'Одеса': (30.7233, 46.4825),
    'Полтава': (34.5514, 49.5883),
    'Рівне': (26.2516, 50.6199),
    'Суми': (34.7981, 50.9077),
    'Тернопіль': (25.5948, 49.5535),
    'Ужгород': (22.2879, 48.6208),
    'Харків': (36.2304, 49.9935),
    'Херсон': (32.6169, 46.6354),
    'Хмельницький': (26.9871, 49.4225),
    'Черкаси': (32.0598, 49.4444),
    'Чернівці': (25.9358, 48.2921),
    'Чернігів': (31.2893, 51.4982)
}

# Ребра між містами –– умовні автошляхи
edges = [('Київ', 'Житомир'),
         ('Київ', 'Черкаси'),
         ('Київ', 'Суми'),
         ('Київ', 'Полтава'),
         ('Київ', 'Одеса'),
         ('Вінниця', 'Житомир'),
         ('Вінниця', 'Кропивницький'),
         ('Вінниця', 'Хмельницький'),
         ('Дніпро', 'Запоріжжя'),
         ('Дніпро', 'Полтава'),
         ('Дніпро', 'Харків'),
         ('Донецьк', 'Луганськ'),
         ('Житомир', 'Вінниця'),
         ('Житомир', 'Рівне'),
         ('Запоріжжя', 'Дніпро'),
         ('Івано-Франківськ', 'Тернопіль'),
         ('Київ', 'Чернігів'),
         ('Кропивницький', 'Черкаси'),
         ('Кропивницький', 'Дніпро'),
         ('Луганськ', 'Донецьк'),
         ('Луцьк', 'Рівне'),
         ('Львів', 'Івано-Франківськ'),
         ('Львів', 'Тернопіль'),
         ('Львів', 'Луцьк'),
         ('Миколаїв', 'Херсон'),
         ('Миколаїв', 'Кропивницький'),
         ('Миколаїв', 'Запоріжжя'),
         ('Одеса', 'Миколаїв'),
         ('Одеса', 'Вінниця'),
         ('Полтава', 'Дніпро'),
         ('Рівне', 'Луцьк'),
         ('Суми', 'Полтава'),
         ('Тернопіль', 'Івано-Франківськ'),
         ('Тернопіль', 'Хмельницький'),
         ('Ужгород', 'Львів'),
         ('Ужгород', 'Івано-Франківськ'),
         ('Харків', 'Суми'),
         ('Харків', 'Полтава'),
         ('Херсон', 'Миколаїв'),
         ('Хмельницький', 'Рівне'),
         ('Черкаси', 'Кропивницький'),
         ('Черкаси', 'Полтава'),
         ('Чернівці', 'Тернопіль'),
         ('Чернівці', 'Івано-Франківськ'),
         ('Чернівці', 'Вінниця'),
         ('Чернігів', 'Київ')]

def main():
    # Створюємо граф
    G = nx.Graph()
    
    for city, coords in cities.items():
        G.add_node(city, pos=coords)
    
    # Додаємо ребра, де вага ребра –– це відстань між містами 
    for edge in edges:
        length = int(math.dist(cities[edge[0]], cities[edge[1]]) * 100)
        G.add_edge(*edge, weight=length)
    
    # Завдання 1. Основні характеристики
    print(f"Кількість вузлів: {G.number_of_nodes()}")
    print(f"Кількість ребер:  {G.number_of_edges()}")
    print("\n\n")
    
    if nx.is_connected(G):
        print("Граф звʼязний")
    else:
        print("Граф незвʼязний")
    print("\n\n")
    
    for node in G:
        print(f"Ступінь вузла \"{node}\" = {len(G[node].items())}")
    print("\n\n")

    # Завдання 2
    print("DFS:")
    dfs_iterative(G, 'Київ')
    print("\n\n")

    print("BFS:")
    bfs_iterative(G, 'Київ')
    print("\n\n")

    # Завдання 3
    print("Dijkstra:")
    for city in G:
        res = dijkstra(G, city)
        for neighbor,length in res.items():
            if city != neighbor:
                print(f"Найкоротша відстань від {city} до {neighbor}: {length}")
    print("\n\n")

    # print(nx.single_source_dijkstra_path(G, 'Київ', cutoff=None, weight='weight'))

    # Малюємо граф
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_color='yellow')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos, edge_labels=labels, font_size=7, font_color='r', )
    plt.show()

if __name__ == '__main__':
    main()