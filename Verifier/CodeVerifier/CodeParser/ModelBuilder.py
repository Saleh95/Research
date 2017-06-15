from Sub_Tree import *
from Tree import *

class ModelBuilder:
    def __init__(self,data,sub_tree):
        self._data = data
        self._tree = sub_tree
        self._node = None
        self._res = []

    def build_model(self):
        self._node = Sub(self._data)
        p=1
        for elem in self._tree:
            self._node.add_sub(elem,p)
            p+=1
            if isinstance(elem,Tree):
                if elem.hasChildren:
                    self.build_sub_model(elem)

    def build_sub_model(root,elem):
        list_=[]
        sub_list = []
        walk_tree_df_preorder(elem,list_)
        p=1
        for elm in list_:
            print str(elem)
            sub = Sub(elem,p)
            p+=1
            sub_list.append(sub)

        root.add_sub_tree(sub_list)
    
     
    def query_model(self,parent):
        if isinstance(parent,Sub):
            if parent.children.isEmpty:
                return self._res
            self._res.append(str(parent))
            return self.query_model(parent.get_Head())

    def define_model(self):
        print "What!!"
        self.query_model(self._node)
        print "I am the node"
        print str(self._node.children)
        return str(self._res)