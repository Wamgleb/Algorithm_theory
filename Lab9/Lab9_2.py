INF = 9999999
# кількість вершин у графіку
V = 5
# створити 2d-масив розміром 5x5
# для матриці суміжності для представлення графіка
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
# створити масив для відстеження вибраної вершини
# вибране стане істинним, інакше хибним
selected = [0, 0, 0, 0, 0]
# встановити номер ребра 0
no_edge = 0
'''число ребра в мінімальному дереві, що охоплює, 
завжди буде менше (V - 1), де V - кількість вершин у графі, 
виберіть 0-ю вершину і зробіть це істинним'''
selected[0] = True
# друк для краю та ваги
print("Edge : Weight\n")
while (no_edge < V - 1):
    '''Для кожної вершини множини S знайдіть усі сусідні вершини, 
    обчисліть відстань від вершини, вибраної на кроці 1.,
    якщо вершина вже є в множині S, відкиньте її, інакше виберіть іншу вершину, 
    найближчу до вибраної вершини, на кроці 1.'''
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    # не має краю у вибраному і
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1