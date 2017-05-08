class data_:
    def __init__(self,name,type,value=None):
        self.name= name
        self.type = type
        self.value = value
        self.sub = []


    def __str__(self):
        return self.name

    @property
    def get_type(self):
        return self.type

    @property
    def set_value(self,val):
        self.value = val

    @property
    def get_value(self):
        return self.value

    @property
    def set_sub(self,node):
        self.sub.append(node)

    @property
    def get_sub(self):
        return self.sub



class Var_(data_):
    def __init__(self, name, type, value = None):
        return super(Var_, self).__init__(name, type, value)

    @property
    def set_alter(self,data):
        self.alter_ = data

        
class Const_(data_):
    def __init__(self, name, type, value = None):
        return super(Const_, self).__init__(name, type, value=self)



