items = []
n = 0
i = 0
j = 0
pivot  = []
fase = 1
posicion = []
parte = ""

def init(vals):
    global items, n, i, j, pivot, fase, pivot, posicion, parte, pivot_actual, proceso
    items = list(vals)
    n = len(items)
    i = 0
    pivot = items[-1]
    posicion = []
    j = -1
    fase = 1
    parte = "menores"
    pivot_actual = []
    proceso = False

def step():
    global items, n, i, j, pivot, fase, pivot, posicion, parte, pivot_actual, proceso
    swap = True
    if fase == 1:
        if items[i] < pivot:
            j += 1
            items[i], items[j] = items[j], items[i]
            swap = True 
            i += 1
            return {"a": i-1, "b": j, "swap": True, "done": False}
        if items[i] == pivot:
            j += 1
            if parte == "menores": 
             posicion.append(j)
            else:
                if not j in posicion:
                 proceso = False
                 pivot_actual.append(j)
                else:
                 proceso = True
            items[i], items[j] = items[j], items[i]
            swap = True
            fase = 2
            i +=1
            return {"a": i-1, "b": j, "swap": True, "done": False}
        i += 1
        return {"a": i-1, "b": j, "swap": False, "done": False}
    if fase == 2:
        if parte == "menores":
            i = 0
            j = -1
            if pivot == 0:
                parte = "menores_subiendo"
            else:
             pivot = items[posicion[-1]-1]
        if parte == "menores_subiendo":
           if len(posicion) > 2:
            if proceso == False:  
               if len(pivot_actual) == 0:
                  i = posicion[-1]
                  j = posicion[-1]-1
                  pivot = items[posicion[-2]-1]          
               else:
                  i = posicion[-1]
                  j = posicion[-1]-1
                  pivot = items[pivot_actual[-1]-1]          
            else:
                  posicion = posicion[:-1] + pivot_actual[:]
                  i = posicion[-1]
                  j = posicion[-1]-1
                  pivot = items[posicion[-2]-1]          
     

        fase = 1
        return {"a": i-1, "b": j, "swap": False, "done": False}
            