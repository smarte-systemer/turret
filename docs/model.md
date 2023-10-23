# Detector
Detector models were created using this [Jupyter notebook](https://dev.azure.com/smarte-systemer/turret/_git/turret?path=/object_detection/training/Turret_syndrom_training.ipynb).

<style>
  table {
    border-collapse: collapse;
    width: 100%;
    color: var(--color-content-foreground);
    font-family: Arial, sans-serif;
    font-size: 14px;
    text-align: left;
    border-radius: 5px;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    margin: auto;
    margin-top: 50px;
    margin-bottom: 50px;
  }
table th {
  background-color: var(--color-api-name);
  color: #fff;
  font-weight: bold;
  padding: 1px;
  text-transform: uppercase;
  letter-spacing: 1px;
  } 

table tr:hover td {
  background-color: var(--color-link);
  opacity: 90%;
}
</style>

<table class="styled-table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Frames per second</th>
      <th>Model based on</th>
      <th>Path</th>
    </tr>
  </thead>
  <tbody>
    <tr class="active-row">
      <td>f16-turret-syndrome-efficientdet_lite1.tflite</td>
      <td style="text-align: center; vertical-align: middle;">??</td>
      <td><a href="https://tfhub.dev/tensorflow/efficientdet/lite1/detection/1" style="color:black">efficientdet-1</a></td>
      <td>object_detection/models/f16-turret-syndrome-efficientdet_lite1.tflite</td>
    </tr>
    <tr class="active-row">
     <td>f16-turret-syndrome-efficientdet_lite2.tflite</td>
      <td style="text-align: center; vertical-align: middle;">??</td>
      <td>
      <a href="https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1" style="color:black">efficientdet-2</a></td>
      <td>object_detection/models/f16-turret-syndrome-efficientdet_lite2.tflite</td>
    </tr>
    <tr class="active-row">
     <td>turret-syndrome-efficientdet_lite1.tflite</td>
      <td style="text-align: center; vertical-align: middle;">6</td>
      <td> <a href="https://tfhub.dev/tensorflow/efficientdet/lite1/detection/1" style="color:black">efficientdet-1</a></td>
      <td>object_detection/models/turret-syndrome-efficientdet_lite1.tflite</td>
    </tr>
    <tr class="active-row">
      <td>turret-syndrome-efficientdet_lite2.tflite</td>
      <td style="text-align: center; vertical-align: middle;">??</td>
      <td><a href="https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1" style="color:black">efficientdet-2</a></td>
      <td>object_detection/models/turret-syndrome-efficientdet_lite2.tflite</td>
    </tr>
    </tr>
  </tbody>
</table>


```{eval-rst}
.. automodule:: turret.detector
   :members:
   :undoc-members:
   :show-inheritance:
``` 