from random import *

def generation(looking, values, js):
    if looking == "l":
        v = randint(values["v"][0], values["v"][1])
        t = randint(values["t"][0], values["t"][1])
        text = js["l"][0].replace("v", str(v)).replace("t", str(t))
        return text, v * t
    if looking == "v":
        l = randint(values["v"][0], values["v"][1])
        t = randint(values["t"][0], values["t"][1])
        text = js["v"][0].replace("l", str(l)).replace("t", str(t))
        return text, l / t
    if looking == "t":
        v = randint(values["v"][0], values["v"][1])
        l = randint(values["t"][0], values["t"][1])
        text = js["t"][0].replace("v", str(v)).replace("l", str(l))
        return text, l / v
    

    
    

