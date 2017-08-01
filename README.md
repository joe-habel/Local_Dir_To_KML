# Local_Dir_To_KML
A short script to strip EXIF data from jpgs with it and create a KML of said jpgs


The command line will take in the directory for the photos i.e.
  
  `python PhotoToKML.py User/Photos`
  
  where the directory of the pictures would be User/Photos.

The script will then output in a subdirectory a KML and a txt file containing a list of all the photos without exif data.

Note that exifread is not a standard python package and must be installed
