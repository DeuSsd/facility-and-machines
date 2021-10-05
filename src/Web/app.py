from flask import Flask, render_template, request, url_for, flash, redirect
from markupsafe import escape

import glob
from random import randint

from src.Web.generate_configs import generateRandomConfigs
from src.read_config_of_machienes import read_json

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567'


@app.route('/', methods=('GET', 'POST'))
def index():
    """
    Start page to generate machines with configurations or start creating the solution
    """
    files = glob.glob("./ConfigPacks/*.json")
    if request.method == 'POST':
        if "solution" in request.form:
            # Где-то тут надо получить результирующий json
            # datasetName =
            json = read_json("ConfigPacks/" + request.form['datasetName'])
            return render_template('result.html', dataset=json, randint=randint)
        elif "create" in request.form:
            generateRandomConfigs(request.form['ConfigurationPackName'],
                                  request.form['NumberOfMachines'],
                                  request.form['MaxNumConf'])
            files = glob.glob("./ConfigPacks/*.json")

    return render_template('index.html', files=files)



if __name__ == '__main__':
    app.run()
