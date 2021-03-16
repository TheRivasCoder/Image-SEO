import os

new_filename = 'Example title for images'
count = 0
image_file = './images'
for filename in os.listdir(image_file):
    if '.jpg' not in filename:
        continue
    suffix = filename.split('.')[1]
    os.rename(image_file + "/" + filename, new_filename + ' ' + str(count) + '.' + suffix)
    count +=1
