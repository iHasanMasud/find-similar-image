import os
from PIL import Image
import progressbar


def find_similar_images():
    image = input("Enter the image full path.\nExample C:\\Users\\userName\\Desktop\\image.jpg\n:")

    # check if the file exists
    if not os.path.isfile(image):
        print("The provided file does not exist.")
        return

    directory = input("Enter the folder path.\nExample C:\\Users\\userName\\Desktop\n: ")

    # check if the directory exists
    if not os.path.isdir(directory):
        print("The provided directory does not exist.")
        return

    # Create an empty list to store the matches
    matches = []

    try:
        with Image.open(image) as img:
            # Get the image hash
            img_hash = hash(img.tobytes())
            found = False
            current_file = 0
            total_files = sum([len(files) for r, d, files in os.walk(directory)])
            # bar = progressbar.ProgressBar(maxval=total_files, widgets=[progressbar.AnimatedMarker()])
            bar = progressbar.ProgressBar(maxval=total_files,
                                          widgets=[progressbar.Percentage(), ' ', 'Searching...', ' ',
                                                   progressbar.Bar(), ' ', progressbar.ETA()])
            bar.start()
            for subdir, dirs, files in os.walk(directory):
                for filename in files:
                    current_file += 1
                    bar.update(current_file)
                    # Open the image
                    try:
                        with Image.open(os.path.join(subdir, filename)) as img_to_compare:
                            # Get the image hash
                            img_hash_to_compare = hash(img_to_compare.tobytes())
                            if img_hash == img_hash_to_compare:
                                found = True
                                # if the image is found, add the path to the list
                                matches.append(os.path.join(subdir, filename))
                    except:
                        pass
            bar.finish()
            if not found:
                print("No match found")
            else:
                print("\n")
                for match in matches:
                    print(match)
    except:
        print("The provided file is not an image.")
    print("\nSimilar image search finished.\nTotal matches found: " + str(len(matches)))


find_similar_images()

input('Press ENTER to exit')
