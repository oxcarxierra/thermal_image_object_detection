import csv
import os

def convert_csv_to_txt(csv_file_path, output_folder):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)

        data = {}
        for row in csv_reader:
            image_id = row[0]
            image_name = image_name = os.path.splitext(row[1])[0] 
            class_label = 0
            x1, y1, x2, y2 = map(int, row[3:])
            
            if image_id not in data:
                data[image_id] = {'image_name': image_name, 'annotations': []}
            
            data[image_id]['annotations'].append({
                'class': class_label,
                'x1': x1,
                'y1': y1,
                'x2': x2,
                'y2': y2
            })
    
    for image_id, values in data.items():
        output_file_path = f"{output_folder}/{values['image_name']}.txt"
        
        # Create a new text file if it doesn't exist
        if not os.path.exists(output_file_path):
            open(output_file_path, 'w').close()
            
        with open(output_file_path, 'a') as txt_file:
            for annotation in values['annotations']:
                x_center = int((annotation['x1'] + annotation['x2']) / 2)
                y_center = int((annotation['y1'] + annotation['y2']) / 2)
                width = annotation['x2'] - annotation['x1']
                height = annotation['y2'] - annotation['y1']
                txt_file.write(f"0 {x_center} {y_center} {width} {height}\n")

# Replace 'annotation.csv' and 'output_folder' with your actual file paths
convert_csv_to_txt('./train_annotations.csv', './label')