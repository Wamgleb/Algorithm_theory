import time

start_time = time.time()

def qsort(s):
    if len(s) <= 1:
        return s


    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    centrt = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return qsort(left) + centrt + qsort(right)

coordin = [(49.20 ,'Вінницькі Хутори'), 
           (49.16, 'Бохоніки'),
           (49.23, 'Вінниця'), 
           (49.19, 'Щитки'),
           (49.52, 'Писарівка'), 
           (49.41, 'Говрилівка'),
           (49.28, 'Стадниця'), 
           (49.34, 'Лавровка'), 
           (49.31, 'Стрижівка'), 
           (49.33, 'Тютюнники'), 
           (49.32, 'Переорки'),
           (49.33, 'Мизяківські хутори'), 
           (48.91, 'Душковці'),
           (49.25, 'Якушенці'), 
           (49.25, 'Зарванці'), 
           (49.22, 'Березине'),
           (49.19, 'Агрономічне'), 
]

popular = [
           (7723 ,'Вінницькі Хутори'), 
           (1690, 'Бохоніки'),
           (370834, 'Вінниця'), 
           (1182, 'Щитки'),
           (1448, 'Писарівка'), 
           (2988, 'Говрилівка'),
           (1291, 'Стадниця'), 
           (862, 'Лавровка'), 
           (1310, 'Стрижівка'), 
           (294, 'Тютюнники'), 
           (402, 'Переорки'),
           (1500, 'Мизяківські хутори'), 
           (724, 'Душковці'),
           (4024, 'Якушенці'), 
           (7305, 'Зарванці'), 
           (3556, 'Березине'),
           (1703, 'Агрономічне'), 
]

a = qsort(coordin)
b = qsort(popular)
print("Відсортований список міст в залежності від координат:\n", a, "\n")
print("Відсортований список міст в залежності від кількості населення:\n", b, "\n")
print("Час виконання алгоритму: ", str((time.time() - start_time) * 1000), "ms")