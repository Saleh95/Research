from Tree import *
from parse_eval import *
from  parse_declaration import *

class Processor:
    def __init__(self,forest_,declarations_):
        self.data_ = forest_
        self.declarations_ = declarations_
        self._comparables=[]
        self._elems=[]


    def build_list(self):
        for elm in self.data_:
            list_=[]
            walk_tree_df_preorder(elm,list_)
            self._comparables.append(list_)

    def compare_items(self):
        i=0
        while i<len(self._comparables) and i+1 <len(self._comparables):
            if len(self._comparables[i]) != len(self._comparables[i+1]):
                return False
            else:
                j=0
                while j<len(self._comparables[i]):
                    if self._comparables[i][j]["Length"] != self._comparables[i+1][j]["Length"]:
                        return False
                    ch_1 = self._comparables[i][j]["children"]
                    ch_2 = self._comparables[i+1][j]["children"]

                    for k in range(len(ch_1)):
                        if self.declarations_[str(ch_1[k])] != None and self.declarations_[str(ch_2[k])] != None:
                            if (self.declarations_[str(ch_1[k])].get_type == self.declarations_[str(ch_2[k])].get_type) or (self.declarations_[str(ch_1[k])].get_type == "const" and self.declarations_[str(ch_2[k])].get_type == "var") or (ch_2[k].get_type == "const" and self.declarations_[str(ch_1[k])].get_type == "var"):
                                continue
                            else:
                               return False
                    j+=1
            i+=1
          
        return True

    def compare_trees(self):
        self.build_list()
        if self.compare_items():
            print "Acceptable"