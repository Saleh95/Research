from Tree import *
from parse_eval import *
from  parse_declaration import *
from ModelBuilder import *
from Processor import *

class LogicProcessor:
    def __init__(self,forest_,declarations_):
        self.data_ = forest_
        self.declarations_ = declarations_
        self._comparables=[]
        self._elems=[]
        self.model = ""
        self.prc=Processor(declarations_)


    def build_list(self):
        for elm in self.data_:
            list_=[]
            walk_tree_bf(elm,list_)
            print str(list_)
            self._comparables.append(list_)

    def print_list(self):
        for elm in self._comparables:
            print ','.join(str(v) for v in elm)

    def get_smaller(self,arg_1,arg_2):
        if len(arg_1)<len(arg_2):
            return len(arg_1)
        return len(arg_2)


    def compare_trees(self):
        accepted=False
        self.build_list()
        self.print_list()
        i=0
        while i+1 <len(self._comparables):
            sm=self.get_smaller(self._comparables[i],self._comparables[i+1])
            for j in range(sm):
                accepted=self.prc.build_edges(self._comparables[i][j],self._comparables[i+1][j])
                if not accepted:
                    print "They can't be equal"

            print "smmmmm"
            check=self.prc.nested_edges()
            print str(check)
            if check and accepted:
                print "They can be equal"
                self.prc.get_model()
            else:
                print "They can't be equal"

            i += 1