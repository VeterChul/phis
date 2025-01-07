from random import *

def generation(looking, values, js):
    if looking == "c":
        v1 = randint(values["v"][0], values["v"][1])
        v2 = randint(values["v"][0], values["v"][1])
        l1 = randint(values["l"][0], values["l"][1])
        l2 = randint(values["l"][0], values["l"][1])
        text = js["c"][0].replace("v1", str(v1)).replace("l1", str(l1)).replace("v2", str(v2)).replace("l2", str(l2))
        return text, (l1 + l2)/((l1/v1)+(l2/v2))
    if looking == "l":
        v1 = randint(values["v"][0], values["v"][1])
        v2 = randint(values["v"][0], values["v"][1])
        l1 = randint(values["l"][0], values["l"][1])
        c = randint(values["c"][0], values["c"][1])
        t1 = l1 / v1
        text = js["l"][0].replace("v1", str(v1)).replace("l1", str(l1)).replace("v2", str(v2)).replace("c", str(c))
        return text, (c*t1 - l1)/(1 - c/v2)
    if looking == "t":
        v1 = randint(values["v"][0], values["v"][1])
        v2 = randint(values["v"][0], values["v"][1])
        l1 = randint(values["l"][0], values["l"][1])
        c = randint(values["c"][0], values["c"][1])
        t1 = l1 / v1
        text = js["t"][0].replace("v1", str(v1)).replace("l1", str(l1)).replace("v2", str(v2)).replace("c", str(c))
        return text, (c*t1 - l1)/(v2 - c)
    if looking == "v":
        v1 = randint(values["v"][0], values["v"][1])
        l2 = randint(values["l"][0], values["l"][1])
        l1 = randint(values["l"][0], values["l"][1])
        c = randint(values["c"][0], values["c"][1])
        t1 = l1 / v1
        text = js["v"][0].replace("v1", str(v1)).replace("l1", str(l1)).replace("l2", str(l2)).replace("c", str(c))
        return text, (c*l2)/(l1+l2 - c * t1)
    
    
    

    
    

