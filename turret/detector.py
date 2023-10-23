import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
from detection import Detection
#from turret.sharedvar import SharedVar
import sharedvar as SharedVar
class Detector:
    def __init__(self, frame: SharedVar, coordinates: SharedVar,model: str = '../object_detection/models/turret-syndrome-efficientdet_lite1.tflite',
                 threads: int = 4, max_results: int = 10, score_threshold: float = 0.7) -> None:
        self.frame = frame
        self.coordinates = coordinates
        base_options = core.BaseOptions(
                        file_name=model, num_threads=threads)
        detection_options = processor.DetectionOptions(
                            max_results=max_results, score_threshold=score_threshold)
        options = vision.ObjectDetectorOptions(base_options=base_options, 
                                               detection_options=detection_options)
        self.model = vision.ObjectDetector.create_from_options(options)
        print("Model: init done")

    def set_coordinates(self, image: cv2.typing.MatLike):
        """Sets coordinates for detected objects in SharedVar object
           Format: ((x1,y1,x2,y2), class_name)

        Args:
            image: frame from stream to process
        """
       # print("Model: Process frame")
        #image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        tensor = vision.TensorImage.create_from_array(image)
        result = self.model.detect(tensor)
        detections = [Detection]*len(result.detections)
        for i in range(len(result.detections)):
            detections[i] = Detection(
                (result.detections[i].bounding_box.origin_x, result.detections[i].bounding_box.origin_y),
                (result.detections[i].bounding_box.origin_x + result.detections[i].bounding_box.width, 
                 result.detections[i].bounding_box.origin_y + result.detections[i].bounding_box.height),
                 "Ballon"
                )
            # detections[i] = [result.detections[i].bounding_box.origin_x,
            #                   result.detections[i].bounding_box.origin_y,
            #                   result.detections[i].bounding_box.origin_x + result.detections[i].bounding_box.width,
            #                   result.detections[i].bounding_box.origin_y + result.detections[i].bounding_box.height, 
            #                   "ballon"]
                              #result.categories[i].category_name)
         #   print("########Model: Detection")
        self.coordinates.set_var(detections)

    def run(self):
        """Function to continuously run.
        """
        while True:
            image = None
#            self.frame.cv.acquire()
 #           try:
  #              image = self.frame.get_var()
   #             print("Model: Image found")
    #            self.frame.cv.notify()
     #       finally:
     #           self.frame.cv.release()
            image = self.frame.get_var()
            if image is not None:
          #      print("Model: Setting coordinate")
                self.set_coordinates(image)
    
