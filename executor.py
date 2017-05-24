import sys
import zip_folder

print('Zipping folder...', end = "")
zip_folder.zip_folder(sys.argv[1])
print('Done')
