from tkinter import *
from random import randint


class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(0)
       
        self.a[1+20][2+20] = 1
        self.a[2+19][1+19] = 1
        self.a[2+30][1+30] = 1
        self.a[randint(10, 40)][randint(10, 40)] = 1
        self.a[randint(10, 40)][randint(10, 40)] = 1
        self.risovat()
   
    def move(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)
       
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                neib_sum = self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] + self.a[i][j - 1] + self.a[i - 1][j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] + self.a[i + 1][j + 1]
                if neib_sum == 2:
                    b[i][j] = 2
                else:
                    b[i][j] = self.a[i][j]
       
        self.a = b
 
 
    def func(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()
 
    def risovat(self):
        color = "grey"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = "blue"
                elif (self.a[i][j] == 2):
                    color = "maroon"
                else:
                    color = "light steel blue"
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.move()
        self.c.after(99, self.risovat)

root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()
 
f = Field(c, 40, 40, 800, 800)
f.func()
 
root.mainloop()

