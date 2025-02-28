A = {"c", "d", "a", "g", "b", "f"}
B = {"c", "l", "m", "o", "b", "h"}
C = {"c", "d", "h","i", "j", "k","f"}


print("How many elements are there in set A", len(A))
print("How many elements are there in set B", len(B))


b = B - (A | C)
print("How many elements are there in B that is not part of A and C:", len (b))

print("i.", (C - (A | B)) | (B & C)- ( A & B & C))
print("ii.", A & C)
print("iii.", (B & A) | (B & C))
print("iv.", A & C - B)
print("v.", A & B & C)
print("vi.", B - (A | C))