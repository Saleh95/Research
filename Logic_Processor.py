from Tree import *
from parse_eval import *
from  parse_declaration import *
from ModelBuilder import *

class Processor:
    def __init__(self,forest_,declarations_):
        self.data_ = forest_
        self.declarations_ = declarations_
        self._comparables=[]
        self._elems=[]
        self.model = ""


    def build_list(self):
        for elm in self.data_:
            print str(elm)
            list_=[]
            walk_tree_df_preorder(elm,list_)
            print str(list_)
            self._comparables.append(list_)

    def print_list(self):
        for elm in self._comparables:
            for el in elm:
                print el

    def build_model(self,arg_1,arg_2):
        acceptable = False
        var = None
        cross = None
       
        if isinstance(arg_1,data_) and isinstance(arg_2,data_):
            if arg_1.get_type == arg_2.get_type and arg_1.name == arg_2.name:
                acceptable = True
            elif arg_1.get_type == arg_2.get_type and arg_1.name != arg_2.name and arg_1.value == arg_2.value:
                acceptable = True
            elif arg_1.get_type == "var" and (arg_2.get_type == "const" or arg_2.get_type == "func"):
                acceptable = True
                var = arg_1
                cross = arg_2
            elif arg_2.get_type == "var" and (arg_1.get_type == "const" or arg_1.get_type == "func"):
                var = arg_2
                cross = arg_1

        if acceptable and var!= None and cross != None:
            return model_handler(var,cross)
        else:
            return acceptable

    
    def getComparables(self):
        for item in self._comparables:
            print str(item)
  
    def model_handler(self,args_1,args_2):
        model_ = ModelBuilder(args_1,args_2)
        model_.build_model()
        return model_.define_model()
               
    @property
    def get_model(self):
        return self.model

    def compare_items(self):
        pass

    def compare_trees(self):
        self.build_list()
        self.getComparables()
        i=0
        while i and i+1 in range(len(self.data_)):
            if self.data_[i] != self.data_[i+1]:
                print "Failure"
                return
        if self.compare_items():
            print "Acceptable"
        else:
            print "Failure"