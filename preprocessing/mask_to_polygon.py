import os
import cv2
import numpy as np

input_dir = 'decoration_textarea_masks'
output_dir = 'decoration_textarea_labels'

for j in os.listdir(input_dir):
    image_path = os.path.join(input_dir, j)
    # Load the color image
    mask = cv2.imread(image_path, cv2.IMREAD_COLOR)

    H, W, _ = mask.shape
    
    # Create empty images to store red and yellow regions
    red_mask = np.zeros((H, W), dtype=np.uint8)
    yellow_mask = np.zeros((H, W), dtype=np.uint8)

    # Iterate through the original image to identify red and yellow regions
    for y in range(H):
        for x in range(W):
            # Check if the pixel color is red
            if all(mask[y, x] == [0, 0, 255]):
                red_mask[y, x] = 255
            # Check if the pixel color is yellow
            elif all(mask[y, x] == [0, 255, 255]):
                yellow_mask[y, x] = 255

    # Find contours in the red mask
    contours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Convert the red contours to polygons and save the coordinates with class label "0"
    polygons_red = []
    for cnt in contours_red:
        if cv2.contourArea(cnt) > 200:
            polygon = []
            for point in cnt:
                x, y = point[0]
                print(point[0])
                polygon.append(x / W)
                polygon.append(y / H)
            polygons_red.append(polygon)

    # Find contours in the yellow mask
    contours_yellow, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Convert the yellow contours to polygons and save the coordinates with class label "1"
    polygons_yellow = []
    for cnt in contours_yellow:
        if cv2.contourArea(cnt) > 200:
            polygon = []
            for point in cnt:
                x, y = point[0]
                polygon.append(x / W)
                polygon.append(y / H)
            polygons_yellow.append(polygon)

    # Write the polygons to the label file
    with open('{}.txt'.format(os.path.join(output_dir, j)[:-4]), 'w') as f:
        # Write red polygons with class label "0"
        for polygon in polygons_red:
            f.write('0 ')
            for p in polygon:
                f.write('{} '.format(p))
            f.write('\n')
        
        # Write yellow polygons with class label "1"
        for polygon in polygons_yellow:
            f.write('1 ')
            for p in polygon:
                f.write('{} '.format(p))
            f.write('\n')
