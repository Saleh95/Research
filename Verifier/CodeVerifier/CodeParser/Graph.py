from data_ import *
class Graph:
    def __init__(self,dec_):
        self.declarations=dec_
        self.graph={}
        self.gen_graph()

    def gen_graph(self):
        for k in self.declarations:
            if isinstance(self.declarations[k],data_):
                self.graph[k]=self.declarations[k].get_sub

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.graph.has_key(start):
            return None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath: return newpath
        return None