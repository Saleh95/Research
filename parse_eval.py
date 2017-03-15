from pyparsing import *
from Tree import Tree,walk_tree_bf_gen, walk_tree_df_preorder
import string
from multiprocessing import Pool

class ParseGen:
    def __init__(self):
        self.enclosed = Forward()
        self.nestedParens = nestedExpr('(', ')', content=self.enclosed)
        self.nestedBrackets = nestedExpr('[', ']', content=self.enclosed)
        self.nestedCurlies = nestedExpr('{', '}', content=self.enclosed)
        self.data_list = []
        self.data_tree = []
        self.data_root = []
        self.roots = []
        self.tree_dict = {}


    def gen_init(self):
        self.enclosed << (Word(alphas) | ',' | self.nestedParens | self.nestedBrackets | self.nestedCurlies)


    def gen_data(self,data):
        str(data).replace(" ","") # trim spaces and new lines
        print  data
        self.data_list = str(data).split("=")

        j=0
        for j in range(len(self.data_list)):
            self.data_list[j].strip()
            end = self.data_list[j].find("(")
            gam = self.data_list[j][:end]
            print "gamma" + str(end)
            print gam
            self.roots.append(gam)
            self.data_list[j] = self.data_list[j][end:]
            print self.data_list[j]
        for dt in self.data_list:
            alpha= self.enclosed.parseString(dt).asList()
            print alpha
            self.data_tree.append(alpha)



    def build_tree(self,data, t):
        if data:
            # print t
            ch_ = None
            for val in data:
                if not isinstance(val, list) and str(val) != ',':
                    # print val
                    if t == None:
                        t = Tree(val)
                    else:
                        ch_ = Tree(val)
                        t.add_child(ch_)

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
        print str(len(self.data_tree))
        i=0
        for x in self.data_tree:
            t = Tree(self.roots[i])
            self.build_tree(x,t)
            self.data_root.append(t)
            i+=1

        return self.data_root

    def solve_equality(self):
        for root in self.data_root:
            walk_tree_df_preorder(root)



# g = ParseGen()

# g.get_data(str(raw_input("Enter data\n")))

# g.solve_equality()













