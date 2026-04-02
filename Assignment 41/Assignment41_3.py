#    
# Study Hours[2,   5,   6,   1]
# Attendance [60,  80,  85,  50]
# Results    [Fail,Pass,Pass,Fail]

import numpy as mp
import math

def EucDistance(P1,P2):

    Ans = math.sqrt((P1['StudyHours'] - P2['StudyHours']) **2 + (P1 ['Attendance'] - P2['Attendance']) **2)
    return Ans

def KNN():
    Border = "=" *40

    data = [
        {'StudyHours': 2,'Attendance': 60, 'Result': 'Fail'},
        {'StudyHours': 5,'Attendance': 80, 'Result': 'Pass'},
        {'StudyHours': 6,'Attendance': 85, 'Result': 'Pass'},
        {'StudyHours': 1,'Attendance': 50, 'Result': 'Fail'}      
          ]
    print(Border)
    print("User Defined KNN")
    print(Border)

    print(Border)
    print("Training Dataset")
    print(Border)

    for i in data:
        print(i)
    
    print(Border)

    x = int(input("Enter Study Hours: "))
    y = int(input("Enter Attendance Percentage: "))

    new_point = {'StudyHours': x, 'Attendance': y}

    #calculate all distances
    for d in data:
        d['distance'] = EucDistance(d,new_point) 

    print(Border)
    print("Calculated Distances are:")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data,key = lambda item: item['distance'])   # sort the data based on distance from new point

    print(Border)
    print("Sorted Dataset is based on distances is:")
    print(Border)

    for d in sorted_data:
        print(d)
    
    k = 5         # try k=2,3,5 
    nearest = sorted_data[:k]
    print(Border)
    print("Nearest Elements Are:")
    print(Border)

    for d in nearest:
        print(d)

    # Voting

    votes= {}
    for neighbour in nearest:
        label = neighbour['Result']
        votes[label] = votes.get(label,0) +1

    print(Border)
    print("Voting Result:")
    print(Border)

    for d in votes:
        print("Name:", d, "Number of votes: ", votes[d])

    print(Border)

    predicted_class = max(votes, key = votes.get)

    print("Predicted class of is: ", predicted_class)

def main():

    KNN()

if __name__ == "__main__":
    main()



