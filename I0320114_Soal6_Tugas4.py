# Operator Binary

a = 4
b = 11       
c = 0

c = a | b;      
print("nilai : ", c, ", binary : ", format(c, "08b"))

print("")
c = a >> b;     
print("nilai : ", c, ", binary : ", format(c, "08b"))

print("")
c = a ^ b;      
print("nilai : ", c, ", binary : ", format(c, "08b"))

print("")
c = ~a;         
print("nilai : ", c, ", binary : ", format(c, "08b"))

print("")
c = b & a;      
print("nilai : ", c, ", binary : ", format(c, "08b"))
