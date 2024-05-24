""" File to get all the routes of the api

This saves a csv file with all the routes of the api in the data folder
"""
import json
import pandas as pd
# a dictionary
with open(
    "prod-insol-insights-api.json",
) as f:
    data = json.load(f)

all_paths = data["paths"]
all_paths = list(all_paths.keys())

# sort paths
all_paths = sorted(all_paths)

# save to csv
with open("prod-insol-insights-api.csv", "w") as f:
    for path in all_paths:
        f.write(f"{path}\n")

paths_df = pd.DataFrame(all_paths, columns=["path"])
paths_df["path_reduced"] = paths_df["path"]

for s in [
    "/all",
    "/events",
    "/stream",
    "/latest",
    "/rates",
    "/daily",
    "/weekly",
    "/day-ahead",
    "/yearly",
    "/total",
    "/summary",
    "/stream",  # this is a repeat, but needed
]:
    paths_df["path_reduced"] = paths_df["path_reduced"].apply(lambda x: x.replace(s, ""))

# remove any paramters
paths_df["path_reduced"] = paths_df["path_reduced"].apply(lambda x: x.split("/{")[0])

# remove last parameter
def remove_last(x):
    """ Remove last parameter

    Done remove if only one later deep, like "/temperature"
    """
    x_split = x.split("/")
    if len(x_split) > 2:
        return "/".join(x_split[:-1])
    else:
        return x


paths_df["path_reduced"] = paths_df["path_reduced"].apply(lambda x: remove_last(x))

# take unique
unique_paths = paths_df["path_reduced"].unique()

# check to see if route is in any other routes
new_paths = []
for i, row in paths_df.iterrows():
    if any([row.path_reduced in p for p in unique_paths if p != row.path_reduced]):
        new_paths.append(f"{row.path_reduced}/main.py")
    else:
        new_paths.append(f"{row.path_reduced}.py")
paths_df["python_file"] = new_paths

# save to csv
paths_df.to_csv("data/routes.csv", index=False)
