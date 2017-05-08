from data_ import data_

class Func_(data_):
    def __init__(self, name, type, value = None):
        self.params_num = 0
        self.call_params = {}
        self.children = []
        return super(Func_, self).__init__(name, type, value)

    def __str__(self):
        return str(self.name)

    def __iter__(self):
        return iter(self.children)

    @property
    def get_call_params(self):
        return self.call_params

    @property
    def set_call_params(self,cal_):
        self.call_params = cal_

    @property
    def add_child(self,param_):
        self.children.append(param_)

    def merge_children(self):
        self.call_params=dict(zip(self.value,self.children))

    @property
    def hasChildren(self):
        return (len(self.children) != 0)


def walk_tree_df_preorder(dict_,node,list_):
    if isinstance(list_,list):
        list_.append(node)
    if isinstance(node,Func_):
        for child in node.children:
            walk_tree_df_preorder(child,list_)

# def walk_tree_df_postorder(node, visit):
#     for child in node.children:
#         walk_tree_df_preorder(child, visit)
#     visit(node)

# def walk_tree_bf(node, visit):
#     to_visit = [node]
#     while to_visit:
#         new_to_visit = []
#         for node in to_visit:
#             visit(node)
#             new_to_visit.extend(node.children)
#         to_visit = new_to_visit
#
# def walk_tree_bf_gen(node):
#     if isinstance(node,Tree):
#         to_visit = [node]
#         while to_visit:
#             new_to_visit = []
#             for node in to_visit:
#                 yield  len(to_visit)
#                 yield node
#                 new_to_visit.extend(node.children)
#             to_visit = new_to_visit
