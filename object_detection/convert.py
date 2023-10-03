import pandas as pd
import ast
import json

df = pd.read_csv(r'dataset/balloon-data.csv')

output = {
    "version": 1,
    "type": "bounding-box-labels",
    "boundingBoxes": {}
    }

df['bbox'] = df['bbox'].apply(ast.literal_eval)

for index, row in df.iterrows():
    bounding = []

    for box in row['bbox']:
        bounding.append({'label': 'balloon',
                    'x': box['xmin'],
                    'y': box['ymin'],
                    'width': box['xmax'] - box['xmin'],
                    'height': box['ymax'] - box['ymin']})
    output['boundingBoxes'][f"{row['fname']}"] =  bounding

with open('dataset/bounding_boxes.labels', 'w') as f:
    json.dump(output, f)
