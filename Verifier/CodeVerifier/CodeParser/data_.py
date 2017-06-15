class data_(object):
    def __init__(self,name,value=None):
        self.name= name
        self.value = value
        self.sub = []


    def __str__(self):
        return self.name

    @property
    def set_value(self,val):
        self.value = val

    @property
    def get_value(self):
        return self.value

    def set_sub(self,node):
        self.sub.append(node)

    @property
    def get_sub(self):
        return self.sub


class Var_(data_):
    def __init__(self, name, value = None):
        return super(Var_, self).__init__(name, value)

    @property
    def set_alter(self,data):
        self.alter_ = data

        
class Const_(data_):
    def __init__(self, name, value = None):
        return super(Const_, self).__init__(name, value)



