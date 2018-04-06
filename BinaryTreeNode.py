class BinaryTreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        if left == None:
            self.left = None
        else:
            self.left = BinaryTreeNode(left)
        
        if right == None:
            self.rite = None
        else:
            self.rite = BinaryTreeNode(right)

    def __str__(self):
        if (self.left == None) and (self.rite == None):
            return str(self.val)
        return str(self.val) + ' -> ( ' + str(self.left) + ', ' + str(self.rite) + ' )'
    
    def getVal(self):
        return self.val

    def getLeft(self):
        return self.left

    def getRite(self):
        return self.rite

    def setLeft(self, val):
        self.left = val
    
    def setRite(self, val):
        self.rite = val

    def DFS(self):
        stack = Stack()
        q = [self]
        rlst = []
        while (len(q) != 0):
            ftree = q.pop()
            subs = [ftree.getRite(), ftree.getLeft()]
            rlst.append(ftree.val)
            for sub in subs:
                if sub != None:
                    q.append(sub)
        return rlst
        
    def BFS(self):
        stack = Stack()
        q = [self]
        rlst = []
        while (len(q) != 0):
            ftree = q.pop(0)
            subs = [ftree.getLeft(), ftree.getRite()]
            rlst.append(ftree.val)
            for sub in subs:
                if sub != None:
                    q.append(sub)
        return rlst
        
    def MSS(self):
        q = [self, 'enddepth']
        rlst = [] 
        blst = []
        revbool = False
        while (len(q) != 0):
            ftree = q.pop(0)
            if ftree == 'enddepth':
                if revbool:
                    blst.reverse()
                rlst = rlst + blst
                blst = []
                revbool = not revbool
                if len(q) > 0:
                    q.append('enddepth')
            else:
                subs = [ftree.getLeft(), ftree.getRite()]
                blst.append(ftree.getVal())
                for sub in subs:
                    if sub != None:
                        q.append(sub)
        return rlst
            
