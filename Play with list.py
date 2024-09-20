l = [4,5,1,2,9,7,10,8]
print(f"Original list = {l}")

count = 0

for i in l:
    count = count + i
    
avg = count/len(l)

print(f"sum = {count} ")
print(f"average = {avg}")

l.sort( )
print(l)

print(f"Smallelst element is:{l[0]}")

print(f"Largest element is:{l[-1]}")