import os
import re #Regex
import pandas as pd
import numpy as np

"""Pathing"""
script_list = []
script_names = ['12-Monkeys','Carrie','Catch-Me-If-You-Can' ,'Cell,-The' ,'Kafka']

script = os.path.join(os.getcwd(), 'scripts\\12-Monkeys.txt')
script2 = os.path.join(os.getcwd(), 'scripts\\Carrie.txt')
script3 = os.path.join(os.getcwd(), 'scripts\\Catch-Me-If-You-Can.txt')
script4 = os.path.join(os.getcwd(), 'scripts\\Cell,-The.txt')
script5 = os.path.join(os.getcwd(), 'scripts\\Kafka.txt')

# Adding multiple scripts into script_list
script_list.extend([script,script2,script3, script4,script5])

# TODO: Need to pull all scripts (currently 700's). Use glob to accomplish
# TODO: Pull from springfield source
# https://www.springfieldspringfield.co.uk/movie_scripts.php?order=0

"""Word counts & lists"""
god_count = 0
jesus_count = 0
christ_count = 0

god_series = []
jesus_series = []
christ_series = []

"""Counting words"""
for script in script_list:
    with open(script, 'r', encoding="utf-8") as file:
        data = file.read()

        # /b is an empty string
        # Using re.finditer, counting all the matches in the scripts
        god_tick = sum(1 for match in re.finditer(r"\bGod\b", data))
        jesus_tick = sum(1 for match in re.finditer(r"\bJesus\b", data))
        christ_tick = sum(1 for match in re.finditer(r"\bChrist\b", data))

        print(f"God: {god_tick}, Jesus: {jesus_tick}, Christ: {christ_tick} in this script")

        god_series.append(god_tick)
        jesus_series.append(jesus_tick)
        christ_series.append(christ_tick)

        god_count += god_tick
        jesus_count += jesus_tick
        christ_count += christ_tick

        print(f"God shows up {god_count} times, Jesus {jesus_count}, and Christ {christ_count}")
print(f"God list: {god_series} times, Jesus list: {jesus_series}, and Christ list: {christ_series}")

"""Dataframe"""
data = {'scripts': script_names, 'god_count': god_series,'jesus_count': jesus_series,'christ_count': christ_series}
df = pd.DataFrame(data)
df.to_csv(os.path.join(os.getcwd(), 'movies.csv'), index=False)
