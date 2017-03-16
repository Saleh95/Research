from Tree import *
from parse_eval import *
from  parse_declaration import *

class Processor:
    def __init__(self,forest_,declarations_):
        self.data_ = forest_
        self.declarations_ = declarations_
        self._comparables=[]
        self._elems=[]
        self.model = ""
        print str(self.declarations_)


    def build_list(self):
        for elm in self.data_:
            list_=[]
            walk_tree_df_preorder(elm,list_)
            self._comparables.append(list_)

    def build_model(self,arg_1,arg_2):
        if isinstance(arg_1,data_) and isinstance(arg_2,data_):
            if arg_1.get_type == arg_2.get_type:
                self.model += str(arg_1) + " can be equal " + str(arg_2) +"\n"
            elif arg_1.get_type == "var" and arg_2.get_type == "const":
                self.model += str(arg_1) + " can be equal " + str(arg_2) +"\nwhen "+str(arg_1.value)+"\nequals "+str(arg_2.value)+"\n"
    @property
    def get_model(self):
        return self.model

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
                        print self.declarations_[str(ch_1[k])].get_type
                        if isinstance(self.declarations_[str(ch_1[k])],data_) and isinstance(self.declarations_[str(ch_2[k])],data_):
                            if self.declarations_[str(ch_1[k])] != None and self.declarations_[str(ch_2[k])] != None:
                                if (self.declarations_[str(ch_1[k])].get_type == self.declarations_[str(ch_2[k])].get_type) or (self.declarations_[str(ch_1[k])].get_type == "const" and self.declarations_[str(ch_2[k])].get_type == "var" )or (self.declarations_[str(ch_2[k])].get_type == "const" and self.declarations_[str(ch_1[k])].get_type == "var"):
                                    self.build_model(self.declarations_[str(ch_1[k])],self.declarations_[str(ch_2[k])])
                                else:
                                    return False
                    j+=1
            i+=1
          
        return True

    def compare_trees(self):
        self.build_list()
        if self.compare_items():
            print "Acceptable"
        else:
            print "Failure"