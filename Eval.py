from multiprocessing import Process
import threading
from Tree import *
from parse_eval import *

class Processor:
    def __init__(self,forest_):
        self.data_ = forest_
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
                    if self._comparables[i][j]["Children"] != self._comparables[i+1][j]["Children"]:
                        pass
                    j+=1
            i+=1
          
        return True

    def compare_trees(self):
        self.build_list()
        self.compare_items()

         
    

if __name__ == '__main__':
    g = ParseGen()
    #roots = g.get_data(str(raw_input("Enter data\n")))
    #compare_trees(roots[0],roots[1])
    data_ = g.get_data(str(raw_input("Enter data\n")))
    p = Processor(data_)
    p.compare_trees()
    #print "Iam data "
    #struct_=[]
    #for elm in data_:
    #    print str(elm)
    #    list_=[]
    #    walk_tree_df_preorder(elm,list_)
    #    struct_.append(list_)
    
    #for l in struct_:
    #    print str(l)+"\n"
    #proc = Processor(data_)
    #proc_= Process(target=proc.compare_trees)
    #proc_.start()
    #proc_.join()

