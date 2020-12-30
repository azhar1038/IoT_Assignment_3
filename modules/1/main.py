import scicalc

x = int(input("Enter x: "))
y = int(input("Enter y: "))

print("%d + %d = %d"%(x, y, scicalc.addition(x, y)))
print("%d - %d = %d"%(x, y, scicalc.subtraction(x, y)))
print("%d * %d = %d"%(x, y, scicalc.multiplication(x, y)))
print("%d / %d = %f"%(x, y, scicalc.division(x, y)))
print("%d %% %d = %d"%(x, y, scicalc.modulus(x, y)))
print("%d ^ %d = %d"%(x, y, scicalc.power(x, y)))
print("sqrt(%d) = %f"%(x, scicalc.square_root(x)))
print("curt(%d) = %f"%(x, scicalc.cubic_root(x)))
print("sin(%d) = %f"%(x, scicalc.sinx(x)))
print("cos(%d) = %f"%(x, scicalc.cosx(x)))
print("tan(%d) = %f"%(x, scicalc.tanx(x)))
print("log(%d) = %f"%(x, scicalc.logx(x)))
print("exp(%d) = %f"%(x, scicalc.expx(x)))
print("|%d| = %d"%(x, scicalc.absolute(x)))