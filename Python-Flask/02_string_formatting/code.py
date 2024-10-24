# name = "Bob"
# greeting = f"Hello, {name}"

# print(greeting)

# name = "Rolf"

# print(greeting)

# -------------------

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

longer_phrase = "Hello, {}. Today is {}"

formatted = longer_phrase.format("Bob","Monday")
print(formatted)


