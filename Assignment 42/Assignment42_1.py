import numpy as np

def Predictor():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Independant Variables: ", X)
    print("Dependent Variables:", Y)

    mean_x = sum(X)/len(X)
    mean_y = sum(Y)/len(Y)

    print("Mean of X is:",mean_x)
    print("Mean of Y is:", mean_y)

    n= len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)** 2)
    
    m = numerator/denominator
    print("Slope of the line (m) is:", m)

    C = mean_y -(m* mean_x)
    print("Intercept of line (C) is:", C)

    print("Regression Equation:")
    print("Y = ", m, "X + ", C)

    print("Predicted Y for X=6 is:", m*6 + C)

def main():
    Predictor()

if __name__ == "__main__":
    main()

