from src.read_config_of_machienes import load_machines_from_json
from src.facility_and_machines import Machine,CollectionOfMachines,Facility,CollectionOfFacilities

#TODO ATTENTION
#TODO THIS IS NOT WORKING!

def main(machine_list:CollectionOfMachines):
    variate = Facility()
    facilitys = CollectionOfFacilities()

    facilitys_res = process_machines(machine_list,variate,facilitys)

    return facilitys_res

def process_machines(machine_list:CollectionOfMachines, variate:Facility,facilitys:CollectionOfFacilities):
    while True:
        copy_variate = variate.copy()
        if not machine_list:
            break
        machines_name = list(machine_list.machines.keys())
        title = machines_name.pop()
        machines_configs = machine_list.machines.pop(title)
        process_configs(machines_configs,machine_list,copy_variate,facilitys)
    return facilitys

def process_configs(machines_configs:list,machine_list:CollectionOfMachines, variate:Facility,facilitys:CollectionOfFacilities):
    for config in machines_configs:
        copy_variate = variate.copy()
        copy_variate.append_new_machine(config)
        if not machine_list.empty():
            process_machines(machine_list,copy_variate,facilitys)
        else:
            facilitys.append_new_facility_variate(copy_variate)

if __name__ == '__main__':
    path = "U:/facility-and-machines/input.json"
    MM = load_machines_from_json(path)
    facilitys = main(MM)
    facilitys.show()