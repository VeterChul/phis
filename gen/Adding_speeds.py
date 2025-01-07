from random import *

def generation(looking, values, js):
    if looking == "v++":
        v1 = randint(values["v++"][0], values["v++"][1])
        v2 = randint(values["v++"][0], values["v++"][1])
        text = js["v++"][0].replace("v1", str(v1)).replace("v2", str(v2))
        return text, v2+v1
    if looking == "v++":
        v1 = randint(values["v--"][0], values["v--"][1])
        v2 = randint(values["v--"][0], values["v--"][1])
        text = js["v--"][0].replace("v1", str(v1)).replace("v2", str(v2))
        return text, v2+v1
    if looking == "v-":
        v1 = randint(values["v-"][0], values["v-"][1])
        v2 = randint(values["v-"][0], values["v-"][1])
        text = js["v-"][0].replace("v1", str(v1)).replace("v2", str(v2))
        return text, v1-v2
    if looking == "t":
        v1 = randint(values["v-"][0], values["v-"][1])
        v2 = randint(values["v-"][0], v1)
        l = randint(values["l"][0], values["l"][1])
        text = js["t"][0].replace("v1", str(v1)).replace("v2", str(v2)).replace("l", str(l))
        return text, l / (v1-v2)
    if looking == "l":
        v1 = randint(values["v-"][0], values["v-"][1])
        v2 = randint(values["v-"][0], v1)
        t = randint(values["t"][0], values["t"][1])
        text = js["l"][0].replace("v1", str(v1)).replace("v2", str(v2)).replace("t", str(t))
        return text, (v1-v2) * t
    if looking == "v":
        v = randint(values["v"][0], values["v"][1])
        t = randint(values["t"][0], values["t"][1])
        l = randint(values["l"][0], values["l"][1])
        text = js["v"][0].replace("v", str(v)).replace("t", str(t)).replace("l", str(l))
        return text, v + l / t