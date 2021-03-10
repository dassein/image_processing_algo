# https://github.com/wizardforcel/sicp-py-zh/blob/master/1.6.md
# UCB CS61a SICP Python  1.6 高阶函数

def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


## Newton's method
def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta) - f(x)
    return df / delta

def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update

## Find root with specific method
def find_root(f, initial_guess=10):
    def test(x): # is root or not
        return approx_eq(f(x), 0)
    return iter_improve(newton_update(f), test, initial_guess)


## Instances for finding root
def square(x):
    return x * x

def square_root(a):
    return find_root(lambda x: square(x) - a)

def logarithm(a, base=2):
    return find_root(lambda x: base**x - a)


if __name__ == "__main__":
    print( square_root(16) )
    print( logarithm(32, 2) )
