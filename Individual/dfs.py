import time

start_time = time.time()
# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {
    'Вінниця': set(['Вінницькі Хутори', 'Бохоніки']),
    'Вінницькі Хутори': set(['Вінниця', 'Щитки']),
    'Щитки': set(['Вінницькі Хутори', 'Писарівка']),
    'Писарівка': set(['Щитки', 'Говрилівка']),
    'Говрилівка': set(['Писарівка', 'Стадниця']),
    'Стадниця': set(['Говрилівка', 'Лавровка']),
    'Лавровка': set(['Стадниця', 'Стрижівка']),
    'Стрижівка': set(['Лавровка', 'Тютюнники']),
    'Тютюнники': set(['Стрижівка', 'Переорки']),
    'Переорки': set(['Тютюнники', 'Мизяківські хутори']),
    'Мизяківські хутори': set(['Переорки', 'Душковці']),
    'Душковці': set(['Мизяківські хутори', 'Якушенці']),
    'Якушенці': set(['Душковці', 'Зарванці']),
    'Зарванці': set(['Якушенці', 'Березине']),
    'Березине': set(['Зарванці', 'Агрономічне']),
    'Агрономічне': set(['Березине', 'Бохоніки']),
    'Бохоніки': set(['Агрономічне', 'Вінниця']),
}

dfs(graph, 'Вінниця')
print("\nЧас виконання алгоритма: ", str((time.time() - start_time) * 1000).replace('.', ','), "ms")
