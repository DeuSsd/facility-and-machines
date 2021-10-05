from json import dump
from src.facility_and_machines import Facility


def write_json(file_path: str, json_data: dict) -> None:
    """
    Load json data from file_path
    :param file_path: full path where store input.json
    :param json_data: data
    :return: data of machines
    """
    file = open(file_path, "w")
    dump(json_data, file)
    file.close()


def process_all_machines_to_json(facility: Facility) -> dict:
    """
    Process JSON data, extract every machine from them and every configs of that machines
    :param facility: JSON data of machines (actually type is dict())
    :return: collection of all machines and them configs zip in CollectionOfMachines
    """
    # TODO check exist facility
    json_data = {"Count of Machines": len(facility.list_of_machine)}
    list_of_machine = []
    for machine in facility.list_of_machine:
        x, y = machine.get_coors()
        machine_json = {
            "Title of machine": machine.title,
            "x": x,
            "y": y,
            "h": machine.h,
            "w": machine.w
        }
        list_of_machine.append(machine_json)
    json_data["List of machines"] = list_of_machine
    return json_data


def write_machines_to_json(file_path: str, facility: Facility):
    """
    Read JSON config file of all machines and process them to collection of object
    :param file_path: full path file to JSON input.json
    :param facility:
    :return: collection of all machines and them configs zip in CollectionOfMachines
    """
    json_data = process_all_machines_to_json(facility)
    write_json(file_path, json_data)


if __name__ == "__main__":
    path = "U:/facility-and-machines/input.json"
    # MM = write_machines_to_json(path)
    # print(len(MM))
