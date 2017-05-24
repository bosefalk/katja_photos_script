
def generate_url(folder_name):

    url = '/brains/' + folder_name

    zip_download = 'photos/' + folder_name + '/katerina_falk_photos.zip'

    # Check if this url already exists in web server
    if url in open('flask_main.py').read():
        url_exists = True

    else:
        url_exists = False

    # If not, add it at the end
    if url_exists == False:
        with open('flask_main.py', "a+") as f:
            f.write('\n' + '\n')
            f.write("@app.route('" + url + "', methods=['GET', 'POST'])" + '\n')
            f.write('def ' + folder_name + '():' + '\n')
            f.write("\treturn send_file('" + zip_download + "', as_attachment=True)")

