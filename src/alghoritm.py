from src.read_config_of_machienes import load_machines_from_json
from src.facility_and_machines import Machine, CollectionOfMachines, Facility, CollectionOfFacilities


def main(file_path: str):
    machine_list = load_machines_from_json(file_path)
    machines_name = list(machine_list.machines.keys())
    title = machines_name[0]
    machines_configs = machine_list.machines.pop(title)
    collection_of_facilites = CollectionOfFacilities()
    for config in machines_configs:
        best_facility = Facility()
        best_facility.append_new_machine((0,0),config)
        for machine in machine_list.machines:
            machine = machine_list.machines[machine]
            print(machine, type(machine))
            best_facility = find_best_facility(machine,best_facility)
        collection_of_facilites.append_new_facility(best_facility)
    return collection_of_facilites



def find_best_facility(machine:[Machine],facility:Facility):
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
        print(config,type(config))
        best_facility = find_best_facility_place(config,facility_variate)
        local_collection_of_facilites.append_new_facility(best_facility)
    local_collection_of_facilites.show()
    best_facility = local_collection_of_facilites.get_best_choose()
    return best_facility


def find_best_facility_place(config:Machine,facility:Facility):
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
    print(mounting_points)

    for point in mounting_points:
        facility_variate = facility.copy()
        print("bruteforce")
        print(point)
        facility_variate.append_new_machine(point, config)
        local_collection_of_facilites.append_new_facility(facility_variate)
    best_facility = local_collection_of_facilites.get_best_choose()
    return best_facility







if __name__ == '__main__':
    path = "U:/facility-and-machines/input.json"
    facilitys = main(path)
    facilitys.show()