class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


s = Programmer("Sarvesh", 100000, 23434)
print(s.name, s.salary, s.pin, s.company)
r = Programmer("Rishabh", 100000, 23434)
print(r.name, r.salary, r.pin, r.company)