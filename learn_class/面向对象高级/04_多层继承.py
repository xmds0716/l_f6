"""
多层基层解释：
    类A继承类B 类B继承类C
object <- Master , School <- prentice <- Tusun
"""

class Master:
    def __init__(self):
        self.kongfu = "[古法配方]"

    def make_cake(self):
        print(f"采用{self.kongfu}制作煎饼")

class School:
    def __init__(self):
        self.kongfu = "[现代配方]"

    def make_cake(self):
        print(f"采用{self.kongfu}制作煎饼")

class Prentice(School,Master):
    def __init__(self):
        self.kongfu = "[独创配方]"

    def make_cake(self):
        print(f"采用{self.kongfu}制作煎饼")

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    #def make_old_cake(self):
    #    super().__init__()
    #    super().make_cake()

class TuSun(Prentice):
    pass

if __name__ == "__main__":
    ts = TuSun()
    ts.make_cake()
    ts.make_master_cake()
    ts.make_school_cake()