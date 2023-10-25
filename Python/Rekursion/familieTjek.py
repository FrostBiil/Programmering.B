class Node(object):
    def __init__(self, data, parent=None):
        self.parent = parent
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
    
    def oldestParent(self, item):
        if self.parent == None: 
            return self.data
        return self.parent.oldestParent(item)        

    def isInFamily(self, item, item2):
        if (self.oldestParent(item) and self.oldestParent(item2)):
            return True
        
esther = Node("Esther")
esther.addChild(Node("Bent", "Esther"))
esther.addChild(Node("Else", "Esther"))
erna = Node("Erna", "Esther")
esther.addChild(erna)
lotte = Node("Lotte", "Erna")
erna.addChild(lotte)
lotte.addChild(Node("Hugo", "Lotte"))
lotte.addChild(Node("Harald", "Lotte"))

frederikke = Node("Frederikke")
frederikke.addChild(Node("Bodil", "Frederikke"))
frederikke.addChild(Node("Svend", "Frederikke"))
amalie = Node("Amalie", "Frederikke")
frederikke.addChild(amalie)
birgitte = Node("Birgitte", "Amalie")
amalie.addChild(birgitte)
birgitte.addChild(Node("Åge", "Birgitte"))
birgitte.addChild(Node("Karl", "Birgitte"))

print(esther.oldestParent("Esther"))
print(lotte.oldestParent("Lotte"))

print(esther.isInFamily("Esther", "Lotte"))

print(amalie.oldestParent("Amalie"))
print(lotte.oldestParent("Lotte"))

print(esther.isInFamily("Amalie", "Bent"))


