from math import exp

def main():
    x = 0
    h = float(input("Input the Value of h: "))
    y = 1
    ap = 0
    exact = []
    approx = []
    exact_approx = []
    while 0 <= x < 1:
        x = round(x, 2)
        function = round(f(x, y), 7)
        y = y + h * function
        approx.append(y)
        print(y)
        if x >= 0.1:
            ap = round(e(x), 7)
            exact.append(ap)
        x += h
    print(f"     Xn     |      Yn(approx)       |      Yn(exact)      |      Error(e)      ")
    print(f"----------------------------------------------------------------------------------------------------------")
    for i in range(len(approx) and len(exact)):
        print(f"     x{i + 1}      |      {approx[i]}      |       {exact[i]}       |      {exact[i] - approx[i]} ")
        print(f"----------------------------------------------------------------------------------------------------------")

def f(xn, yn):
    return 3 * (xn ** 2) * yn

def e(xn):
    c = xn ** 3
    return exp(c)

main()