from parse_eval import *
from data_ import *

class parse_declaration:
    def __init__(self,code_data):
        self._code=code_data
        self._code_list = []
        self._declarations = {}

    def declare_functions(self,line_):
        n_line = str(line_).split(":")[1]
        str_ = ""
        name_ = ""
        i=0
        while n_line[i] != '(' and i<len(n_line):
            name_ += n_line[i]
            i+=1
        n_line= n_line[i:]
        for j in range(len(n_line)):
            if n_line[j] != ' ' and n_line[j] != '(' and n_line[j]!= ')':
                str_ += n_line[j]

        func_list = str_.split(",")
        self._declarations[name_]=Func_(name_,"func",func_list)
        print str(func_list)


    def declar_vars(self,line_):
        n_line = str(line_).split(":")[1]
        str_ = ""
        for j in range(len(n_line)):
            if n_line[j] != ' ':
                str_ += n_line[j]
        vars_ = str_.split(",")
        for s in str_:
            self._declarations[s] = Var_(s,"var")
        
    def declare_consts(self,line_):
         n_line = str(line_).split(":")[1]
         str_ = ""
         for s in n_line:
             str_ +=s
         
         consts_ = str_.split(",")

         for c in consts_:
             al_ = str(c).split("=")
             self._declarations[c[0]] = Const_(c[0],"const",c[1])

         print "lolll"



    def parse_code(self):
        print "whatever"
        self._code_list = str(self._code).split(";")
        print str(self._code_list)
        for line_ in self._code_list:
            try:
                print line_
                if "func" in line_:
                    self.declare_functions(line_)
                elif "var" in line_:
                    self.declar_vars(line_)
                else:
                    self.declare_consts(line_)
            except Exception:
                continue
        return self._declarations
