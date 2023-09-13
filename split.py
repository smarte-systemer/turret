import os
import pandas as pd
import shutil
import random
import ast
import numpy as np

classes = ['balloons']
images = os.listdir('dataset/images')
number_of_images = len(images)

train_percent = 0.8
validation_percent = 0.1
test_percent = 0.1

# Python will always round down, test_number_images gets the remaining images
train_number_of_images = int(number_of_images * train_percent)
validation_number_of_images = int(number_of_images * validation_percent)
test_number_of_images = number_of_images - train_number_of_images - validation_number_of_images

def relative_coordinate(maximum: int, value: int):
   return np.float32(value/maximum)[0]

def move_files(amount: int, label: str, images: list):
  path = rf'dataset/{label}'
  all_meta = pd.read_csv(rf'dataset/balloon-data.csv')
  all_meta['bbox'] = all_meta['bbox'].apply(ast.literal_eval)

  print(f'Moving {amount} files to {path}')
  meta = pd.DataFrame(columns=['label', 'path', 'class', 'x_min', 'y_min','a','b',
                              'x_max', 'y_min', 'c', 'd'])
  print(all_meta.columns)
  for i in range(amount):
      file = random.choice(images)
      print(rf'dataset/images/{file}')
      print(rf'{path}/{file}')
      entry = all_meta.loc[all_meta['fname'] == file]
      for boxes in entry['bbox']:
        for box in boxes:
          meta.loc[len(meta)] = {'label': label.upper(), 'path': rf'{path}/{file}', 'class': 'balloon', 
                       'x_min': relative_coordinate(entry['width'] ,box['xmin']), 
                       'y_min': relative_coordinate(entry['height'], box['ymin']),
                       'x_max': relative_coordinate(entry['width'], box['xmax']), 
                       'y_max': relative_coordinate(entry['height'], box['ymax'])}
      #shutil.copy(rf'dataset/images/{file}', rf'{path}/{file}')
      images.remove(file)
  return meta, images

train_meta_data, images = move_files(train_number_of_images, 'train', images)
validation_meta, images = move_files(validation_number_of_images, 'validation', images)
test_meta, images = move_files(test_number_of_images, '/test', images)

meta = pd.concat([train_meta_data, validation_meta, test_meta])

meta.to_csv('dataset-meta.csv', index=False, header=False)