class Tree(object):
    """Generic tree."""
    def __init__(self, name='', children=None):
        self.name = name
        if children is None:
            children = []
        self.children = children
    def __str__(self):
        return str(self.name)

    def add_child(self,child):
        self.children.append(child)



def walk_tree_df_preorder(node):
    print node
    print str(len(node.children))
    for child in node.children:
        walk_tree_df_preorder(child)

def walk_tree_df_postorder(node, visit):
    for child in node.children:
        walk_tree_df_preorder(child, visit)
    visit(node)

def walk_tree_bf(node, visit):
    to_visit = [node]
    while to_visit:
        new_to_visit = []
        for node in to_visit:
            visit(node)
            new_to_visit.extend(node.children)
        to_visit = new_to_visit

def walk_tree_bf_gen(node):
    if isinstance(node,Tree):
        to_visit = [node]
        while to_visit:
            new_to_visit = []
            for node in to_visit:
                yield  len(to_visit)
                yield node
                new_to_visit.extend(node.children)
            to_visit = new_to_visit