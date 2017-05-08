from data_ import *
from Tree import *
from Graph import *

class Processor:
    def __init__(self,declarations):
        self.graph=Graph(declarations)
        self.covered={}

    def build_edges(self,arg_1,arg_2):
        if isinstance(arg_1, data_) and isinstance(arg_2, data_):
            if arg_1.get_type=="func" and arg_2.get_type=="func" and arg_1.name != arg_2.name:
                return False

            elif isinstance(arg_1,Func_) and isinstance(arg_2,Func_):
                for k in arg_1.get_call_params:
                    self.build_edges(arg_1.get_call_params[k],arg_2.get_call_params[k])

            elif arg_1.get_type=="var":
                arg_1.set_sub(arg_2)

            elif arg_1.get_type=="const" and arg_2.get_type=="const":
                if arg_1.get_value != arg_2.get_value:
                    return False

                else:
                    arg_1.set_sub(arg_2)
                    arg_2.set_sub(arg_1)

            self.covered[str(arg_1)] = arg_1.get_sub
            return True

    def nested_edges(self):
        for k in self.covered:
            if isinstance(self.covered[k],data_):
                if len(self.covered[k].sub)>1:
                    for i in range(len(self.covered.sub)):
                        accepted = self.build_edges(self.covered.sub[i],self.covered.sub[i+1])
                        if not accepted:
                            return False

                return True


    def get_model(self):
        for k in self.covered:
            print str(self.covered[k])