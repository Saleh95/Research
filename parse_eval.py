from pyparsing import *
from Tree import walk_tree_df_preorder
import string
from multiprocessing import Pool
from parse_declaration import *
import copy

class ParseGen:
    def __init__(self,declarations):
        self.enclosed = Forward()
        self.nestedParens = nestedExpr('(', ')', content=self.enclosed)
        self.nestedBrackets = nestedExpr('[', ']', content=self.enclosed)
        self.nestedCurlies = nestedExpr('{', '}', content=self.enclosed)
        self.data_list = []
        self.data_tree = []
        self.data_root = []
        self.roots = []
        self.tree_dict = {}
        self.ptrs = declarations

    def gen_init(self):
        self.enclosed << (Word(alphas) | ',' | self.nestedParens | self.nestedBrackets | self.nestedCurlies)


    def gen_data(self,data):
        str(data).replace(" ","") # trim spaces and new lines
        self.data_list = str(data).split("=")

        for j in range(len(self.data_list)):
            self.data_list[j].strip()
            end = self.data_list[j].find("(")
            gam = self.data_list[j][:end]
            self.roots.append(gam)
            self.data_list[j] = self.data_list[j][end:]

        for dt in self.data_list:
            try:
                alpha= self.enclosed.parseString(dt).asList()
                print str(alpha)
            except:
                break
            self.data_tree.append(alpha)

    def build_tree(self,data, t):
        if data:
            ch_ = None
            for val in data:
                if not isinstance(val, list) and str(val) != ',':
                    try:
                        if t == None:
                            t = self.ptrs[val]
                            print 't'+str(t)
                        else:
                            ch_ = copy.deepcopy(self.ptrs[val])
                            if isinstance(t,Func_):
                                t.add_child(ch_)
                            print 'ch'+str(ch_)

                    except KeyError:
                        print str(self.ptrs[val])
                elif isinstance(val, list):
                    if not ch_:
                        ch_ = t
                    self.build_tree(val, ch_)

                elif str(val) == ',' or str(val) == ' ' or str(val) == '\n':
                    continue
                else: 
                    self.build_tree(val, ch_)


    def get_data(self,data):
        self.gen_init()
        self.gen_data(data)
        i=0
        for x in self.data_tree:
            try:
                t = copy.deepcopy(self.ptrs[str(self.roots[i])])
                self.build_tree(x,t)
                if isinstance(t,Func_):
                    t.merge_children()
                self.data_root.append(t)
            except KeyError:
                pass
            i+=1
        return self.data_root
