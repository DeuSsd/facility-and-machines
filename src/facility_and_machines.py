class UnavailableSpace(Exception):
    pass

class NotExistFacility(Exception):
    pass

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
        self.__coors: tuple = (x, y)
        self.h = h
        self.w = w
        self.__square = 0
        self.__calculate_square()

    def get_coors(self) -> tuple:
        """
        Return pair of coordinates of the lower left corner of the rectangle
                           ---------------
                           |             |
                           |             |
        this dot (x,y)->   o -------------
        :return:(x,y)
        """
        # print(self.__coors, id(self.__coors))
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

        y
       |     this point 1 (x1,y1)  x1 = x, y1 = y+h
       |     |
       |     o--------------
       | h   |             |
       |     |             |
       |     --------------o  <- this point 2 (x2,y2)  x2 = x+w, y2 = y
       |         w
       0--------------------------------> x
        :return: (x1,y1),(x2,y2)
        """
        x, y = self.__coors
        point_1 = (x + self.w, y)
        point_2 = (x, y + self.h)
        return point_1, point_2

    def show(self):
        print(id(self), self.get_coors(), self.get_sides(), self.get_square(), type(self))

    def get_all_corner_coors(self) -> [tuple]:
        '''
        ld_point - left-down point
        lu_point - left-up point
        rd_point - right-down point
        ru_point - right-up point

        y
        |     this lu_point (x1,y1)  x1 = x, y1 = y+h
        |     |
        |     o-------------o <- this ru_point (x3,y3)  x3 = x+w, y3 = y+h
        | h   |             |
        |     |             |
        |     o-------------o  <- this rd_point(x2,y2)  x2 = x+w, y2 = y
        |         w
        0--------------------------------> x
        :return: list of corners point [LD, LU, RD, RU]
        '''

        x, y = self.get_coors()
        ld_point = (x, y)
        lu_point = (x, y + self.h)
        rd_point = (x + self.w, y)
        ru_point = (x + self.w, y + self.h)
        return [ld_point, lu_point, rd_point, ru_point]

    def check_cross_rectangle_sides(self, list_of_point: [tuple]) -> bool:
        """
          y
        |
        |
        |     o-------------o          bounders:
        | h   |             |          x < x_t < x+w
        |     | (x,y)       |         y < y_t < y+h
        |     o-------------o
        |         w
        0--------------------------------> x

        :param list_of_point: list of corners point [LD, LU, RD, RU]
        :return: if any point included, then return true
        """

        x, y = self.get_coors()  # (x,y)
        for point in list_of_point:
            x_t, y_t = point
            # if (x_t > x and x_t < x + self.w) and \
            #         (y_t > y and y_t < y + self.h):
            if x_t > x and y_t > y:
                return True
        return False


class Machine(Object):
    """
    Class of Machine.
    """

    def __init__(self, title, x=0, y=0, h=0, w=0):
        super().__init__(x=x, y=y, h=h, w=w)
        self.title = title

    def get_info(self):
        print(self.title, self.get_coors(), self.get_sides())

    def __copy__(self):
        x, y = self.get_coors()
        copy = Machine(
            title=self.title,
            x=x,
            y=y,
            h=self.h,
            w=self.w
        )
        # print(id(copy.get_coors()),id(self.get_coors()))
        return copy

    def copy(self):
        return self.__copy__()


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

        # print(machine, type(machine), id(machine))
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
        self.list_of_machine: [Machine] = []  # TODO может буду инкапсулирвоать
        self.__list_of_mounting_points: {tuple} = set()  # TODO проверить расположение объекта /
        self.__append_new_mounting_point(self.get_coors())

    def get_info(self):
        print(self.list_of_machine.__len__(), self.get_sides(), self.get_square())

    def __lt__(self, other):
        return self.get_square() < other.get_square()

    def get_all_mounting_points(self):
        return self.__list_of_mounting_points

    def set_all_mounting_points(self, mounting_points: [tuple]):
        self.__list_of_mounting_points = mounting_points.copy()

    def exclude_collision(self, new_coors: tuple, machine: Machine):
        copy_machine = machine.copy()
        self.__place_machine(new_coors, copy_machine)
        if self.__collision_detect(copy_machine):
            self.__list_of_mounting_points.add(new_coors)
            return False
        else:
            return True


    def append_new_machine(self, new_coors: tuple, machine: Machine):
        """
        Append a new instance of class Machine to the list of already existing rectangles objects
        :param new_coors:
        :param machine: instance of class Machine
        :return:
        """
        # TODO if included, then interrupt
        copy_machine = machine.copy()
        self.__place_machine(new_coors, copy_machine)  # TODO refactor this function: delete and add same coors
        self.list_of_machine.append(copy_machine)
        self.__find_new_mounting_points(copy_machine)
        self.__calculate_new_sides(copy_machine)
        self.get_square()

        # machine.show()
        # self.show()

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
        copy = Facility(h=self.h, w=self.w)
        for item in self.list_of_machine:
            copy.list_of_machine.append(item.copy())
        copy.set_all_mounting_points(self.__list_of_mounting_points)
        return copy

    def copy(self):
        return self.__copy__()

    def __collision_detect(self, new_machine: Machine) -> bool:
        corners_list = new_machine.get_all_corner_coors()
        for machine in self.list_of_machine:
            if machine.check_cross_rectangle_sides(corners_list):
                return True
        return False

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
            print("")
            for el in item.list_of_machine:
                print(el.title, el.h, el.w, el.get_coors())
            # item.show()

    # def __del__(self): #TODO maybe should realise

    def get_best_choose(self):
        self.__collection_of_facilities.sort()
        return self.__collection_of_facilities.pop(0)


    def empty(self):
        return not bool(self.__collection_of_facilities)

if __name__ == "__main__":
    a = Machine("M", x=0, y=0, h=2, w=3)
    b = Machine("M", x=-3, y=0, h=2, w=3)
    t = a.check_cross_rectangle_sides(b.get_all_corner_coors())
    print(t)
