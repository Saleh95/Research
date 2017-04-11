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
            list_=[]
            walk_tree_df_preorder(elm,list_)
            self._comparables.append(list_)

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
        i=0
        while i<len(self._comparables) and i+1 <len(self._comparables):
            print str(len(self._comparables[i])) +':'+ str(len(self._comparables[i+1]))
            if len(self._comparables[i]) != len(self._comparables[i+1]):
                print str(len(self._comparables[i])) +':'+ str(len(self._comparables[i+1]))
                return False
            else:
                j=0
                while j<len(self._comparables[i]):
                    if self._comparables[i][j]["Length"] != self._comparables[i+1][j]["Length"]:
                        return False
                    ch_1 = self._comparables[i][j]["children"]
                    ch_2 = self._comparables[i+1][j]["children"]

                    for k in range(len(ch_1)):
                        print str(ch_1[k]) +':'+ str(ch_2[k])
                        if isinstance(self.declarations_[str(ch_1[k])],data_) and isinstance(self.declarations_[str(ch_2[k])],data_):
                            if self.declarations_[str(ch_1[k])] != None and self.declarations_[str(ch_2[k])] != None:
                                if (self.declarations_[str(ch_1[k])].get_type == self.declarations_[str(ch_2[k])].get_type) or (self.declarations_[str(ch_1[k])].get_type == "const" and self.declarations_[str(ch_2[k])].get_type == "var" )or (self.declarations_[str(ch_2[k])].get_type == "const" and self.declarations_[str(ch_1[k])].get_type == "var") or (self.declarations_[str(ch_1[k])].get_type == "const" and self.declarations_[str(ch_2[k])].get_type=="func"):
                                    self.build_model(ch_1[k],ch_2[k])
                                else:
                                    return False
                    j+=1
            i+=1
          
        return True

    def compare_trees(self):
        self.build_list()
        i=0
        while i and i+1 in range(len(self.data_)):
            if self.data_[i] != self.data_[i+1]:
                print "Failure"
                return
        if self.compare_items():
            print "Acceptable"
        else:
            print "Failure"