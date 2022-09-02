"""Rogan Helm

Date: 3/31/22
This will implement several job classes derived from person.
"""


def main():
    human1 = Person("Matt", "1", "3", "7")
    # human1.sit()
    human1.go_to_work()
    human2 = Plumber("mike", "2", "4", "6", "Jobber")
    # human2.sit()
    human2.go_to_work()


class Person:
    def __init__(self, a_name, ss, height, age):
        self.name = a_name
        self.ss = ss
        self.height = height
        self.age = age

    def sit(self):
        print("I am sitting!")

    def walk(self):
        print("I am walking")

    def state_name(self):
        print("Hello. My name is " + str(self.name))

    def go_to_work(self):
        print("I need a job")


class Plumber(Person):
    def __init__(self, a_name, ss, height, age, a_type):
        super().__init__(a_name, ss, height, age)
        self.type = a_type
        self.toolbox = ToolBox()

    def fix(self):
        print("fix")

    def go_to_work(self):
        # return super().go_to_work()
        print("I'm at the job site")
        print("I'm installing new pipes")
        print("I'm fixing the sink")


class ToolBox:
    def __init__(self):
        self.tools = ["Hammer", "Screw Driver"]

    def __organize_tools(self):
        self.tools.sort()

    def add_tool(self, new_tool):
        self.tools.append(new_tool)
        self.__organize_tools()


if __name__ == "__main__":
    main()
# ---------------
# permutations and combinations
# ---------------
# Review day

