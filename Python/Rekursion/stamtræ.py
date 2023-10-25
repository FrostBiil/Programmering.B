# 1. Læs koden for metoden displayDescendants.
# tree.py
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)

    def displayDescendants(self):
        print('(', end='')
        for c in self.children:
            # Grundlæggende tilfælde:
            print(c.data + ' ', end='')
            # Rekursivt tilfælde:
            c.displayDescendants()
        print(') ', end='')

esther = Node("Esther")
esther.addChild(Node("Bent"))
esther.addChild(Node("Else"))
erna = Node("Erna")
esther.addChild(erna)
lotte = Node("Lotte")
erna.addChild(lotte)
lotte.addChild(Node("Hugo"))
lotte.addChild(Node("Harald"))
esther.displayDescendants()

# 2. Overvej hvad koden gør.

"koden generer et stamtræ for efterkommere af Ester"

# 3. Ret i programmets sidste linje, så det i stedet viser efterkommere af Erna.
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)

    def displayDescendants(self):
        print('(', end='')
        for c in self.children:
            # Grundlæggende tilfælde:
            print(c.data + ' ', end='')
            # Rekursivt tilfælde:
            c.displayDescendants()
        print(') ', end='')

esther = Node("Esther")
esther.addChild(Node("Bent"))
esther.addChild(Node("Else"))
erna = Node("Erna")
esther.addChild(erna)
lotte = Node("Lotte")
erna.addChild(lotte)
lotte.addChild(Node("Hugo"))
lotte.addChild(Node("Harald"))
erna.displayDescendants() #esther.displayDescendants()


# 4. Tilføj en linje, så det også viser efterkommere af Lotte.
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)

    def displayDescendants(self):
        print('(', end='')
        for c in self.children:
            # Grundlæggende tilfælde:
            print(c.data + ' ', end='')
            # Rekursivt tilfælde:
            c.displayDescendants()
        print(') ', end='')

esther = Node("Esther")
esther.addChild(Node("Bent"))
esther.addChild(Node("Else"))
erna = Node("Erna")
esther.addChild(erna)
lotte = Node("Lotte")
erna.addChild(lotte)
lotte.addChild(Node("Hugo"))
lotte.addChild(Node("Harald"))
erna.displayDescendants() #esther.displayDescendants()
lotte.displayDescendants()

# 1. Kør programmet ovenfor.
"Done"
# 2. Læs koden for metoden isAncestorOf.

# ancestor.py
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)

    def displayDescendants(self):
        print('(', end='')
        for c in self.children:
            # Grundlæggende tilfælde
            print(c.data + ' ', end='')
            # Rekursivt tilfælde
            c.displayDescendants()
        print(') ', end='')

    def isAncestorOf(self, item):
        for c in self.children:
            # Grundlæggende tilfælde
            if c.data == item: return True
            # Rekursivt tilfælde
            elif c.isAncestorOf(item): return True
        return False

esther = Node("Esther")
esther.addChild(Node("Bent"))
esther.addChild(Node("Else"))
erna = Node("Erna")
esther.addChild(erna)
lotte = Node("Lotte")
erna.addChild(lotte)
lotte.addChild(Node("Hugo"))
lotte.addChild(Node("Harald"))
esther.displayDescendants()
print()
print("Bent: " + str(esther.isAncestorOf("Bent")))
print("Hugo: " + str(esther.isAncestorOf("Hugo")))
print("Jesper: " + str(esther.isAncestorOf("Jesper")))

# 3. Forklar det grundlæggende tilfælde og det rekursive tilfælde.

"Det grundlæggende tilfælde er, hvis c.data er lig med item returneres true"
"Det rekursive tilfælde er, hvis c.isancestorOf(Item) returneres true"

# 4. Brug metoden isAncestorOf til at undersøge, om Harald er efterkommer af Erna.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)

    def displayDescendants(self):
        print('(', end='')
        for c in self.children:
            # Grundlæggende tilfælde
            print(c.data + ' ', end='')
            # Rekursivt tilfælde
            c.displayDescendants()
        print(') ', end='')

    def isAncestorOf(self, item):
        for c in self.children:
            # Grundlæggende tilfælde
            if c.data == item: return True
            # Rekursivt tilfælde
            elif c.isAncestorOf(item): return True
        return False

esther = Node("Esther")
esther.addChild(Node("Bent"))
esther.addChild(Node("Else"))
erna = Node("Erna")
esther.addChild(erna)
lotte = Node("Lotte")
erna.addChild(lotte)
lotte.addChild(Node("Hugo"))
lotte.addChild(Node("Harald"))
esther.displayDescendants()
print()
print("Bent: " + str(esther.isAncestorOf("Bent")))
print("Hugo: " + str(esther.isAncestorOf("Hugo")))
print("Jesper: " + str(esther.isAncestorOf("Jesper")))

print("Herald: " + str(erna.isAncestorOf("Herald")))

"Dette returnere, at Herald ikke er efterkommer af Erna"

# 5. Se videoen herunder, som visualiserer kørslen af programmet.
"Done"