from data_ import *
from Tree import *
from Graph import *

class Processor:
    def __init__(self,declarations):
        self.graph=Graph(declarations)
        self.covered={}

    def has_elm(self,arg_1,arg_2):
        if len(arg_1.get_sub) != 0:
            for elm in arg_1.get_sub:
                if isinstance(elm, Func_):
                    print "llll"
                    for v in elm.children:
                        if v != arg_2:
                            arg_1.set_sub(arg_2)
                            return True
        return False

    def build_edges(self,arg_1,arg_2):
        if isinstance(arg_1, data_) and isinstance(arg_2, data_):
            if isinstance(arg_1,Func_) and isinstance(arg_2,Func_) and arg_1.name != arg_2.name:
                print "Fail 1"
                return False

            elif isinstance(arg_1,Func_) and isinstance(arg_2,Func_):
                for k,v in arg_1.get_call_params.iteritems():
                    self.build_edges(arg_1.get_call_params[k],arg_2.get_call_params[k])

            elif isinstance(arg_1,Var_):
                if not(self.has_elm(arg_1,arg_2)):
                    arg_1.set_sub(arg_2)

            elif isinstance(arg_1,Const_) and isinstance(arg_2,Const_):
                if arg_1.get_value != arg_2.get_value:
                    return False

                else:
                    arg_1.set_sub(arg_2)
                    arg_2.set_sub(arg_1)

            self.covered[str(arg_1)] = arg_1.get_sub
            print str(arg_1)+"="+','.join(str(elm) for elm in arg_1.get_sub)
            return True

    def nested_edges(self):
        for k,v in self.covered.iteritems():
            if len(v)>1:
                for i in range(len(v)):
                    print  "1st"+str(v[i])
                    print "2nd"+str(v[i+1])
                    accepted = self.build_edges(v[i],v[i+1])
                    if not accepted:
                        print "Fail here"
                        return False

        return True

    def get_model(self):
        print str(self.covered)
        for k,v in self.covered.iteritems():
            print str(k)+"="+','.join(str(elm) for elm in v)
