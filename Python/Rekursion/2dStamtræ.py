class Node:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)
        self.children[-1].addParent(self)

    def addParent(self, obj):
        self.parents.append(obj)

    def displayDescendants(self):
        print('(', end='')
        for c in self.children:
            # Basic case
            print(c.name + ' ', end='')
            # Recursive case
            c.displayDescendants()
        print(') ', end='')


esther = Node("Esther")
bent = Node("Bent")
esther.addChild(bent)
emma = Node("Emma")
esther.addChild(emma)
erna = Node("Erna")
esther.addChild(erna)
lotte = Node("Lotte")
erna.addChild(lotte)
hugo = Node("Hugo")
lotte.addChild(hugo)
harald = Node("Harald")
lotte.addChild(harald)

esther.displayDescendants()

frederikke = Node("Frederikke")
esther.addParent(frederikke)

frederikke.displayDescendants()
