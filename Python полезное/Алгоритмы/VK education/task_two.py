def find_three_mutual_friends(graph):
    # Перебираем все вершины графа
    for person in graph:
        # Перебираем друзей текущего человека
        for friend1 in graph[person]:
            for friend2 in graph[friend1]:
                # Проверяем, что friend2 не является тем же самым человеком, что person
                if friend2 != person:
                    # Проверяем, что friend2 дружит с person и friend1
                    if friend2 in graph[person] and friend2 in graph[friend1]:
                        # Три человека взаимно дружат друг с другом
                        return True
    # Тройка не найдена
    return False


# Считываем количество рёбер в графе
N = int(input())

# Создаем пустой граф в виде словаря
graph = {}

# Считываем рёбра и строим граф
for _ in range(N):
    u, v = map(int, input().split())

    # Добавляем вершины в граф
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    # Добавляем ребро между вершинами
    graph[u].append(v)
    graph[v].append(u)

# Проверяем, существуют ли три человека, которые все взаимно дружат друг с другом
result = find_three_mutual_friends(graph)

# Выводим результат
if result:
    print("YES")
else:
    print("NO")