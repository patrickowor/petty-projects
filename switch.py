class case():
    def __init__(self,value,when=None,final=None):
        self.val = value
        if when != None:
            self.when(when)
        if final != None:
            self.final(final)
    def final(self,args):
        exec(args)
    def  when(self, dic):
        self.dic = dic
        if  type(self.dic) != type({'a':'b'}):
            raise TypeError('supply a dictionary value')
        for self.single in self.dic:
            if type(self.val) == type(1):
                self.n_val = str(self.val)
            else:
                self.n_val = self.val
            if self.single == self.n_val:
                exec(self.dic[self.single])
                break
print(dir(case))      
a = case('1',
when={
    '1': 'a = 6; print(a)' },final = '#print(a)'
)

     