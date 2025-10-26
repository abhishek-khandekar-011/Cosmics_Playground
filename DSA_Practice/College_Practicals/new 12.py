n = int(input("Enter number of members: "))
books = []

for i in range(n):
    b = int(input(f"Books borrowed by member {i+1}: "))
    books.append(b)

# Average
avg = sum(books) / n
print("Average books borrowed:", avg)

# Highest and Lowest
print("Highest borrowed:", max(books))
print("Lowest borrowed:", min(books))

# Members with 0 books
zero_count = books.count(0)
print("Members with 0 books:", zero_count)

# Mode (most frequent borrow count)
mode = max(books, key=books.count)
print("Most frequent borrow count (Mode):", mode)
