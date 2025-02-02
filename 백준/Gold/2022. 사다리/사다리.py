import math

x, y, c = map(float, input().split())
left, right = 0, min(x, y)

def get_z(z):
   a = math.sqrt(x**2 - z**2)
   b = math.sqrt(y**2 - z**2)
   return 1/(1/a + 1/b)

ans = 0
while (right - left > 1e-6):
   z = (left+right)/2
   if get_z(z) >= c:
      left = z
   else:
      right = z
   ans = z

print(f"{ans:.3f}")