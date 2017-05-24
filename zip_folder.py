# Given a folder name (which must be a sub-folder of /home/bose/photos),
# it creates a zip file called katerina_falk_photos.zip which contains all files
# in that folder

def zip_folder(folder_name):
    import zipfile
    import os
    import glob # list files

    # Construct path to folder to be zipped
    path1 = 'photos/' + folder_name + '/'


    # Create zip file which is ready to write to
    zip_file = zipfile.ZipFile(path1 + 'katerina_falk_photos.zip', 'w')

    # List all files in the folder, then remove the zip file from the list
    all_files = [os.path.basename(x) for x in glob.glob(path1 + '*.*')]
    files_to_write = [file for file in all_files if file != 'katerina_falk_photos.zip']

    #Add all files to zip file, without their path
    for i in range(0, len(files_to_write)):
        zip_file.write(path1 + files_to_write[i], arcname = files_to_write[i])

    zip_file.close()