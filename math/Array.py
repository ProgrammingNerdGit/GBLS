class Array2D:
    def __init__(self,lx,ly,default = None):
        self.data = []
        self.width = lx
        self.height = ly
        for _ in range(lx):
            acm = []
            for __ in range(ly):
                acm.append(default)
            self.data.append(acm)
    def __getitem__(self,x):
        return self.data[x[0]][x[1]]
    def __setitem__(self,x,val):
        self.data[x[0]][x[1]] = val
    def __eq__(self,other):
        return self.data == other.data
    def find(self,regex):
        vals = []
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                v = self.__getitem__((x,y))
                if(v == regex):
                    vals.append((x,y))
        return vals
    def replace(self,regex,val):
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                v = self.__getitem__((x,y))
                if(v == regex):
                    self.__setitem__((x,y),val)
    
        
