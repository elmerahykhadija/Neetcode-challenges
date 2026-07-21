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

    def push(self, val: int) -> None:
        self.stack.append(val)        

    def pop(self) -> None:
        if not self.stack :
            return
        self.stack=self.stack[:-1]

    def top(self) -> int:
        a=self.stack[-1]
        return a

    def getMin(self) -> int:
        minimum=self.stack[0]
        for i in range(0,len(self.stack)):
            if minimum > self.stack[i]:
                minimum=self.stack[i]
        return minimum

        
