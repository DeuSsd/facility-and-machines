from read_config_of_machienes import load_machines_from_json
from src.facility_and_machines import CollectionOfMachines
from write_config_of_machienes import write_machines_to_json
from alghoritm import optimize

def step_by_step(path_output: str, configs_data: CollectionOfMachines):
    optomize_generator = optimize(configs_data)
    try:
        while True:
            best_facility = next(optomize_generator)
            best_facility.show()
            # print(">>>")
            write_machines_to_json(path_output, best_facility)
    except StopIteration:
        print("Done!")

def main():
    # path_input = "U:/facility-and-machines/input.json"
    path_input = "U:/facility-and-machines/src/Web/ConfigPacks/5.json"
    # path_output = "U:/facility-and-machines/output.json"
    path_output =  "U:/facility-and-machines/src/Web/ResultPacks/5.json"
    configs_data = load_machines_from_json(path_input)
    step_by_step(path_output,configs_data)



if __name__ == '__main__':
    main()
