from sympy import symbols, Eq, solve

#Giải phương trình a - 4 = 0
x = symbols('x')
expr = x-4
sol = solve(expr)
x = int(sol[0])
print ("x =", x)

#Giải phương trình x^2 -5x + 6 = 0
x = symbols('x')
eq1 = Eq(x**2 -5*x + 6, 0)
x = solve(eq1)
print ("x =", x)

#Giải phương trình 
# x + y - 5 = 0
# x - y + 3 = 0
x, y = symbols('x y')
eq1 = Eq(x + y - 5, 0)
eq2 = Eq(x - y + 3, 0)
sol = solve((eq1, eq2), (x, y))
x = sol[x]
y = sol[y]
print ("x =", x, "y =", y)
