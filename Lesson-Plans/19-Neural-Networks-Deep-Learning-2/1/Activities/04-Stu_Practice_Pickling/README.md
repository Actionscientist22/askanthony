# Practice Pickling

## Introduction

You will use Pillow and the requests library to import 20 images into a list and then store that list as a pickle file. The real dataset has 250 images, but importing all of them would take a significant amount of time. For future activities, you'll be provided a pickle file to load all 250 images.

## Instructions

Use the Jupyter notebook in the `Unsolved` folder to complete the following steps, which are broken into three sections.

### Create the Image URL List

1. Define the base_url.

2. Create an empty list for the URLs.

3. Loop through the DataFrame and build and append the full image URLs.

4. Check the number of URLs.

### Import the Images

1. Create an empty list for images.

2. Loop through **only the first 20** image_urls to open and append each image to the list. It is important to only import the first 20 as importing 250 images could take a significant amount of time.

3. Print a statement to show progress.

4. Use requests.get along with the stream parameter and raw attribute on each image.

5. Append each image to the list.

6. View the first image to confirm a successful import.

### Save the List of Images as a Pickle File

1. Import the drive module from google.colab, along with the pickle module.

2. Use drive.mount to mount your Google Drive.

3. Open a file named 'fungi.pkl' and dump the images list into the file.

4. Reopen the 'fungi.pkl' file and use the pickle.load function to load the images from the pickle file.

5. Display the first image.

## Reference

Hajati, F. 2021. *DeFungi* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/773/defungi [2023, December 5]. ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

&copy; 2024 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
