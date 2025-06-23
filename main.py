from turtle import *
import math
import random
import time

# ==================== SETUP ====================
screen = Screen()
screen.bgcolor("misty rose")  # Soft pink background
screen.title("Magical Heart Animation")
screen.tracer(0)  # For smooth animation

# ==================== HEART FUNCTION ====================
def heart_shape(n, size=1):
    x = 16 * math.sin(n)**3 * size
    y = (13*math.cos(n) - 5*math.cos(2*n) - 2*math.cos(3*n) - math.cos(4*n)) * size
    return x, y

# ==================== MOVING BUTTERFLY ====================
class Butterfly(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color(random.choice(["pink", "light pink", "hot pink"]))
        self.shape("triangle")
        self.shapesize(0.5, 1)
        self.setpos(random.randint(-350, 350), random.randint(-250, 250))
        self.dx = random.uniform(0.5, 2)
        self.dy = random.uniform(0.5, 2)
        
    def move(self):
        x, y = self.pos()
        if x > 380 or x < -380:
            self.dx *= -1
        if y > 280 or y < -280:
            self.dy *= -1
        self.setx(x + self.dx)
        self.sety(y + self.dy)

# ==================== MOVING HEART ====================
class FloatingHeart(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color(random.choice(["pink", "light coral"]))
        self.size = random.uniform(0.3, 0.8)
        self.setpos(random.randint(-350, 350), random.randint(-250, 250))
        self.dx = random.uniform(0.3, 1.5)
        self.dy = random.uniform(0.3, 1.5)
        self.points = [heart_shape(j/15, self.size) for j in range(0, 100, 5)]
        
    def move(self):
        x, y = self.pos()
        if x > 380 or x < -380:
            self.dx *= -1
        if y > 280 or y < -280:
            self.dy *= -1
        self.setx(x + self.dx)
        self.sety(y + self.dy)
        
    def draw(self):
        self.clear()
        self.penup()
        for point in self.points:
            self.goto(self.xcor() + point[0], self.ycor() + point[1])
            self.pendown()

# ==================== MAIN ANIMATION ====================
def main_animation():
    # Create moving background elements
    butterflies = [Butterfly() for _ in range(10)]
    floating_hearts = [FloatingHeart() for _ in range(15)]
    
    # Draw small heart first
    small_heart = Turtle()
    small_heart.speed(0)
    small_heart.color("deep pink")
    small_heart.pensize(2)
    small_heart.hideturtle()
    
    # Phase 1: Draw small complete heart
    small_points = [heart_shape(j/15, 3) for j in range(100)]
    for i in range(len(small_points)-1):
        small_heart.goto(small_points[i])
        small_heart.pendown()
    small_heart.penup()
    screen.update()
    time.sleep(2)
    
    # Phase 2: Gradually grow bigger heart
    growing_heart = Turtle()
    growing_heart.speed(0)
    growing_heart.pensize(3)
    growing_heart.hideturtle()
    
    for size in range(3, 15):  # Grow from size 3 to 15
        growing_heart.clear()
        color = "red" if size % 2 == 0 else "hot pink"
        growing_heart.color(color)
        
        points = [heart_shape(j/15, size) for j in range(100)]
        for i in range(len(points)-1):
            growing_heart.goto(points[i])
            growing_heart.pendown()
        
        # Update moving elements
        for butterfly in butterflies:
            butterfly.move()
        for heart in floating_hearts:
            heart.move()
            heart.draw()
        
        screen.update()
        time.sleep(0.1)
    
    # Keep animation running
    while True:
        for butterfly in butterflies:
            butterfly.move()
        for heart in floating_hearts:
            heart.move()
            heart.draw()
        screen.update()
        time.sleep(0.05)

# ==================== RUN ANIMATION ====================
main_animation()
done()