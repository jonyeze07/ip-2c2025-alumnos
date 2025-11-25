items = []
n = 0
i = 0        
j = 0         
min_idx = 0   
fase = "buscar" 
reverse = 0 

def init(vals):
    global items, n, i, j, min_idx, fase, reverse
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():

  global items, n, i, j, min_idx, fase, reverse
  if reverse == 0:    
    swap = False
    if i == n-1:
     return {"done": True}
    if fase == "buscar":
      if items[j] < items[min_idx]:
          min_idx = j
      j += 1
      if j == n:
         fase = "swap"
          
    if fase == "swap":
      a = min_idx
      b = i
      if i != min_idx: 
       items[a] , items[b] = items[b], items[a]
       swap = True
       i += 1
       min_idx = i
       fase = "buscar"
       j  = i + 1
       return {"a": a, "b": b, "swap": True , "done": False}
      else:
       i += 1
       min_idx = i
       fase = "buscar"
       j  = i + 1

    return {"a": min_idx, "b": j, "swap": False , "done": False}
  else:
    swap = False
    if i == n-1:
     return {"done": True}
    if fase == "buscar":
      if items[j] > items[min_idx]:
          min_idx = j
      j += 1
      if j == n:
         fase = "swap"
          
    if fase == "swap":
      a = min_idx
      b = i
      if i != min_idx: 
       items[a] , items[b] = items[b], items[a]
       swap = True
       i += 1
       min_idx = i
       fase = "buscar"
       j  = i + 1
       return {"a": a, "b": b, "swap": True , "done": False}
      else:
       i += 1
       min_idx = i
       fase = "buscar"
       j  = i + 1

    return {"a": min_idx, "b": j, "swap": False , "done": False}  