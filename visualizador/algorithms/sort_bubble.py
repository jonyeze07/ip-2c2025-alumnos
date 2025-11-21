items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():

    global items, n, i, j
    swap = False
 
    a = j
    b = j + 1

    if n - i - 1 == 0:
        return {"done": True}        
    
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True
    
    j += 1
    
    if b == n - i - 1:
        j = 0
        i += 1
    return {"a": a, "b": b, "swap": swap, "done": False}
