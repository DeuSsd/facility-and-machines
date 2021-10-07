from src.facility_and_machines import Machine, Facility, CollectionOfFacilities, CollectionOfMachines


def optimize(machine_list: CollectionOfMachines) -> Facility:
    # title = machines_name[0]
    title = machine_list.get_title_large_of_machines()
    machines_configs = machine_list.machines.pop(title)
    collection_of_facilities = CollectionOfFacilities()
    for config in machines_configs:
        # config.get_info() ####
        best_facility = Facility()
        if best_facility.append_new_machine((0, 0), config):
            for machine in machine_list.machines:
                machine = machine_list.machines[machine]
                # print(machine, type(machine), id(machine))
                best_facility = find_best_facility(machine, best_facility)
            # print("BB")
            # for el in best_facility.list_of_machine:
            #     print(el.title, el.h, el.w, el.get_coors())
            # best_facility.show()
            # print("FF")
            yield best_facility
            collection_of_facilities.append_new_facility(best_facility)
            # print("=")
            # collection_of_facilities.show()
            # print("=")
    best_facility = collection_of_facilities.get_best_choose()
    yield best_facility


def find_best_facility(machine: [Machine], facility: Facility):
    '''
    1. Create collection of facilities for config machine
    2. Bruteforce all config machine
    4. Find best facility and return them

    :param machine:
    :param facility_variate:
    :return:
    '''
    local_collection_of_facilites = CollectionOfFacilities()
    for config in machine:
        facility_variate = facility.copy()

        # print("-> ", end="")
        # config.get_info()
        # print(config,type(config))

        best_facility = find_best_facility_place(config, facility_variate)
        local_collection_of_facilites.append_new_facility(best_facility)
    # local_collection_of_facilites.show()
    best_facility = local_collection_of_facilites.get_best_choose()
    return best_facility


def find_best_facility_place(config: Machine, facility: Facility):
    '''
    1. Create collection of facilities for config machine
    2. Get all points for mount config machine
    3. Bruteforce all mount points
    4. Find best facility and return them

    :param config:
    :param facility_variate:
    :return:
    '''
    local_collection_of_facilites = CollectionOfFacilities()
    mounting_points = facility.get_all_mounting_points()
    # print(mounting_points)

    for point in mounting_points:
        facility_variate = facility.copy()
        # print("bruteforce")
        # print(point)
        if facility_variate.append_new_machine(point, config):

            # print("--> ", end="")
            # config.get_info()
            # facility_variate.get_info()

            local_collection_of_facilites.append_new_facility(facility_variate)
    best_facility = local_collection_of_facilites.get_best_choose()
    return best_facility


if __name__ == '__main__':
    path = "U:/facility-and-machines/input.json"
    # facilitys = optimize(path)
    # facilitys.show()
    # item = facilitys
    # for el in item.list_of_machine:
    # print(el.title, el.h, el.w, el.get_coors())
    # item.show()
