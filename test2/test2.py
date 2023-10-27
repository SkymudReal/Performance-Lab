import sys

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

with open(sys.argv[1], 'r') as circle_file:

    circle_coords = circle_file.readline().strip().split()
    circle_x = float(circle_coords[0])
    circle_y = float(circle_coords[1])
    circle_radius = float(circle_coords[2])


with open(sys.argv[2], 'r') as dots_file:
    for line in dots_file:
        dot_coords = line.strip().split()
        dot_x = float(dot_coords[0])
        dot_y = float(dot_coords[1])

        dot_distance = distance(circle_x, circle_y, dot_x, dot_y)

        if dot_distance == circle_radius:
            print("0 - Точка лежит на окружности\n")
        elif dot_distance < circle_radius:
            print("1 - Точка внутри окружности\n")
        else:
            print("2 - Точка снаружи окружности\n")
