#Highest Common Factor#
first=int(input("First number: "))
Second=int(input("Second number: "))
if first<Second:
    factor=first
else:
    factor=Second
while first%factor!=0 or Second%factor!=0:
    factor=factor-1
print(" The highest Common factor:",factor)