## Find Similar Images

The script find_similar_images() is used to find similar images in a specified directory and its subdirectories. The user is prompted to enter the path of the image they wish to find similar images of, and the directory path in which to search for similar images.

The script first checks if the provided file and directory path exists or not, if it does not exist it will display the appropriate message and exit the function.

The script then uses the Python Imaging Library (PIL) to open the input image and calculate its hash using the hash function. It then recursively searches the specified directory and its subdirectories for images, and compares their hashes to the input image's hash.

The script also uses the progressbar library to show the search progress as a percentage. It updates the progress bar as it searches through the files and directories.

If a similar image is found, the script will add the full path of the match to a list, and print all the matches at the end of the search. If no similar image is found, the script will print "No match found".

The script also checks if the provided file is an image or not, if it's not an image it will display "The provided file is not an image."

In the end, the script will print "Similar image search finished" along with total matches found to indicate that the search has completed. At the end of the script, it will wait for user input to exit the script.

### Installation and Usage

The script requires Python 3.6 or higher to run. It also requires the PIL and progressbar libraries to be installed. To install the libraries, run the following command:

    pip install -r requirements.txt

To run the script, run the following command:
    
    python find_similar_images.py

### License

MIT License

Author: [Hasan Masud](https://github.com/iHasanMasud)

