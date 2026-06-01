class demo():
    def __init__(self,a,b):
        self. __a=a #private
        self. _b=b #protected
class demo2(demo):
    def output(self):
        print(self. _b)
d=demo2(3,4)
d.output()        
