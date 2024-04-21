# Comic Books

In this activity, you will take a large CSV file of comic books, read it into the Jupyter Notebook by using Pandas, clean up the columns, and then write a modified DataFrame to a new CSV file.

This dataset is an expanded version of the Comic Books dataset from the British Library.

## Instructions

* Read in the comic books CSV using Pandas.

* Remove unnecessary columns from the DataFrame so that only the following columns remain:

  * ISBN
  * Title
  * Other titles
  * Name
  * All names
  * Country of publication
  * Place of publication
  * Publisher
  * Date of publication

* Rename the “Name” column to “Author”, rename the “Date of publication” column to “Publication Year”, and then apply title case styling where appropriate in the remaining columns.

* Answer the following questions using `loc` and `iloc`:

  * How many comics were published in the 1960s?

  * Are there more Batman comics or Superman comics?

    * Find the number of Batman comics.

    * Find the number of Superman comics.

    * Write your answer in the summary cell.

## Hint

* The base CSV file uses UTF-8 encoding. Trying to read in the file by using some other kind of encoding could introduce strange characters to the dataset. Check the tail of the dataset with `.tail()` to determine if you correctly imported the CSV file. You should be able to see characters from other languages.

## Reference

British Library. 2014. Comic books CSV. Available: [https://www.bl.uk/collection-metadata/downloads](https://www.bl.uk/collection-metadata/downloads)

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
