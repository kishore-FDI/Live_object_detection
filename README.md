# Project Title: Real-time Object Detection using YOLO and OpenCV

## Description
This project is about implementing a real-time object detection system using the YOLO (You Only Look Once) model trained on the IP102 dataset. The model was initialized with random weights and then trained on the dataset using a Jupyter notebook. The trained model was then used to perform object detection on live camera feed using OpenCV in a Python script.

## Dataset
The model was trained on the [IP102 dataset](https://paperswithcode.com/dataset/ip102), a large scale benchmark dataset for insect pest recognition. It is a comprehensive dataset that includes 75,000 images, covering 102 insect pest species.

## Model
The object detection model used in this project is YOLO (You Only Look Once), a popular object detection algorithm known for its speed and accuracy. The model was initialized with random weights before training.

## Dependencies
- Python 3.6 or later
- OpenCV
- Ultralytics (YOLO)
- Jupyter Notebook

## Setup & Installation
1. Clone the repository.
2. Install the dependencies using pip:
    ```
    pip install -r requirements.txt
    ```
3. Download the IP102 dataset and place it in the 'data' directory.
4. Run the Jupyter notebook to train the YOLO model on the IP102 dataset.

## Usage
After training the model, you can run the object detection script on your live camera feed:
```
python detect.py
```

## Results
The trained model was able to successfully detect objects in real-time on a live camera feed. The detection results were displayed using OpenCV.

## Future Work
- Improve the model's accuracy by fine-tuning the hyperparameters.
- Test the model on different datasets.
- Implement additional features such as tracking.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- The YOLO model was used for object detection.
- The IP102 dataset was used for training the model.
- OpenCV was used for handling video input and displaying the detection results.
