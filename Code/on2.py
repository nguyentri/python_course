a, b = [5, 2]
c = a%b + a/b
if c > a:
  c = a
elif c > b:
  c = b
elif c > 1:
  c = 1
else:
  c = 0
print(c)
