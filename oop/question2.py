class Employee:
    def __init__(self, name, dob, salary, skill_sets):
        self.name = name
        self.dob = dob
        self.salary = salary
        self.skill_sets = skill_sets

    @property
    def age(self):
        return 2026 - self.dob


class Developer(Employee):
    def __init__(self, name, dob, salary, skill_sets, github_link, is_fullstack):
        super().__init__(name, dob, salary, skill_sets)
        self.github_link = github_link
        self.is_fullstack = is_fullstack

    def show_profile(self):
        skill_set_names = ", ".join(self.skill_sets)
        return f"{self.name} has skills: {skill_set_names}  Git: {self.github_link}"


person_1 = Developer("ankit", 1999, 300000, {s1,s2}, "hd123", "Yes")
print(person_1.age)
print(person_1.show_profile())
