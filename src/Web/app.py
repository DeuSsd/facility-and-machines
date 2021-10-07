from flask import Flask, render_template, request, url_for, flash, redirect
import glob
from random import randint
from itertools import tee
import redis

from flask import Flask, session
from flask_redis import FlaskRedis

from src.Web.generate_configs import generateRandomConfigs
from src.facility_and_machines import CollectionOfMachines
from src.read_config_of_machienes import read_json
from src.read_config_of_machienes import load_machines_from_json
from src.write_config_of_machienes import write_machines_to_json
from src.alghoritm import optimize

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567'
SESSION_TYPE = 'filesystem'

app.config.from_object(__name__)

PATH_INPUT: str
PATH_OUTPUT: str


@app.route('/', methods=('GET', 'POST'))
def index():
    """
    Start page to generate machines with configurations or start creating the solution
    """
    files = glob.glob("./ConfigPacks/*.json")
    print("s")
    if request.method == 'POST':
        print("p")
        if "solution" in request.form:
            session["PATH_INPUT"] = request.form['datasetName']
            print(session["PATH_INPUT"])
            session["PATH_OUTPUT"] = "./ResultPacks/" + request.form['datasetName'][14:]

        print("g")
        print(request.form)
        if "solution" in request.form:
            print("s")
            configs_data = load_machines_from_json(session["PATH_INPUT"])
            optomize_generator = optimize(configs_data)
            try:

                optomize_generator, other = tee(optomize_generator)
                while True:
                    best_facility = next(other)
                    best_facility.show()
                    write_machines_to_json(session["PATH_OUTPUT"], best_facility)
            except StopIteration:
                print("Done!")
                optomize_generator, other = tee(optomize_generator)
                r = redis.Redis()
                r.mset({"generator":other})
                print(r.get("generator"))
                # print(session["generator"])
            # write_machines_to_json(path_output, best_facility)
            json = read_json(session["PATH_OUTPUT"])

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
            return render_template('index.html', files=files)
        elif "next" in request.form:
            print("n")
            try:
                best_facility = next(session["generator"])
                best_facility.show()
                write_machines_to_json(session["PATH_OUTPUT"], best_facility)
            except StopIteration:
                print("Done!")
            json = read_json(session["PATH_OUTPUT"])
            if json['Facility']['w'] > json['Facility']['h']:
                k = 800 / json['Facility']['w']
            else:
                k = 500 / json['Facility']['h']
            par_vis = False
            return render_template('result.html', dataset=json, randint=randint, k=k, par_vis=par_vis)
    return render_template('index.html', files=files)


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


def find_result() -> dict:
    path_input = request.form['datasetName']
    path_output = "./ResultPacks/" + request.form['datasetName'][14:]
    configs_data = load_machines_from_json(path_input)
    best_facility = optimize(configs_data)
    write_machines_to_json(path_output, best_facility)

    json_result = read_json(path_output)  # result
    return json_result


if __name__ == '__main__':
    app.run()
