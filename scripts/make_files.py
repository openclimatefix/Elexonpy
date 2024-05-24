""" SCript to make the raw python files"""

import pandas as pd
import os

main_dir = "pyelexon"
elexon_url = "https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api"

paths = pd.read_csv("data/routes.csv")

# make main directory
if not os.path.exists(main_dir):
    os.mkdir(main_dir)

# make the files by looping over routes
for i, row in paths.iterrows():
    path = row.path
    file = row.python_file

    # make the file
    file = f"{main_dir}/{file}"
    if not os.path.exists(file):

        dir = os.path.dirname(file)
        if not os.path.exists(dir):
            os.makedirs(dir)

        with open(file, "w") as f:
            f.write(f'""" Functions for {row.path_reduced} """\n\n')
            f.write(f'""" \n See {elexon_url} for more information \n')
            f.write(f'This file should contain the following routes:\n"""\n\n')

    # add the path to the file
    with open(file, "a") as f:
        f.write(f"# Path: {path}\n")
