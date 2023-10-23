import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision

#from turret.sharedvar import SharedVar
import sharedvar as SharedVar
class Detector:
    def __init__(self, frame: SharedVar, coordinates: SharedVar,model: str = '../object_detection/models/turret-syndrome-efficientdet_lite1.tflite',
                 threads: int = 3, max_results: int = 10, score_threshold: float = 0.7) -> None:
        self.frame = frame
        self.coordinates = coordinates
        base_options = core.BaseOptions(
                        file_name=model, num_threads=threads)
        detection_options = processor.DetectionOptions(
                            max_results=max_results, score_threshold=score_threshold)
        options = vision.ObjectDetectorOptions(base_options=base_options, 
                                               detection_options=detection_options)
        self.model = vision.ObjectDetector.create_from_options(options)


    def set_coordinates(self, image: cv2.typing.MatLike):
        """Sets coordinates for detected objects in SharedVar object
           Format: ((x1,y1,x2,y2), class_name)

        Args:
            image: frame from stream to process
        """

        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        tensor = vision.TensorImage.create_from_array(image)
        result = self.model.detect(tensor)
        detections = [None]*len(result.detections)
        for i in range(result.detections):
            detections[i] = ((result.detections[i].bounding_box.origin_x,
                              result.detections[i].bounding_box.origin_y,
                              result.detections[i].bounding_box.origin_x + result.detections[i].bounding_box.width,
                              result.detections[i].bounding_box.origin_y + result.detections[i].bounding_box.height), 
                              result.categories[i].category_name)
        self.coordinates.set_var(detections)

    def run(self):
        """Function to continuously run.
        """
        while True:
            self.frame.cv.acquire()
            try:
                image = self.frame.get_var()
                self.frame.cv.notify()
            finally:
                self.frame.cv.release()
            self.set_coordinates(self.frame.get_var())
    
