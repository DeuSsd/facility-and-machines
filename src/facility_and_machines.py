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
        self.__calculate_square()

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

    def get_sides(self):
        """
        Return pair of rectangle's sides
            --------------
        h   |            |
            |            |
            --------------
                  w
        :return:(h,w)
        """

        return self.h, self.w

    def __calculate_square(self) -> None:
        """
        Count value of square rectangle
            ---------------
        h   |             |
            | S = h * w   |
            --------------
                  w
        :return:
        """
        self.__square = self.h * self.w

    def get_square(self):
        """
        Recount value of square rectangle and return them
        :return: value of square rectangle
        """
        self.__calculate_square()
        return self.__square

    def process_mounting_points(self):
        """
        Add new point

            this point 1 (x1,y1)
            |
            o--------------
        h   |             |
            |             |
            --------------o  <- this point 2 (x2,y2)
                w
        :return: (x1,y1),(x2,y2)
        """
        x, y = self.__coors
        point_1 = (x + self.h, y)
        point_2 = (x, y + self.w)
        return point_1, point_2


class Machine(Object):
    """
    Class of Machine.
    """

    def __init__(self, title, x=0, y=0, h=0, w=0):
        super().__init__(x=x, y=y, h=h, w=w)
        self.title = title


class CollectionOfMachines:
    """
    Class which store all machines and them configs
    access by every machine provided by a key called "title"
    """

    def __init__(self):
        self.machines = dict()

    def __len__(self):
        return self.machines.__len__()

    def append_new_machine(self, machine: Machine):
        """
        Method for appending a new machine in the collection
        struct of collection present below:
        {
            "M1" : [Machine.M1 shape h1 x w1, Machine.M1 shape h2 x w2],
            "M2" : [Machine.M2 shape h1 x w1, Machine.M2 shape h2 x w2, Machine.M2 shape h3 x w3]
            "M3" : [Machine.M3 shape h1 x w1]
        }
        :param machine: instance of class Machine
        :return: None
        """
        
        # Create list if doesn't exist earlier
        if self.__check_exist_this_machine(machine):
            self.machines[machine.title].append(machine)
        else:
            self.machines[machine.title] = [machine]

    def __check_exist_this_machine(self, machine: Machine) -> bool:
        """
        Method check exist this type of machine in collection
        :param machine: instance of class Machine
        :return: bool type of answer exist or not [True / False]
        """
        return machine.title in self.machines.keys()

    def empty(self):
        return bool(self.machines)


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
        self.__list_of_mounting_points = set()  # TODO проверить расположение объекта /
        self.__append_new_mounting_point(self.get_coors())

    def __lt__(self, other):
        return self.get_square() < other.get_square()

    def get_all_mounting_points(self):
        return self.__list_of_mounting_points

    def set_all_mounting_points(self, mounting_points : [tuple]):
        self.__list_of_mounting_points = mounting_points.copy()

    def append_new_machine(self, new_coors: tuple, machine: Machine):
        """
        Append a new instance of class Machine to the list of already existing rectangles objects
        :param new_coors:
        :param machine: instance of class Machine
        :return:
        """
        self.__place_machine(new_coors, machine)  # TODO check changes
        self.list_of_machine.append(machine)
        self.__find_new_mounting_points(machine)
        self.__calculate_new_sides(machine)
        self.get_square()

    def __append_new_mounting_point(self, new_coors: tuple):
        self.__list_of_mounting_points.add(new_coors)

    def __place_machine(self, new_coors: tuple, machine: Machine):
        machine.set_coors(new_coors)
        self.__list_of_mounting_points.discard(new_coors)
        return machine  # TODO check changes, maybe need deleted

    def __find_new_mounting_points(self, machine: Machine):
        point_1, point_2 = machine.process_mounting_points()
        self.__append_new_mounting_point(point_1)
        self.__append_new_mounting_point(point_2)

    def __update_sides(self, h, w):
        if h > self.h:
            self.h = h
        if w > self.w:
            self.w = w

    def __calculate_new_sides(self, machine: Machine):  # TODO check changes
        x, y = machine.get_coors()
        h, w = machine.get_sides()
        h += y
        w += x
        self.__update_sides(h=h, w=w)

    def __copy__(self):
        copy = Facility()
        copy.list_of_machine = self.list_of_machine.copy()
        copy.set_all_mounting_points(self.__list_of_mounting_points)
        return copy

    def copy(self):
        return self.__copy__()


class CollectionOfFacilities:
    def __init__(self):
        self.__collection_of_facilities = []

    def sort(self):
        self.__collection_of_facilities.sort()

    def append_new_facility(self, facility: Facility):
        """
        Append a new instance of class Machine to the list of already existing rectangles objects
        :param facility: instance of class Machine
        :return:
        """
        self.__collection_of_facilities.append(facility)

    def show(self):
        for item in self.__collection_of_facilities:
            print(";")
            for el in item.list_of_machine:
                print(el.title, el.h, el.w,el.get_coors())

    # def __del__(self): #TODO maybe should realise

    def get_best_choose(self):
        self.__collection_of_facilities.sort()
        return self.__collection_of_facilities.pop(0)

if __name__ == "__main__":
    a = Facility(x=1, y=2, h=2, w=4)
    print(a.get_square())
    print(a.get_coors())
