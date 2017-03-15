class data_(object):
    def __init__(self,name,type,value=None):
        self.name= name
        self.type = type
        self.value = value

    @property
    def get_type(self):
        return self.type

    @property
    def set_value(self,val):
        self.value = val

class Var_(data_):
    def __init__(self, name, type, value = None):
        self.alter_ = None
        return super(Var_, self).__init__(name, type, value)

    @property
    def set_alter(self,data):
        self.alter_ = data

class Func_(data_):
    def __init__(self, name, type, value = None):
        self.params_num = 0
        self.params_type =''
        self.params_ = []
        self.call_params = []
        return super(Func_, self).__init__(name, type, value)

    @property
    def set_params(self,parms_):
        self.params_ = params_

    @property
    def get_parms(self):
        return self.params_

    @property
    def get_call_params(self):
        return self.call_params

    @property
    def set_call_params(self,cal_):
        self.call_params = cal_

    def is_valid(self,data):
        if isinstance(data,data_):
            if data.get_type == "func" or data.get_type == self.get_type:
                return True
            else:
                return False
    
        
class Const_(data_):
    def __init__(self, name, type, value = None):
        return super(Const_, self).__init__(name, type, value=self)



