"""
Conception d'une classe `MinStack` (pile) supportant les opérations suivantes :

- `push(val)` : pousse l'élément `val` sur la pile.
- `pop()` : supprime l'élément au sommet de la pile.
- `top()` : retourne l'élément au sommet de la pile.
- `getMin()` : récupère l'élément minimum actuel de la pile.

Les spécifications demandent des opérations en O(1). Dans cette version
le `getMin()` parcourt la pile (O(n)). Pour une version O(1), on peut
conserver une pile auxiliaire des minima.
"""
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val=min(val,self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            del self.stack[-1] 
            del self.minStack[-1]      

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
        
