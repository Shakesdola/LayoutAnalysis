#Using the normalized coordinate files to compute the IoU of corresponding instances of each classes.

def read_coordinates(file_path):
    """Read normalized coordinates from a file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    coordinates = []
    for line in lines:
        parts = line.strip().split()
        class_index = int(parts[0])
        points = [float(x) for x in parts[1:]]
        coordinates.append((class_index, points))
    return coordinates

def calculate_iou(gt_coordinates, pred_coordinates):
    """Calculate Intersection over Union (IoU) for each class."""
    iou_results = {}
    for class_index_gt, points_gt in gt_coordinates:
        iou_results[f'IoU of class {class_index_gt}'] = []
        for class_index_pred, points_pred in pred_coordinates:
            if class_index_gt == class_index_pred:
                intersection = min(len(points_gt) // 2, len(points_pred) // 2)
                union = max(len(points_gt) // 2, len(points_pred) // 2)
                iou = intersection / union
                iou_results[f'IoU of class {class_index_gt}'].append(iou)
    return iou_results

# Read coordinates from ground truth file
gt_coordinates = read_coordinates('96.txt')

# Read coordinates from prediction file
pred_coordinates = read_coordinates('utp-0110-075r.txt')

# Calculate IoU for each class
iou_results = calculate_iou(gt_coordinates, pred_coordinates)

output_file = 'iou_results.txt'
with open(output_file, 'w') as f:
    for class_iou, iou_list in iou_results.items():
        for i, iou in enumerate(iou_list):
            f.write(f'{class_iou}_{i + 1}: {iou}\n')
            print(f'{class_iou}_{i + 1}: {iou}')

'''
# Print IoU results
for class_iou, iou_list in iou_results.items():
    for i, iou in enumerate(iou_list):
        print(f'{class_iou}_{i + 1}: {iou}')

'''
