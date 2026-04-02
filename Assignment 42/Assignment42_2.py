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

    # Predict all Y values using regression equation

    Y_pred = []
    for x in X:
        y= m*x + C
        Y_pred.append(y)
        print("Predicted values of Y are:", Y_pred)

    # Calulate MSE
    mse = 0
    for i in range(n):
        mse = mse + ((Y[i] - Y_pred[i])**2)
        mse = mse/n
    print("Mean Squared Error is:", mse)

    # Calculate R2 Score
    r2_numerator = 0
    r2_denominator = 0
    for i in range(n):
        r2_numerator = r2_numerator + ((Y[i] - Y_pred[i])**2)
        r2_denominator = r2_denominator + ((Y[i] - mean_y)**2)
    r2_score = 1 - (r2_numerator/r2_denominator)
    print("R2 Score is:", r2_score)





def main():
    Predictor()

if __name__ == "__main__":
    main()

