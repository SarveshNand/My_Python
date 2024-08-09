def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "shaktimaan", power = "lazer")
print_kwargs(name = "shaktimaan")
print_kwargs(name = "shaktimaan", power = "lazer", enemy = "Dr. Jackaal")