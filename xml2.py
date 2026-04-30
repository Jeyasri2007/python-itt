
maxdepth = 0
def depth(elem, level):
    global maxdepth
    # Update maxdepth if current level is deeper
    if level + 1 > maxdepth:
        maxdepth = level + 1
    
    # Recursively check children
    for child in elem:
        depth(child, level + 1)
