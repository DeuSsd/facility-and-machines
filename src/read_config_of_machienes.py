from json import load
from src.facility_and_machines import Machine,CollectionOfMachines


def read_josn(file_path: str) -> dict:
    """
    Load json data from file_path
    :param file_path: full path where store input.json
    :return: data of machines
    """
    file = open(file_path, "r")
    machines_json = load(file)
    file.close()
    return machines_json


def process_all_machines_from_json(machines_json: dict) -> CollectionOfMachines:
    """
    Process JSON data, extract every machine from them and every configs of that machines
    :param machines_json: JSON data of machines (actually type is dict())
    :return: collection of all machines and them configs zip in CollectionOfMachines
    """
    machines_collections = CollectionOfMachines()
    amount_of_machines = machines_json['Count of Machine']
    machines_list_json = machines_json['List of machine']

    for machine_object in machines_list_json:
        title = machine_object["Title of machine"]
        amount_of_configs = machine_object['Amount of configs']
        for machine_config in machine_object['Machines']:

            h = machine_config['h']
            w = machine_config['w']

            machine = Machine(title=title,h=h, w=w)
            machines_collections.append_new_machine(machine)
    return machines_collections


def load_machine_from_json(file_path: str) -> CollectionOfMachines:
    """
    Read JSON config file of all machines and process them to collection of object
    :param file_path: full path file to JSON input.json
    :return: collection of all machines and them configs zip in CollectionOfMachines
    """
    json_machines = read_josn(path)
    collection_of_machines = process_all_machines_from_json()
    return collection_of_machines

if __name__ == "__main__":
    path = "U:/facility-and-machines/input.json"
    MM = load_machine_from_json(path)
    print(len(MM))
