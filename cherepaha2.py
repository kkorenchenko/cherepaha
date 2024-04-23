import turtle

class Info:
    def __init__(self):
        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.colors = ['red', 'orange', 'yellow', 'green', 'royal blue', 'blue', 'purple', 'black', 'brown']
        self.figures = ['circle', 'rectangle', 'square', 'triangle']
        self.size = 50
        self.figure = 0
        self.color = 0

    def text(self):
        self.info.clear()
        self.info.up()
        self.info.goto(-330,260)
        self.info.write(f"Фигура: {self.figures[self.figure]}", align="left", font=("Arial", 10, "normal"))
        self.info.goto(-330,240)
        self.info.write(f"Цвет: {self.colors[self.color]}", align="left", font=("Arial", 10, "normal"))
        self.info.goto(-330,220)
        self.info.write(f"Размер: {self.size}", align="left", font=("Arial", 10, "normal"))

    def next_figure(self):
        if self.figure < len(self.figures)-1:
            self.figure+=1
        elif self.figure == len(self.figures)-1:
            self.figure = 0
        info.text()
            
    def next_color(self):
        if self.color < len(self.colors)-1:
            self.color+=1
        elif self.color == len(self.colors)-1:
            self.color = 0
        info.text()

    def min_size(self):
        self.size-=10
        info.text()

    def max_size(self):
        self.size+=10
        self.text()

class Figure:
    def __init__(self, info, x, y):
        self.x = x
        self.y = y
        #self.color = info.colors[info.color]
        print(self.x,self.y)
        self.turtle = turtle.Turtle()
        self.turtle.shape('turtle')
        self.turtle.pensize(3)
        self.turtle.speed(5)
        self.turtle.color(info.colors[info.color])

    def draw():
        pass

class Circle(Figure):
    def __init__(self, info, x, y):
        super().__init__(info, x, y)
        self.size = info.size
        self.color = info.color
        print(self.size, self.x, self.y)

    def draw(self):
        #self.turtle.color(self.color)
        self.turtle.up()
        self.turtle.goto(self.x, self.y)
        self.turtle.down()
        self.turtle.begin_fill()
        self.turtle.circle(self.size)
        self.turtle.end_fill()
        self.turtle.hideturtle()

class Rectangle(Figure):
    def __init__(self, info, x, y):
        super().__init__(info, x, y)
        self.size = info.size

    def draw(self):
        self.turtle.up()
        self.turtle.goto(self.x, self.y)
        self.turtle.down()
        self.turtle.begin_fill()
        for i in range(2):
            self.turtle.forward(self.size)
            self.turtle.right(90)
            self.turtle.forward(self.size*2)
            self.turtle.right(90)
        self.turtle.end_fill()
        self.turtle.hideturtle()

class Square(Figure):
    def __init__(self, info, x, y):
        super().__init__(info, x,y)
        self.size = info.size

    def draw(self):
        self.turtle.up()
        self.turtle.goto(self.x, self.y)
        self.turtle.down()
        self.turtle.begin_fill()
        for i in range(4):
            self.turtle.forward(self.size)
            self.turtle.right(90)
        self.turtle.end_fill()
        self.turtle.hideturtle()

class Triangle(Figure):
    def __init__(self, info, x, y):
        super().__init__(info, x, y)
        self.size = info.size

    def draw(self):
        self.turtle.up()
        self.turtle.goto(self.x, self.y)
        self.turtle.down()
        self.turtle.begin_fill()
        for i in range(3):
            self.turtle.forward(self.size)
            self.turtle.left(120)
        self.turtle.end_fill()
        self.turtle.hideturtle()
        
def draw(x,y):
    info.text()
    #print(info)
    if info.figures[info.figure] == 'circle':
        #print(info)
        figure = Circle(info, x, y)
        figure.draw()
    if info.figures[info.figure] == 'rectangle':
        figure = Rectangle(info, x, y)
        figure.draw()
    if info.figures[info.figure] == 'square':
        figure = Square(info, x, y)
        figure.draw()
    if info.figures[info.figure] == 'triangle':
        figure = Triangle(info, x, y)
        figure.draw()



info = Info()
info.text()
turtle.onscreenclick(draw)
turtle.onkey(info.next_color, "q")
turtle.onkey(info.next_figure, "w")
turtle.onkey(info.min_size, "Down")
turtle.onkey(info.max_size, "Up")
turtle.listen()

'''circle = Circle (100, 'red', 250, -250)
circle.draw()'''
