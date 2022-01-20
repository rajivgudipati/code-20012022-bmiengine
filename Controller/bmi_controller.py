from flask import Flask, request, Response
from utils.bmi_utils import convert_json_to_dataframe, read_yml_config, NpEncoder
import pandas as pd
import json
import logging

app = Flask('bmi_controller')

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def get_cat_risk_info(val):
    bmi_info = read_yml_config()
    bmi_info = bmi_info['bmi_info']
    for level in bmi_info.values():
        if (level['st_range'] and val >= level['st_range']) and (level['ed_range'] and val <= level['ed_range']):
            cat = level['cat']
            risk = level['risk']
            return (cat, risk)
        elif (not level['st_range']) and (val <= level['ed_range']):
            cat = level['cat']
            risk = level['risk']
            return (cat, risk)
        elif  (not level['ed_range']) and (val >= level['st_range']):
            cat = level['cat']
            risk = level['risk']
            return (cat, risk)
        else:
            continue
    return ('','')

def populateBMI(df):
    df['bmi'] = round(df['WeightKg'] / (df['HeightCm'] / 100), 2)
    return df

def populateCategory(df):
    df['bmi_category'] = df['bmi'].apply(lambda val: get_cat_risk_info(val))
    df[['bmi_catg', 'health_risk']] = pd.DataFrame(df['bmi_category'].tolist())
    df.drop('bmi_category', inplace=True, axis=1)
    return df

def bmi_summary(df):
    bmi_catg_stats = df['bmi_catg'].value_counts()
    health_risk_stats = df['health_risk'].value_counts()
    return {**dict(bmi_catg_stats), **dict(health_risk_stats)}

@app.route('/api/v1/bmiengine/calculatebmi', methods=['POST'])
def receive_persons_info():
    try:
        persons_info_json = request.get_json()

        persons_info_df = convert_json_to_dataframe(persons_info_json)
        persons_info_df = populateBMI(persons_info_df)
        persons_info_df = populateCategory(persons_info_df)
        output = persons_info_df.to_dict('records')
        response = app.response_class(response=json.dumps(output),
                                      status=200,
                                      mimetype='application/json')
        return response
    except Exception as e:
        log.error(e)
        return Response(status=500)

@app.route('/api/v1/bmiengine/calculatestats', methods=['POST'])
def receive_persons_summary():
    try:
        persons_info_json = request.get_json()

        persons_info_df = convert_json_to_dataframe(persons_info_json)
        persons_info_df = populateBMI(persons_info_df)
        persons_info_df = populateCategory(persons_info_df)
        output = bmi_summary(persons_info_df)
        response = app.response_class(response=json.dumps(output, cls=NpEncoder),
                                      status=200,
                                      mimetype='application/json')
        return response
    except Exception as e:
        log.error(e)
        return Response(status=500)

if __name__ == '__main__':
    app.run(port=8090)