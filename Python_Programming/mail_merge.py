PLACEHOLDER = "[name]"

names = ["Angela", "Frank", "Sam", "Jenny"]
letter_template = """Dear [name],

You are invited to my birthday party this Saturday!

Hope to see you there,
Abhishek
"""

for name in names:
    new_letter = letter_template.replace(PLACEHOLDER, name.strip())
    filename = f"letter_for_{name.strip()}.txt"
    with open(filename, mode="w") as file:
        file.write(new_letter)
    print(f"Created {filename}")