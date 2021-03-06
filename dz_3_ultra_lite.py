# Методы списка
# Перечисление по мере частоты применения (и почему я так считаю)

'''

list.append(x) - вставляет элемент х в конец списка (очень часто приходится заполнять пустой список значениями)

list.copy() - создаёт поверхностную копию списка (нередко приходится создавать копию, чтобы с ней работать)

list.insert(i, x) - вставляет на i-тый элемент значение x (нередко приходится изменять список на месте)

list.pop([i]) - удаляет i-тый элемент и возвращает его (нередко приходится что-то удалять из списка)

list.extend(L) - расширяет элементы списка, добавляя в конец все элементы списка L (иногда нужно объединить списки)

list.count(x) - возвращает количество элементов со значением x (нередко нужно узнать кол-во каких-то элементов)

list.index(x[,start [,end]]) - возвращает положение первого элемента со значением x, при этом поиск ведется от start
до end (иногда может понадобиться понять, где расположен конкретный элемент списка для каких-то действий с ним)

list.sort([key=функция]) - сортирует список на основе функции (иногда необходимо отсортировать данные в нужном порядке)

list.reverse() - разворачивает список (иногда может понадобиться)

list.clear() - очищает список (иногда нужно очистить данные, чтобы потом заполнить их другими)

'''

