items = []
n = 0
i = 0      
j = None   
reverse = 0

def init(vals):
    global items, n, i, j, reverse
    items = list(vals)
    n = len(items)
    i = 1  
    j = i

def step():
  global items, n, i, j, reverse

  if reverse == 0:
    swap = False 
    if i >= n:
       return {"done": True}
    a = 0
    b = 0
    if j > 0:
     a = j
     b = j - 1
     if items[b] > items[a]:
       items[b] ,items[a] = items[a] ,items[b]
       swap = True
       j -= 1
     else:
        i += 1 
        j = i    
    else:
        i += 1
        j = i
    return {"a": a, "b": b, "swap": swap, "done": False}
  else:
    swap = False 
    if i >= n:
       return {"done": True}
    a = 0
    b = 0
    if j == None:
       j = i
    if j > 0:
     a = j
     b = j - 1
     if items[b] < items[a]:
       items[b] ,items[a] = items[a] ,items[b]
       swap = True
       j -= 1
     else:
        i += 1 
        j = None     
    else:
        i += 1
        j = None
    return {"a": a, "b": b, "swap": swap, "done": False}     