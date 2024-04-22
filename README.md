# LayoutAnalysis
For Challenge 3.

Colab: https://colab.research.google.com/drive/1yfSLtSZYp8TQJdX5pLjZUcZncG_rf1DX?usp=sharing
Google drive with data: https://drive.google.com/drive/folders/13eXCmo8-EKIOvTUKDMxOoj2ZYhuQ_X0I?usp=drive_link
【Part A】
For decorations and text area.
1. Preprocessing
From groundtruth, decoration:(255,0,0); text_area:(255,255,0).

2. Generate label files(txt)
class 0: decoration
class 1:text_area
format: <class_index> <x1> <y1> ... (they are normalized (0~1) by X/W, Y/H.

3. File Folder Structure

4. train model [model = YOLO('yolov8n-seg.pt')]
   validate model

5. Prediction (one image by now)

6. Evaluation

【Part B】
For text lines and initial capital segmentatioin...


【Part C】
Adjust models to get better results...
