import cv2

import argparse
import tflite_support.task import core, processor, vision

from turret.motor import Motor

motor_driver = Motor(direction_pin=23, pulse_pin=18, 
                     frequency=2000, microstep='1')

def main(file_path: str, camera_id: int, number_of_threads: int, score_threshold: float):
    camera = cv2.VideoCapture(camera_id)
    base_options = core.Baseoptions(file_name=file_path,
                                    num_treads=number_of_threads)
    detection_options = processor.DetectionOptions(max_results=10, 
                                                   score_threshold=score_threshold)
    options = vision.ObjectDetectorOptions(base_options=base_options, 
                                            detection_options=detection_options)
    detector = vision.ObjectDetector.create_from_options(options)

    while camera.isOpened():
        result, image = camera.read()
        if not result:
            print(f"Unable to open camera{camera_id}")
            exit()
        image = cv2.flip(image, 1)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        input_tensor = vision.TensorImage.create_from_array(rgb_image)
        detection_result = detector.detect(input_tensor)

        if detection_result.any():
            object_x = (detection_result[0].ounding_box.origin_x + detection_result[0].bounding_box.width)/2
            object_x = round(object_x)
            camera_center = round(camera_center)
            camera_center = camera.get(cv2.CAP_PROP_FRAME_WIDTH)/2 
            
            x_axis_diff =  camera_center - object_x
            motor_driver.move_to_target(object_x, camera_center, 10)
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--model',
                        help='File path of the model',
                        required=True)
    parser.add_argument('-number_of_threads',
                        help='The number of threads to be run',
                        type=int,
                        default=3)
    parser.add_argument('--camera_id',
                        help='Id of camera to use',
                        default=0)
    parser.add_argument('--score_threshold',
                        help='Threshold for detection(0-1)',
                        default=0.7)
    arguments = parser.parse_args()
    main(arguments.model, arguments.camera_id, arguments.number_of_threads, 
         arguments.score_threshold)
