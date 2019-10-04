import numpy as np

#Variable used as a counter of interated test cases
counter_case=1

#Receive the number of Test Cases
test_case=int(input("Please, Insert the number of test cases"))

#Start to receive all input related to the Star's coordinates
while counter_case<=test_case:

    #Insert the Data from all Starts according to the Case
    print(" Insert data related to Case", counter_case)
    print("Insert the oldest Coordinate (X,Y) of First Star, Case", counter_case)
    a1=float(input())
    b1=float(input())
    print("Insert the oldest Coordinate (X,Y) of Second Star, Case", counter_case)
    c1=float(input())
    d1=float(input())
    print("Insert the newest Coordinate (X,Y) of First Star, Case", counter_case)
    a2=float(input())
    b2=float(input())
    print("Insert the newest Coordinate (X,Y) of Second Star, Case", counter_case)
    c2=float(input())
    d2=float(input())

    #Define an Equation that correlates the oldest and new position of First Star
    x1= -2*a1+2*a2
    y1= -2*b1+2*b2
    z1= a2*a2-a1*a1 + b2*b2-b1*b1

    # Define an Equation that correlates the oldest and new position of Second Star
    x2= -2*c1+2*c2
    y2= -2*d1+2*d2
    z2= c2*c2-c1*c1 + d2*d2-d1*d1

    #Use numpy library to calculate a linear system,
    # This output will be the coordinate of the Black Hole (Concentric Circle)
    A = np.array([[x1,y1],[x2,y2]])
    b = np.array([z1,z2])
    result = np.linalg.solve(A, b)
    print("Case #"+str(counter_case)+ "  {:.2f} {:.2f} ".format(result[0],result[1]))

    # Increment a variable to receive a data from another Test Case
    counter_case = counter_case + 1

