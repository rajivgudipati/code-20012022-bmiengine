import pandas as pd
import numpy as np
import yaml
import json

CONFIG_FILE = r'../config/bmi_config.yml'

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def convert_json_to_dataframe(jsonData):
    df = pd.DataFrame(jsonData)
    return df

def read_yml_config():
    with open(CONFIG_FILE, 'r') as stream:
        cfg = yaml.safe_load(stream)
    return cfg

if __name__ == '__main__':
    output = read_yml_config()
    print (output)