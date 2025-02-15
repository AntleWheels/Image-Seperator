import os
import shutil
source_folder = "path/to/your/images"

# Define destination folders
anemic_folder = "path/to/your/images/Anemic"
non_anemic_folder = "path/to/your/images/Non_Anemic"

# Create destination folders if they don't exist
os.makedirs(anemic_folder, exist_ok=True)
os.makedirs(non_anemic_folder, exist_ok=True)

# Iterate through files and move them based on the name
for filename in os.listdir(source_folder):
    if "Anmeic" in filename:  
        shutil.move(os.path.join(source_folder, filename), os.path.join(anemic_folder, filename))
    elif "Non-Anrmic" in filename:  
        shutil.move(os.path.join(source_folder, filename), os.path.join(non_anemic_folder, filename))

print("Separation complete!")
