def power(p,n):
    if n == 0:
        return 1
    return p*power(p,n-1)
p = float(input("Enter the value of p: "))
n = int(input("Enter the value of n: "))
print("p^n = ",power(p,n))
