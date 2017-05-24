import sys
from zip_folder import zip_folder
from generate_url import generate_url

print('Zipping folder...', end = "")
zip_folder(sys.argv[1])
print('Done')


print('Generating url...', end = "")
generate_url(sys.argv[1])
print('Done')
