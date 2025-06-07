import os
import pandas as pd


src_dir = os.path.dirname(__file__)
repo_dir = os.path.dirname(src_dir)
data_dir = os.path.join(repo_dir, "data")
input_file = os.path.join(data_dir, "input.csv")
output_file = os.path.join(data_dir, "outputs.csv")


def load_inputs():
    df = pd.read_csv(input_file)
    return df.to_dict(orient="records")


def write_outputs(outputs):
    df = pd.DataFrame(outputs)
    df.to_csv(output_file, index=False)
