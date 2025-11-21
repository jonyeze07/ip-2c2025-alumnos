items = []
n = 0
i = 0
j = 0
pivot = items[n-1]
recorer = items[:]
menores = []
pivot_lista = []
mayores = []
def init(vals):
    global items, n, i, j, pivot, recorer, menores, mayores, pivot_lista
    items = list(vals)
    n = len(items)
    i = 0
    pivot = items[n-1]
    j = 0 
    recorer = items[:]
    menores = []
    pivot_lista = []
    mayores = []

def step(): 
    global items, n, i, j, pivot, recorer, menores, mayores, pivot_lista
    swap = False
    if i < len(recorer): 
     if recorer[i]>pivot:
        mayores.append(recorer[i])
        i += 1
        {"a": recorer[j], "b": recorer[i], "swap": True, "done": False}
     if recorer[i]<pivot:
        menores.append(recorer[i])
        j +=1
        recorer[i],recorer[j] = recorer[j],recorer[i]
        swap = True
        i +=1
        {"a": recorer[j], "b": recorer[i], "swap": True, "done": False}
     if recorer[i] == pivot:
        j += 1
        recorer[i],recorer[j] = recorer[j],recorer[i]
        pivot_lista.apppend(recorer[i])
        swap = True 
        i += 1
        {"a": recorer[j], "b": recorer[i], "swap": True, "done": False}
    else:
        if len(mayores) > 2:
            recorer = mayores
        else:
            recorer = menores
        if len(mayores) < 2 and len(menores) < 2:
           return {"done": True}
        else:
           mayores = []
           menores = []
    i = 0
    j = 0
    {"a": recorer[j], "b": recorer[i], "swap": True, "done": False}