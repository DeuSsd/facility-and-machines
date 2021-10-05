import json
from random import randint
from math import modf


def generateRandomConfigs(jsonName="test", numMachines="1", maxNumConf="5"):
    """
    Create some json file
    """
    configs = {"Count of Machine": int(numMachines), "List os machine": list()}
    for i in range(int(numMachines)):
        randAmount = randint(1, int(maxNumConf))
        machine = {"Title of machine": "M" + str(i), "Amount of configs": randAmount, "Machines": list()}
        rh = randint(1, 15)
        rw = randint(1, 15)
        rS = rh * rw
        for machineCount in range(randAmount):
            while True:
                rh = randint(1, 15)
                rw = rS / rh
                if type(rw) == int():
                    break
            machine["Machines"].append({"h": rh, "w": rw})
        configs["List os machine"].append(machine)

    file = open("ConfigPacks/" + jsonName + ".json", "w")
    json.dump(configs, file)
    file.close()
