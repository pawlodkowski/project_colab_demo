import pandas as pd
import matplotlib.pyplot as plt
import time
import random

df = pd.read_csv("data/monday.csv")
states = ["entrance", "fruits", "dairy", "spices", "checkout"]


class Customer:
    pass


if __name__ == "__main__":
    while True:
        
        print('before you run anything, remember: may the loop be with you')
        print('my young padavan')
        
        loc = random.choices(states)[0]
        if loc == "checkout":
            print("Checked out!")
            break
        print(f"Customer is at {loc}")

        time.sleep(1)
