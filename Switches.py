class switch:
    def __init__(self):
        self.cases = []
        self.triggered = False
    def anyCase(self,func,*args):
        if(len(args) <= 1): args += tuple([False])
        for i in args:
            if(args[i] and not self.triggered):
                self.triggered = True
                func()
    def exclusiveCase(self,func,*args):
        if(len(args) <= 1): args += tuple([False])
        numOfExepts = 0
        for i in args:
            if(args[i] and not self.triggered):
                numOfExepts += 1
        
        if(numOfExepts == len(args)):
            self.triggered = True
            func()
    def default(self,func):
        if(not self.triggered):
            func()
