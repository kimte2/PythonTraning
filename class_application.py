class Calculation:
    value = 0
    def square(self):
        s = self.value * self.value
        return s
    def tri(self):
        y = self.value * self.value * self.value
        return y

calcs = [Calculation(),Calculation(),Calculation()]
calcs2 = Calculation()
calcs2.value = 2
print calcs2.tri()
print calcs2.square()

#cal = [Caluculationses(),Caluculationses(),Caluculationses()]

#calcs[0].value = 3
#calcs[1].value = 5
#calcs[2].value = 7
#cal[0].value = 3
#cal[1].value = 4
#cal[2].value = 5

#print calcs[0].square()
#print calcs[1].square()
#print calcs[2].square()
#print calcs[0].tri()
#print calcs[1].tri()
#print calcs[2].tri()

#for c in calcs:
#    print c.square()
#    print c.tri()





