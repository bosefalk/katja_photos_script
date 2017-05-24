# Given a folder name (which must be a sub-folder of /home/bose/photos),
# it creates a zip file called katerina_falk_photos.zip which contains all files
# in that folder

def zip_folder(folder_name):
    import zipfile
    import os
    import glob # list files

    # Change working directory
    os.chdir('/home/bose/photos/' + folder_name)

    # Create zip file in current working directory
    zip_file = zipfile.ZipFile('katerina_falk_photos.zip', 'w')

    # List all files in the folder, then remove the zip file from the list
    all_files = glob.glob('*.*')
    files_to_write = [file for file in all_files if file != 'katerina_falk_photos.zip']

    #Add all files (in current wd) to zip file
    for i in range(0, len(files_to_write)):
        zip_file.write(files_to_write[i])

    zip_file.close()
