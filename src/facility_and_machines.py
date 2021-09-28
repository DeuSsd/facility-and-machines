class Object:
    """
    Base class
    Every one of objects is actually rectangle:
         ---------------
    h   |             |
        |             |
        --------------
              w
    """

    def __init__(self, x=0, y=0, h=0, w=0):
        self.__coors = (x, y)
        self.h = h
        self.w = w
        self.__square = 0
        self.__count_square()

    def get_coors(self):
        """
        Return pair of coordinates of the lower left corner of the rectangle
                           ---------------
                           |             |
                           |             |
        this dot (x,y)->   o -------------
        :return:(x,y)
        """
        return self.__coors

    def set_coors(self, coors: tuple) -> None:
        """
        Set new pair of coordinates of the lower left corner of the rectangle
                           ---------------
                           |             |
                           |             |
        this dot (x,y)->   o -------------
        :return:(x,y)
        """
        self.__coors = coors

    def __count_square(self):
        """
        Count value of square rectangle
            ---------------
        h   |             |
            |             |
            --------------
                  w
        :return: S = h * w
        """
        self.__square = self.h * self.w

    def get_square(self):
        """
        Recount value of square rectangle and return them
        :return: value of square rectangle
        """
        self.__count_square()
        return self.__square

class Machine(Object):
    """
    Class of Machine.
    """

    def __init__(self, x=0, y=0, h=0, w=0):
        super().__init__(x=x, y=y, h=h, w=w)


class Facility(Object):
    """
    Class of facility.
    There are a lot of machine (that are rectangles) inside them area.
    Machines objects (that are instances of class Machine) store in list_of_machines
    New one could be append by functions append_new_machine
    """

    def __init__(self, x=0, y=0, h=0, w=0):
        super().__init__(x=x, y=y, h=h, w=w)
        self.__square = 0
        self.list_of_machine = []  # TODO может буду инкапсулирвоать


    def append_new_machine(self, machine: Machine):
        """
        Append a new instance of class Machine to the list of already existing rectangles objects
        :param machine: instance of class Machine
        :return:
        """
        self.list_of_machine.append(machine)


if __name__ == "__main__":
    a = Facility(x=1, y=2, h=2, w=4)
    print(a.get_square())
    print(a.get_coors())
