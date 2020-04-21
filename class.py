class IntSet(object):
    def __init__(self):
        self.vals = []
    
    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)
    
    def member(self, e):
        return e in self.vals
    
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def getMembers(self):
        return self.vals[:]
    
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'  # -1 omits the trailing comma
