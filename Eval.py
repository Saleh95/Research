from Logic_Processor import *
from parse_declaration import *
if __name__ == '__main__':
    input_=""
    dat_=""
    print "Initialize:\n"
    while input_ != "done;":
        input_ = raw_input()
        if input_ != "done;" and input_ != "":
            dat_ += input_
    var = parse_declaration(dat_)
    declarations_ = var.parse_code()
    print str(declarations_)
    code_ = ""
    input_=""
    while input_ != "run;":
        input_ = raw_input()
        if input_ != "run;" and input_ != "":
            code_ += input_
    code =""
    for s in code_:
        if s != " " and s!="\n":
            code +=s
    code_list = code.split(";")
    for snip_ in code_list:
        g = ParseGen(declarations_)
        data_ = g.get_data(snip_)
        p = LogicProcessor(data_,declarations_)
        print "Equation: " + snip_
        p.compare_trees()


    
  

