x = 10
y = 3

# Arithmetic
print(f"Arithmetic  :\n x+y={x+y}, \n x-y={x-y}, \n x*y={x*y}, \n x/y={x/y:.2f}")

# Comparison
print(f"Comparison  :\n x>y={x>y}, \n x<y={x<y}, \n x==y={x==y}, \n x!=y={x!=y}, \n x>=y={x>=y}")

# Logical
print(f"Logical     :\n (x>5 and y<5)={(x>5 and y<5)}, \n (x<5 or y<5)={(x<5 or y<5)}, \n not(x>5)={not(x>5)}")

# Assignment operators
n = 10
n += 5;  print(f"Assignment  :\nn+=5  -> n={n}")
n -= 3;  print(f"n-=3  -> n={n}")
n *= 2;  print(f"n*=2  -> n={n}")
n //= 4; print(f"n//=4 -> n={n}")

# Bitwise operators
p, q = 6, 3   # 110, 011 in binary
print(f"Bitwise     : p={p}({bin(p)}), q={q}({bin(q)})")
print(f"  AND p&q  = {p & q}  ({bin(p & q)})")
print(f"  OR  p|q  = {p | q}  ({bin(p | q)})")
print(f"  XOR p^q  = {p ^ q}  ({bin(p ^ q)})")
print(f"  NOT ~p   = {~p}")
print(f"  LEFT  p<<1 = {p << 1}")
print(f"  RIGHT p>>1 = {p >> 1}")

# Expression with multiple operators
result = (x + y) * 2 - x // y + x % y
print(f"\nComplex expression (x+y)*2 - x//y + x%y = {result}")
