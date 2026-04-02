import numpy as np
import matplotlib.pyplot as plt

# Experience as X and Salary as Y

def Predictor():

    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]

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

    print("Predicted Salary for 6 Years Experience is:", m*6 + C)

    # Plot Data Points and Regression Line

    plt.scatter(X,Y,color = "r",label = "Data points")
    plt.plot(X,Y,color = "g",label ="Regression Line" )

    plt.xlabel("X : Independent variables")
    plt.ylabel("Y : Dependent variables")

    plt.legend()
    plt.show()



def main():
    Predictor()

if __name__ == "__main__":
    main()

