# Chase Whitfield
# MAE 3403
# Problem 1a
# 02/05/2024

import math
import copy

import math
import copy


def shallow_copy(lst):
    """
    Create and return a shallow copy of the input list.

    Parameters:
    - lst (list): The input list to be copied.

    Returns:
    - list: Shallow copy of the input list.
    """
    return lst[:]


def deep_copy(lst):
    """
    Create and return a deep copy of the input list.

    Parameters:
    - lst (list): The input list to be copied.

    Returns:
    - list: Deep copy of the input list.
    """
    return [elem for elem in lst]


def PDF_callback(args_tuple):
    """
    Gaussian/normal probability density function (PDF) callback.

    Parameters:
    - args_tuple (tuple): A tuple containing values for x, mu (population mean), and sigma (population standard deviation).

    Returns:
    - float: Probability density function value.
    """
    x, mu, sigma = args_tuple
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def integrate_simpsons_1_3(PDF, args, c, GT=True, n=1000):
    """
    Integrate the given PDF using Simpson's 1/3 rule to find the probability.

    Parameters:
    - PDF (callable): A callback function for the Gaussian/normal probability density function.
    - args (tuple): A tuple containing μ and σ for the normal distribution.
    - c (float): The upper limit of integration.
    - GT (bool): If True, calculate the probability of x being greater than c. If False, calculate the probability of x being less than c.
    - n (int): Number of intervals for Simpson's rule (default is 1000).

    Returns:
    - float: The calculated probability.
    """
    mu, sigma = args
    a = mu - 5 * sigma
    b = c

    h = (b - a) / n
    x_values = [a + i * h for i in range(n + 1)]

    result = 0
    for i in range(n + 1):
        if i == 0 or i == n:
            coefficient = 1
        elif i % 2 == 1:
            coefficient = 4
        else:
            coefficient = 2

        x = x_values[i]
        result += coefficient * PDF((x, mu, sigma))

    result *= h / 3

    if GT:
        return result
    else:
        return 1 - result

# Used ChatGPT to help with PDF callback function
# Used ChatGPT for lines 75-91 to help understand coding methods for developing math equations

def main():
    """
    Main function to demonstrate the use of integrate_simpsons_1_3 for two examples.
    """
    # Example 1
    args1 = (100, 12.5)
    c1 = 105
    probability1 = integrate_simpsons_1_3(PDF_callback, args1, c1)
    print(f'P(x<{c1:.2f}|N({args1[0]},{args1[1]}))={probability1:.2f}')

    # Example 2
    args2 = (100, 3)
    c2 = args2[0] + 2 * args2[1]
    probability2 = integrate_simpsons_1_3(PDF_callback, args2, c2, GT=False)
    print(f'P(x>{c2:.2f}|N({args2[0]},{args2[1]}))={probability2:.2f}')

# Used Chat GPT for lines 100-104 to help understand the example process

if __name__ == "__main__":
    main()


