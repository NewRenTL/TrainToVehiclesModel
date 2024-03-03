import os
import random
import shutil
import numpy as np

original_folders= ["./Buses","./Combi","./MiniBus","./Moto","./MotoTaxi"]
newFolder = "./MixCars"
if not os.path.exists(newFolder):
    os.makedirs(newFolder)

images_per_folders = 10

for folder in original_folders:

    files = os.listdir(folder)


    #Randomly select 'images_per_folder' files
    #selected_files = random.sample(files,images_per_folders)
    selected_files = np.random.choice(files,images_per_folders,replace=False)

    #Copy the selected files to the new folder
    for file in selected_files:
        original_path = os.path.join(folder,file)
        destination = os.path.join(newFolder,file)

        shutil.copyfile(original_path,destination)
    
print(f"{images_per_folders} images randomly selected from each other folder and copied to the new folder")
