import requests
import pandas as pd
import matplotlib.pyplot as plt


def esg_image_init():
    URL = "http://api:8080/esg"

    r = requests.get(url=URL)

    data = r.json()

    E = 0
    S = 0
    G = 0

    for i in data:
        if i["esg"] == "ENVIRONMENTAL":
            E += 1
        if i["esg"] == "SOCIAL":
            S += 1
        if i["esg"] == "GOVERNMENTAL":
            G += 1

    df = pd.json_normalize(data)

    plt.bar(["Environmental", "Social", "Governmental"], [E, S, G])
    plt.title("problems")
    plt.xlabel("ESG")
    plt.ylabel("numbers")

    plt.savefig("./static/esg.svg", format="svg")
