greet = lambda name: "Welcome, " + name
print(greet("Bob"))

x = lambda price, count: price * count
print(x(2,10))

res = (lambda x, y: x + y) (2,3)
print(res)

def mult(n):
  return lambda a: a * n

doubler = mult(2)
tripler = mult(3)

print(doubler(5))
print(tripler(5))