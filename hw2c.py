# Chase Whitfield
# MAE 3403
# Problem 1c
# 02/05/2024

def GaussSeidel(Aaug, x, Niter=15):
    """
    Solve liner equations using Gauss-Seidel method.

    :param Aaug: list of lists, augmented matrix [A | B]
    :param x: list, first guess for solution vector
    :param Niter: number of iterations, default set at 15
    :return: final solution vector
    """
    N = len(x)
    for _ in range(Niter):
        for i in range(N):
            sigma = 0
            for j in range(N):
                if j != i:
                    sigma += Aaug[i][j] * x[j]
            x[i] = (Aaug[i][-1] - sigma) / Aaug[i][j]
    return x
def main():
    """
    Main function to run Gauss-Seidel.
    """

    # Example 1
    Aaug1 = [[3, 1, 1, 2],
             [1, 4, 1, 12],
             [2, 1, 2, 10]]
    x1 = [0, 0, 0]
    result1 = GaussSeidel(Aaug1, x1)
    print("Solution for Ex 1:", result1)

    # Example 2
    Aaug2 = [[1, 10, 2, 4, 2],
             [3, 1, 4, 12, 12],
             [9, 2, 3, 4, 21],
             [1, 2, 7, 3, 37]]
    x2 = [0, 0, 0, 0]
    result2 = GaussSeidel(Aaug2, x2)
    print("Solution for Ex 2:", result2)

# Used GPT to help understand the layout of the two different matrices (lines 29-35)

if __name__ == "__main__":
    main()