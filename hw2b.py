# Chase Whitfield
# MAE 3403
# HW 1 Problem b
# 02/05/2024

from math import cos

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """

    :param fcn: Function used to find the root
    :param x0: X value in neighborhood of the root
    :param x1: Other X value in neighborhood of root
    :param maxiter: Max number of iterations allowed. Default is 10
    :param xtol: Exit if the absolute difference between the most recent and previous x values is less than xtol. Default is 1e-5.

    :return: Final estimate of the root (most recent new x value).
    """
    iter_count = 0

    while iter_count < maxiter:
        f_x0 = fcn(x0)
        f_x1 = fcn(x1)

        # Find root using Secant formula
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(f_x1 - f_x0) < xtol:
            return x1

        if abs(x_new - x1) < xtol:
            return x_new

        x0, x1 = x1, x_new
        iter_count += 1

        # Return last estimate if max number is reached
        return x1
# Used GPT to help with the while loop
def main():
    """
    Main function demonstrate Secant on diff eqs
    """
    # Equation 1: x - 3cos(x) = 0
    fcn1 = lambda x: x - 3 * (cos(x))
    x0_1, x1_1, maxiter_1, xtol_1 = 1, 2, 5, 1e-4
    root_1 = Secant(fcn1, x0_1, x1_1, maxiter_1, xtol_1)
    print("Solution for x - 3cos(x)" , root_1)

# Used GPT to understand 44-48 to get the base idea of the formula down
    # cos(2x) * x^3 = 0
    fcn2 = lambda x: cos(2 * x) * (x ** 3)
    x0_2, x1_2, maxiter_2, xtol_2 = 1, 2, 15, 1e-8
    root_2 = Secant(fcn2, x0_2, x1_2, maxiter_2, xtol_2)
    print("Solution for cos(2x) * x^3 = 0:", root_2)

    # same as second equation but different values
    fcn3 = lambda x: cos(2 * x) * (x**3)
    x0_3, x1_3, maxiter_3, xtol_3 = 1, 2, 3, 1e-8
    root_3 = Secant(fcn3, x0_3, x1_3, maxiter_3, xtol_3)
    print("Solution for cos(2x) * x^3 = 0:" , root_3)

if __name__ == "__main__":
    main()



