import turtle
x1 = float(input("Enter the center x-coordinate of a circle: "))
y1 = float(input("Enter the center y-coordinate of a circle: "))
radius = float(input("Enter the radius of the circle: "))
x2 = float(input("Enter a point x-coordinate: "))
y2 = float(input("Enter a point y-coordinate: "))
# Draw the circle
turtle.penup() # Pull the pen up
turtle.goto(x1, y1 - radius)
turtle.pendown() # Pull the pen down
turtle.circle(radius)
# Calculate the distance from the point to the center
d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
# Determine the point's position relative to the circle
tolerance = 1e-6
if abs(d - radius) < tolerance:
# Point is on the circle
turtle.penup() # Pull the pen up
turtle.goto(x2, y2)
turtle.pendown() # Pull the pen down
turtle.dot(6, "blue")
status = "The point is on the circle"
elif d < radius:
# Point is inside the circle
turtle.penup() # Pull the pen up
turtle.goto(x2, y2)
turtle.pendown() # Pull the pen down
turtle.dot(6, "green")
status = "The point is inside the circle"
else:
# Point is outside the circle
turtle.penup() # Pull the pen up
turtle.goto(x2, y2)
turtle.pendown() # Pull the pen down
turtle.dot(6, "red")
status = "The point is outside the circle"
# Draw a line from the center to the point
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)
# Display the status
turtle.penup() # Pull the pen up
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown()
turtle.write(status, font=("Times", 12))
turtle.hideturtle()
turtle.done()
