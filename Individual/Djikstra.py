import heapq
from heapq import *
import time

start_time = time.time()

graph = {
    'Вінниця': [(9.3 ,'Вінницькі Хутори'), (14, 'Бохоніки')],
    'Вінницькі Хутори': [(9.3, 'Вінниця'), (7.1, 'Щитки')],
    'Щитки': [(7.1, 'Вінницькі Хутори'), (4.6, 'Писарівка')],
    'Писарівка': [(4.6, 'Щитки'), (7.5, 'Говрилівка')],
    'Говрилівка': [(7.5, 'Писарівка'), (8.4, 'Стадниця')],
    'Стадниця': [(8.4, 'Говрилівка'), (22, 'Лавровка')],
    'Лавровка': [(22, 'Стадниця'), (4.5, 'Стрижівка')],
    'Стрижівка': [(4.5, 'Лавровка'), (8.3, 'Тютюнники')],
    'Тютюнники': [(8.3, 'Стрижівка'), (4.3, 'Переорки')],
    'Переорки': [(4.3, 'Тютюнники'), (5.9, 'Мизяківські хутори')],
    'Мизяківські хутори': [(5.9, 'Переорки'), (36, 'Душковці')],
    'Душковці': [(36, 'Мизяківські хутори'), (15, 'Якушенці')],
    'Якушенці': [(15, 'Душковці'), (4.6, 'Зарванці')],
    'Зарванці': [(4.6, 'Якушенці'), (8.2, 'Березине')],
    'Березине': [(8.2, 'Зарванці'), (7.9, 'Агрономічне')],
    'Агрономічне': [(7.9, 'Березине'), (5.9, 'Бохоніки')],
    'Бохоніки': [(5.9, 'Агрономічне'), (14, 'Вінниця')],
}

def dijkstra(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_cost == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited

start = 'Вінниця'
goal = 'Якушенці'
visited = dijkstra(start, goal, graph)

cur_node = goal
print(f'\nШлях з {goal} до {start}: \n {goal}', end='')

while cur_node != start:
    cur_node = visited[cur_node]
    print(f'---> {cur_node}', end='')

print("\nЧас виконання алгоритма: ", str((time.time() - start_time) * 1000).replace('.', ','), "ms")
