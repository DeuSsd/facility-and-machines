from flask import Flask, render_template, request, url_for, flash, redirect
import glob
from random import randint

from src.Web.generate_configs import generateRandomConfigs
from src.read_config_of_machienes import read_json
from src.read_config_of_machienes import load_machines_from_json
from src.write_config_of_machienes import write_machines_to_json
from src.alghoritm import optimize

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567'

RESULT_NAME = dict()


@app.route('/', methods=('GET', 'POST'))
def index():
    """
    Start page to generate machines with configurations or start creating the solution
    """
    files = glob.glob("./ConfigPacks/*.json")
    if request.method == 'POST':
        if "solution" in request.form:
            path_input = request.form['datasetName']
            f = open("temp.txt", "w")
            f.write(path_input)
            f.close()
            json = find_result(path_input)
            if json['Facility']['w'] > json['Facility']['h']:
                k = 800 / json['Facility']['w']
            else:
                k = 500 / json['Facility']['h']
            par_vis = False
            return render_template('result.html', dataset=json, randint=randint, k=k, par_vis=par_vis)
        elif "create" in request.form:
            generateRandomConfigs(request.form['ConfigurationPackName'],
                                  request.form['NumberOfMachines'],
                                  request.form['MaxNumConf'])
            files = glob.glob("./ConfigPacks/*.json")
        elif "show_parameters" in request.form:
            f = open("temp.txt", "r")
            path_input = f.read()
            f.close()
            json = find_result(path_input)
            if json['Facility']['w'] > json['Facility']['h']:
                k = 800 / json['Facility']['w']
            else:
                k = 500 / json['Facility']['h']
            if request.form['show_parameters'] == "show":
                par_vis = True
            else:
                par_vis = False
            return render_template('result.html', dataset=json, randint=randint, k=k, par_vis=par_vis)

    return render_template('index.html', files=files)


def find_result(path_input: str) -> dict:
    # path_output = "./ResultPacks/" + request.form['datasetName'][14:]
    path_output = "./ResultPacks/" + path_input[14:]
    configs_data = load_machines_from_json(path_input)
    best_facility = optimize(configs_data)
    write_machines_to_json(path_output, best_facility)

    json_result = read_json(path_output)  # result
    return json_result


if __name__ == '__main__':
    app.run()
