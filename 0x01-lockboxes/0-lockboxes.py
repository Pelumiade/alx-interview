#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    keys = set(boxes[0]) # start with the keys in the first box
    unlocked = set([0]) # start with the first box unlocked
    
    while True:
        previous_unlocked = unlocked.copy()
        
        for i in range(n):
            if i in unlocked: # if the box is already unlocked
                keys.update(boxes[i]) # add its keys to our set
                continue
                
            if i not in keys: # if we don't have the key to unlock the box
                continue
                
            # unlock the box and add its keys to our set
            unlocked.add(i)
            keys.update(boxes[i])
            
        if unlocked == previous_unlocked: # if we couldn't unlock any more boxes
            break
            
    return len(unlocked) == n # check if all boxes are unlocked

