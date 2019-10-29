#传入两个点的信息作为实参，传入一个移动信息，生成移动后点的位置，以及当前这两个点的直线距离
from math import sqrt
class Piont():
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def Move_By(self,dx,dy):
        self.dx = dx
        self.dy = dy

    def Move_To(self):
        a = self.x + self.dx
        b = self.y + self.dy
        global num
        num= []
        num.append(a)
        num.append(b)
        return num

    def Distente(self):

        c = self.x - num[0]
        d = self.y - num[1]
        dis = sqrt(c ** 2 + d ** 2)
        print("%.2f"%dis)

p1 = Piont(1,0)
p1.Move_By(2,2)
p2 = p1.Move_To()
p1.Distente()
