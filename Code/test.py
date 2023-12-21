nums = [1, 2, 3]
x = sum(nums) - max(nums)
y = sum(nums)/2
z = int(x - y)
if(z > 3):
  z = 3
elif(z > 2):
  z = 2
elif(z > 1):
  z = 1
print(z)