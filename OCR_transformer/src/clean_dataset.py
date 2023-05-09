import os
import shutil

test_folder_path = "../data/not" 

# Path to the test folder

IMG_DIR = "../data/images"

# list all subfolders in the image directory
folder = os.listdir(IMG_DIR)
for file_name in folder:
    if file_name.endswith('.jpg'):  # Check if the file is an image
        csv_file_name = os.path.splitext(file_name)[0] + '.csv'  # Generate the name of the corresponding CSV file
        csv_file_path = os.path.join(IMG_DIR, csv_file_name)  # Get the path to the CSV file
        
        csv_file_name2 = os.path.splitext(file_name)[0] + '.xlsx'  # Generate the name of the corresponding CSV file
        csv_file_path2 = os.path.join(IMG_DIR, csv_file_name)  # Get the path to the CSV file
        
        if not os.path.exists(csv_file_path) and (not os.path.exists(csv_file_path2)) :  # Check if the CSV file exists
            # If the CSV file doesn't exist, move the image file to the test folder
            image_file_path = os.path.join(IMG_DIR, file_name)
            test_image_file_path = os.path.join(test_folder_path, file_name)
            shutil.move(image_file_path, test_image_file_path)
    else:
        img_file_name = os.path.splitext(file_name)[0] + '.jpg'  # Generate the name of the corresponding CSV file
        img_file_path = os.path.join(IMG_DIR, img_file_name)  # Get the path to the CSV file
        if not os.path.exists(img_file_path):  # Check if the CSV file exists
            # If the CSV file doesn't exist, move the image file to the test folder
            print("OOOOO")
            image_file_path = os.path.join(IMG_DIR, file_name)
            test_image_file_path = os.path.join(test_folder_path, file_name)
            shutil.move(image_file_path, test_image_file_path)
