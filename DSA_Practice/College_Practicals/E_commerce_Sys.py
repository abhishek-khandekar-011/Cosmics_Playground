customer_ids = ["8", "16" , "32" , "64" , "128" , "256" , "512" , "1024"]
found = False
key = (input("Enter the customer id: "))

for i in customer_ids:
    if i == key:
        found = True
        break
print("Linear Search")
if found:
    print("Found")
else:
    print("Not Found")

#Binary Search

customer_ids.sort()
found = False
low , high = 0 , len(customer_ids) - 1

while low <= high:
    mid = low + high // 2
    if customer_ids[mid] == key:
        found = True
        break
    elif key < customer_ids[mid]:
        high = mid - 1
    else:
        low = mid + 1

print("Binary Search")

if found:
    print("Found")
else:
    print("Not Found")