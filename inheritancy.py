'''
single
multilevel
multiple
hierachical 

'''

# class parent():
#     def output(self):
#         print("i'm the parent class")
# class child(parent):
#     def outputc(self):
#         print("i'm the child class")  
# c=child()
# c.outputc()
# c.output()        

# class grandfather():
#     def outputgf(self):
#         print("i'm the grandfather class")
# class parent(grandfather):
#     def output(self):
#         print("i'm the parent class")
# class child(parent):
#     def outputc(self):
#         print("i'm the child class")  
# c=child()
# c.outputc()
# c.output() 
# c.outputgf()

# class father():
#     def outputgf(self):
#         print("i'm the father class")
# class mother():
#     def output(self):
#         print("i'm the parent class")
# class child(father,mother):
#     def outputc(self):
#         print("i'm the child class")  
# c=child()
# c.outputc()
# c.output() 
# c.outputgf()

class father():
    def outputgf(self):
        print("i'm the father class")
class child1(father):
    def output(self):
        print("i'm the child1 class")
class child2(father):
    def outputc(self):
        print("i'm the child2 class")  
c=child1()
c2=child2()
c.output() 
c.outputgf()
c2.outputc()
c2.outputgf()
