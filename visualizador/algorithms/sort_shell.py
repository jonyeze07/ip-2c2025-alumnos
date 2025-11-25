items = []
n = 0
d = 0
i = 0
reverse = 0

def init(vals):
    global items, n, i, d, seguir, reverse
    items = list(vals)
    n = len(items)
    d = n//2
    i = 0
    seguir = False
    
def step():
  global items, n, i, d, seguir, reverse
  if reverse == 0:    
    swap = False 
    if i+d < n:
        if items[i] > items[i + d]:
            items[i], items[i + d] = items[i+d], items[i]
            swap = True 
            seguir = True
            i += 1
            return{"a": i-1, "b": i+d-1, "swap": True, "done": False}  
        i += 1
        return{"a": i-1, "b": i+d-1, "swap": False, "done": False}
    else:
       if d > 1:
          seguir = True
       if d/2 >= 1:
        d = d//2
        i = 0 
    if seguir == True:
        seguir = False
        return{"a": i-1, "b": i+d-1, "swap": False, "done": False}
    if seguir == False:       
      return {"done": True}
    return{"a": i-1, "b": i+d-1, "swap": False, "done": False}
  else:
    swap = False 
    if i+d < n:
        if items[i] < items[i + d]:
            items[i], items[i + d] = items[i+d], items[i]
            swap = True
            seguir = True
            i += 1
            return{"a": i-1, "b": i+d-1, "swap": True, "done": False}  
        i += 1
        return{"a": i-1, "b": i+d-1, "swap": False, "done": False}
    else:
       if d > 1:
          seguir = True
       if d/2 >= 1:
        d = d//2
        i = 0 
    if seguir == True:
        i = 0
        seguir = False
        return{"a": i-1, "b": i+d-1, "swap": False, "done": False}
    if seguir == False:       
      return {"done": True}
    return{"a": i-1, "b": i+d-1, "swap": False, "done": False}