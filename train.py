import numpy as np
import os

from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker.config import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)

spec = model_spec.get('efficientdet_lite0')

train, validation, test = object_detector.DataLoader.from_csv('dataset/balloon-data.csv')

model = object_detector.create(train, model_spec=spec, batch_size=8, train_whole_model=True,
                               validation_data=validation)

model.evaluate(test)

model.export(export_dir='.')

model.evaluate_tflite('model.tflite', test)
