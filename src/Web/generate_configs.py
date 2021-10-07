import json
from random import randint
from math import modf


def generateRandomConfigs(jsonName="test", numMachines="1", maxNumConf="5"):
    """
    Create some json file
    """
    configs = {"Count of Machine": int(numMachines), "List of machine": list()}
    for i in range(int(numMachines)):
        randAmount = randint(1, int(maxNumConf))
        machine = {"Title of machine": "M" + str(i), "Amount of configs": randAmount, "Machines": list()}
        rh = randint(1, 15)
        rh_list = list()
        rw = randint(1, 15)
        rw_list = list()
        rS = rh * rw
        for confCount in range(randAmount):
            rh = randint(1, 15)
            if rh in rh_list:
                break
            else:
                rh_list.append(rh)
            for patch in range(30):
                if patch % 2 == 0:
                    rh = rh - patch
                else:
                    rh = rh + patch
                if rh > 0:
                    rw = rS / rh
                    if modf(rw)[0] == 0.0:
                        rw = int(rw)
                        break
            if rw in rw_list:
                break
            else:
                rw_list.append(rw)
            machine["Machines"].append({"h": rh, "w": rw})
        configs["List of machine"].append(machine)

    file = open("ConfigPacks/" + jsonName + ".json", "w")
    json.dump(configs, file)
    file.close()
