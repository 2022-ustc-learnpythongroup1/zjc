'''
class USTC1958combo:
    name=''
    price = 0
    count=0
    def __init__self(self,id,p):
        self.name=id
        self.price=p
    def combo(self):
        print("%s:%d RMB"%(self.name,self.price))
    def sep(self):
        self.counter+=1
        print("您的单号是：%d"%(self.name,self.price))


class studentComb(USTC1958combo):
    discount=1
    def __init__self(self,id,p):
        USTC1958combo.__init__(self,id,p):
        self.discount=d
    def combo(self):
        print("%s:%d RMB"%(self.name,self.price))
    def sep(self):
        self.counter+=1
        print("您的单号是：%d"%(self.name,self.price))
'''
