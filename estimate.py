import math
import unittest
import random

# function to calculate the Wallis product estimate of Pi
def wallis(n):
    PI = 2.0;
    leftProduct = 0.0;
    rightProduct = 0.0;
    for x in range(1,n):
        leftProduct = (2.0 * x)/((2.0 * x)-1.0);
        rightProduct = (2.0 * x)/((2.0 * x)+1.0);
        PI *= (leftProduct * rightProduct);

    return(PI);

# returns true if the given point is inside the circle, else false
def checkInCircle(x,y):
    equality = (x-1)**2 + (y-1)**2;
    if(equality <= 1):
        return True;
    else:
        return False;

# function for the Monte-Carlo simulation
def monte_carlo(n):

    PI = 0.0;

    x_coordinate = 0 # x coordinate of dart throw
    y_coordinate = 0 # y coordinate of dart throw

    total_darts = 0  # total darts thrown
    darts_in_circle = 0 #total darts inside circle 

    for x in range(n):
        x_coordinate = random.random() * 2;
        y_coordinate = random.random() * 2;

        if(checkInCircle(x_coordinate,y_coordinate) == True):
            darts_in_circle = darts_in_circle + 1;
        total_darts = total_darts + 1;

    PI = (darts_in_circle/total_darts)*4;
    return(PI);

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
