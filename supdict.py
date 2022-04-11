class supdict:
    def __init__(self, val):
        self.val = val
        self._val_keys = list(val.keys())
        for keys in self._val_keys:
            self. __dict__[keys] = self.val[keys]
    def beautify(self):
        self.__beau = str(self.val)
        self.__beau = self.__beau.replace(',',',\n')   
        self.__beau = self.__beau.replace('[','[\n')   
        self.__beau = self.__beau.replace(']',']\n') 
        self.__beau = self.__beau.replace('{','{\n')   
        self.__beau = self.__beau.replace('}','}\n')   
        self.__beau = self.__beau.replace(')',')\n')
        self.__beau = self.__beau.replace('(',')\n')   
        print(self.__beau)
            
            
a = {'abs':12,'ads':[1,2,3],'hope':(1,2,3,4,)}
a = supdict(a)
a.beautify()


