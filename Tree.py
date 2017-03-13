class Tree(object):
    """Generic tree."""
    def __init__(self, name='', children=None):
        self.name = name
        if children is None:
            children = []
        self.children = children
    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return self(self.name)

    def add_child(self,child):
        self.children.append(child)

    def __iter__(self):
        return iter(self.children)



def walk_tree_df_preorder(node,list_):
    if isinstance(list_,list):
        list_.append({str(node):node,"children":node.children,"Length":len(node.children)})
    for child in node.children:
        walk_tree_df_preorder(child,list_)

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

#def compare_trees(tree1,tree2):
#    print "Hey"
#    tree_list1=[]
#    tree_list2=[]
#    tree_list1.append(walk_tree_df_preorder(tree1))
#    tree_list2.append(walk_tree_df_preorder(tree2))
#    print str(len(tree_list1))
#    if len(tree_list1) != len(tree_list2):
#        return "Not equal"

#    else:
#        for i in range(len(tree_list1)):
#            if tree_list1[i]!=tree_list2[i]:
#                return "Not equal"

#    return "They are equal"

