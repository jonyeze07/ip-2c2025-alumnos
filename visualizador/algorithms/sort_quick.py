items = []
n = 0
i = 0
j = 0
pivot =[]
fase = 1
d = 0
def init(vals):
    global items, n, i, j, pivot, fase, lista, d   
    items = list(vals)
    n = len(items)
    i = 0
    pivot = items[n-1]
    j = -1
    lista = items
    d = 0
    fase = 1

def step():
    global items, n, i, j, pivot, fase, lista, d
    if fase == 1:   
        if i <= n-1 - d:
            if items[i + d] < pivot:
             j += 1
             items[i + d], items[j + d] = items[j + d], items[i + d]
             swap = True
             i += 1
             return {"a": j  + d, "b": i - 1 + d, "swap": True, "done": False}    
            if items[i + d] == pivot:
                j += 1
                items[i + d], items[j + d] = items[j + d], items[i + d]
                swap = True
                i += 1
                return {"a": j  + d, "b": i - 1 + d, "swap": True, "done": False}
            i += 1
            return {"a": j + d, "b": i - 1 + d, "swap": False, "done": False}
        else:
          menores = items[d : d + j]
          i = 0
          j = i -1
          pivot = menores[len(menores)-1]
          n = len(menores)
          fase = 2
    if fase == 2:
          if i <= n-1 - d:  
             if items[i + d] < pivot: 
                j += 1
                items[i + d], items[j + d] = items[j + d], items[i + d]
                swap = True
                i += 1
                return {"a": j  + d, "b": i - 1 + d, "swap": True, "done": False}
             if items[i+d] == pivot:
                 j += 1
                 items[i + d], items[j + d] = items[j + d], items[i + d]
                 swap = True
                 i += 1
                 return {"a": j  + d, "b": i - 1 + d, "swap": True, "done": False}
             i +=1
             return {"a": j + d, "b": i - 1 + d, "swap": False, "done": False}
          else:
                 menores = items[d : j + d]
                 i = 0
                 j = -1
                 pivot = menores[len(menores)-1]
                 n = len(menores)
                 if len(menores)< 3:
                    n = len(items)
                    pivot = items[n-1]
                    lista.pop(0,1)
                    d = len(items) - len(lista)
                    fase = 1
                 return {"a": j + d, "b": i - 1 + d, "swap": False, "done": False}
             
             
                



        

            
    