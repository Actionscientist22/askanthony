Show your current path
```shell
pwd
```

Change directories to the Desktop (location may vary)
```shell
cd ~/Desktop
```

Make a new directory (folder) on the desktop
```shell
mkdir Pets
```

Move into the newly created folder
```shell
cd Pets
```

Make a new directory inside Pets
```shell
mkdir Dogs
```

Make a new directory inside Pets
```shell
mkdir Cats
```

Move into the Cats folder
```shell
cd Cats
```

Create an empty file
```shell
touch name.txt
```

Input contents to a file
```shell
echo "My name is Lucky! Bark!" > name.txt
```

Output contents of a file
```shell
cat name.txt
```

Move back to the root of the Pets folder
```shell
cd ..
```

Copy the name.txt file into the Dogs folder
```shell
mv name.txt Dogs
```

Remove a directory
```shell
rm -r Cats
```

Rename a file
```shell
mv Dogs Lucky
```

List contents of Pets
```shell
ls
```
