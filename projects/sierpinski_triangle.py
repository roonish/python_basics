import turtle

def sierpinski_triangle(vertices, degree, my_turtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(vertices, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski_triangle([vertices[0],
                             get_mid(vertices[0], vertices[1]),
                             get_mid(vertices[0], vertices[2])],
                            degree-1, my_turtle)
        sierpinski_triangle([vertices[1],
                             get_mid(vertices[0], vertices[1]),
                             get_mid(vertices[1], vertices[2])],
                            degree-1, my_turtle)
        sierpinski_triangle([vertices[2],
                             get_mid(vertices[2], vertices[1]),
                             get_mid(vertices[0], vertices[2])],
                            degree-1, my_turtle)

def draw_triangle(vertices, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(vertices[1][0], vertices[1][1])
    my_turtle.goto(vertices[2][0], vertices[2][1])
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_vertices = [[-200, -100], [0, 200], [200, -100]]
    sierpinski_triangle(my_vertices, 4, my_turtle)
    my_win.exitonclick()

if __name__ == '__main__':
    main()
