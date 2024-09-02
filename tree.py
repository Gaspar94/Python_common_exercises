from treelib import Node, Tree
from enum import Enum

class Tags(Enum):
    FUSA = 1
    FFI = 2
    QM = 3

class Component:
    target = "my path"
    tag = Tags

    def __init__(self, target, tag):
        self.target = target
        self.tag = tag
        self.children = []

    def addchild(self,child):
        self.children.append(child)
    def getChildrenList(self):
        return self.children

son1 = Component('SWCs1', "FUSA")
son1.addchild('aa')
son2 = Component('SWCs1', "FFI")
son2.addchild('bb')
son3 = Component('SWCs1', "QM")
son3.addchild('cc')
father = Component("SafeCoding", 'FUSA')
sons = [son1,son2,son3]
for son in sons:
    father.addchild(son)

"""print(son1.getChildrenList())
print(father.getChildrenList())
"""

tree = Tree()
tree.create_node("SafeCoding", "SafeCoding")
new_nodes = ["node1","node2","node3"]
for node in new_nodes:
    tree.create_node(node, node, parent="SafeCoding")

tree.show()