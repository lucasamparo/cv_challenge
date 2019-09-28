#########################################################
## Desafio do Curso de Formaçao de Visão Computacional
## Script criado para resolução do cv_challenge
#########################################################
## Autor: Alison do Rosário de Morais
## Email: armorais01@gmail.com
## github: https://github.com/armorais
#########################################################

import os
from sympy.geometry import Point, Segment, Line
from itertools import islice

X_COORD = 0
Y_COORD = 1
LINES_PER_CASE = 4

input_file = './input/input_sample_1.txt'
output_file = './output/output.txt'

# Convert a Point to string
def point_to_string(point):
    return "{0:.2f}".format(point[X_COORD]) + ' ' + "{0:.2f}".format(point[Y_COORD])

# Get the n next lines from the input file. n is defined by LINES_PER_CASE
def next_lines(input):
    return [x.strip() for x in islice(input, LINES_PER_CASE)]

# Get the perpendicular bisector of a segment given two coordinates
def get_byssec_segment(x_coord, y_coord):
    segment = Segment(x_coord, y_coord)
    midpoint = segment.midpoint
    perpendicular_segment = segment.perpendicular_line(midpoint)
    return segment.perpendicular_bisector()

# Get a tuple with the lines representing the bisector of the segments created by the stars positions.
def get_byssec_lines(test_case):
    star1_p1 = Point(get_point(test_case[0]))
    star2_p1 = Point(get_point(test_case[1]))
    star1_p2 = Point(get_point(test_case[2]))
    star2_p2 = Point(get_point(test_case[3]))

    star1_bissec = get_byssec_segment(star1_p1, star1_p2)
    star2_bissec = get_byssec_segment(star2_p1, star2_p2)

    bissec_line_star1 = Line(star1_bissec.points[0],star1_bissec.points[1])
    bissec_line_star2 = Line(star2_bissec.points[0],star2_bissec.points[1])

    return (bissec_line_star1,bissec_line_star2)

# Get the coordinates of the black hole by finding the intersection between two bissectors
def get_black_hole_coord(byssecs):
    coords = byssecs[0].intersection(byssecs[1])[0]
    return (float(coords[0]),float(coords[1]))

# Get a tuples of coordinates from a string of coordinates
def get_point(string_coord):
    return tuple(map(float, string_coord.split()))

# Validate if values are in range
def is_test_case_valid(test_case):
    for i in range(len(test_case)):
        tuple = get_point(test_case[i])
        for item in tuple:
            if(item < -10000.0 or item > 10000.0):
                return False
    return True

# This is the main code block. It opens two files, one for reading the inputs and another for writing
# the output. The idea is getting the black hole position by finding the vertex shared by the two isosceles
# triangles formed by the segments formed by the movement of both stars
if(not os.path.isfile(input_file)):
    print('Error! There is no test case file!')
else:
    with open(input_file, 'r') as input:
        if not os.path.exists('./output/'):
            os.makedirs('./output/')
        with open(output_file, 'w+') as output:
            number_of_test_cases = int(input.readline()) # Get number of test cases
            if(number_of_test_cases > 1 and number_of_test_cases < 10000):
                for i in range(number_of_test_cases):
                    test_case = next_lines(input)
                    if(not is_test_case_valid(test_case)):
                        print('Error! There are out of range data in the test case!')
                        break

                    byssecs = get_byssec_lines(test_case)
                    black_hole_coord = get_black_hole_coord(byssecs)
                    string_out = 'Caso #' + str(i+1) + ': ' + point_to_string(black_hole_coord)
                    print(string_out)
                    output.write("%s\n" % string_out)
                print('\nOutput file created at: ' + output_file)
            elif(number_of_test_cases < 1):
                print('Error! Number of test cases cannot be less than 1!')
            else:
                print('Error! Too many test cases! Number of test cases cannot be more than 10000!')
            output.close()
            input.close()