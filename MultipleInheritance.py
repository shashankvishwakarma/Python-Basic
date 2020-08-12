class Father:
    def gardening(self):
        print("I enjoy gardening")

    def skills(self):
        print("gardening, programing")


class Mother:
    def cooking(self):
        print("I enjoy cooking")

    def skills(self):
        print("cooking, art")


class Child(Father, Mother):
    def sports(self):
        print("I enjoy sports")

    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")


c = Child()
c.gardening()
c.cooking()
c.sports()

c.skills()