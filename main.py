import numpy as np
import json
import os
import shutil
from conf import prog_dir
from random import *
from sklearn.utils import shuffle

def name_job(prog_dir, js):
    if "job_name" in js:
        if js["job_name"] in os.listdir(prog_dir):
            shutil.rmtree(f"{prog_dir}{js["job_name"]}")
        return js["job_name"]
    else:
        l = os.listdir(prog_dir)
        max = 0
        for i in l:
            try:
                if int(i) > max:
                    max = int(i)
            except:
                pass
        return str(max + 1)

# считывание сида и листа задач

f  = open(f"{prog_dir}sid.json", "r")
sid  = json.load(f)
f.close()

f  = open(f"{prog_dir}list_of_tasks.json", "r")
list_of_tasks  = json.load(f)
f.close()

#генерация 

list_ret = {
    "tasks_ans":[]
}

for i in sid["list"]:
    task = list_of_tasks[i["name"]]
    if "quantity" in i:
        r = int(i["quantity"])
    else:
        r = 1
    for j in range(r):
        exec(task["kod"])
        if "values" in i:
            values = i["values"]
        else:
            values = task["standard_values"]
        s = f"an = {i["name"]}('{i["looking"]}',{values}, {task})"
        exec(s)
        list_ret["tasks_ans"].append({
            "text" : an[0],
            "ans" : an[1]
        })

if "random" in sid:
    if sid["random"]:
        list_ret["tasks_ans"] =  shuffle(list_ret["tasks_ans"])

print(list_ret)

#запись

name = name_job(prog_dir, sid)

os.mkdir(f"{prog_dir}{name}")
f = open(f"{prog_dir}{name}/job.json", "a")
f.write(str(list_ret).replace("'", '"'))
f.close()