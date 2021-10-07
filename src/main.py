from read_config_of_machienes import load_machines_from_json
from write_config_of_machienes import write_machines_to_json
from alghoritm import optimize


def main():
    # path_input = "U:/facility-and-machines/input.json"
    path_input = "U:/facility-and-machines/src/Web/ConfigPacks/123.json"
    # path_output = "U:/facility-and-machines/output.json"
    path_output =  "U:/facility-and-machines/src/Web/ResultPacks/123.json"
    configs_data = load_machines_from_json(path_input)
    best_facility = optimize(configs_data)
    write_machines_to_json(path_output, best_facility)
    print("Done!")


if __name__ == '__main__':
    main()
