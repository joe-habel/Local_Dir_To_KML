# Local_Dir_To_KML
A short script to strip EXIF data from jpgs with it and create a KML of said jpgs

All Photos should be in a single directory and renamed in bulk to Photo, i.e. Photo (1), Photo (2), Photo (3)

The command line will take in the directory for the photos and the total number of photos in the directory i.e.
  
  `python PhotoToKML.py User/Photos 15`
  
  where the directory of the pictures would be User/Photos, and there would be 15 jpgs in total

The script will then output in a new folder in the directory a KML and a txt file containing a list of all the photos without exif data.
