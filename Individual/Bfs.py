from collections import deque
import time

start_time = time.time()

graph = {
    'Вінниця': ['Вінницькі Хутори', 'Бохоніки'],
    'Вінницькі Хутори': ['Вінниця', 'Щитки'],
    'Щитки': ['Вінницькі Хутори', 'Писарівка'],
    'Писарівка': ['Щитки', 'Говрилівка'],
    'Говрилівка': ['Писарівка', 'Стадниця'],
    'Стадниця': ['Говрилівка', 'Лавровка'],
    'Лавровка': ['Стадниця', 'Стрижівка'],
    'Стрижівка': ['Лавровка', 'Тютюнники'],
    'Тютюнники': ['Стрижівка', 'Переорки'],
    'Переорки': ['Тютюнники', 'Мизяківські хутори'],
    'Мизяківські хутори': ['Переорки', 'Душковці'],
    'Душковці': ['Мизяківські хутори', 'Якушенці'],
    'Якушенці': ['Душковці', 'Зарванці'],
    'Зарванці': ['Якушенці', 'Березине'],
    'Березине': ['Зарванці', 'Агрономічне'],
    'Агрономічне': ['Березине', 'Бохоніки'],
    'Бохоніки': ['Агрономічне', 'Вінниця'],
}

def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in  next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return visited

start = 'Вінниця'
goal = 'Якушенці'
visited = bfs(start, goal, graph)

cur_node = goal
print(f'\nШлях з {goal} до {start}: \n {goal}', end='')

while cur_node != start:
    cur_node = visited[cur_node]
    print(f'---> {cur_node}', end='')

print("\nЧас виконання алгоритма: ", str((time.time() - start_time) * 1000).replace('.', ','), "ms")

