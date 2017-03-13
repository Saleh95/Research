from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager

class GetSetter(object):
    def __init__(self):
        self.var = None

    def set(self, value):
        self.var = value

    def get(self):
        return self.var


class ChildClass(GetSetter):
    pass

class ParentClass(GetSetter):
    def __init__(self):
        self.child = ChildClass()
        GetSetter.__init__(self)

    def getChild(self):
        return self.child


def change_obj_value(obj):
    obj.set(100)
    obj.getChild().set(100)


if __name__ == '__main__':
    BaseManager.register('ParentClass', ParentClass)
    manager = BaseManager()
    manager.start()
    inst2 = manager.ParentClass()

    p2 = Process(target=change_obj_value, args=[inst2])
    p2.start()
    p2.join()

    print inst2                    # <__main__.ParentClass object at 0x10cf82350>
    print inst2.getChild()         # <__main__.ChildClass object at 0x10cf6dc50>
    print inst2.get()              # 100
    #good!

    print inst2.getChild().get()   # None
    #bad! you need to register child class too but there's almost no way to do it
    #even if you did register child class, you may get PicklingError :)