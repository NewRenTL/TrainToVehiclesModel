import os

# Path to the folder containing the downloaded images

images_folder = './MotoTaxi'

# Get the list of lines in the folder
files = os.listdir(images_folder)

#I'm going to define a prefix for the new names
prefix = 'MotoTaxi'

# Variable to count the images
counter = 1

for file in files:

    #Let's go to create a new file name
    new_name =f"{prefix}{counter}.jpg"
    currentPath = os.path.join(images_folder,file)
    newPath = os.path.join(images_folder,new_name)

    #Rename the file
    os.rename(currentPath,newPath)

    counter+=1

print("File names changed successufully")