import exifread as exif
import base64
import sys
import os
import glob

lat = []
lon = []
latref = []
lonref = []
time = []
tags = []
encoded_images = []
noexif = []
location = sys.argv[1]
index = 0

#Makes an array of the certain EXIF values of the Photos, specifically date and time and lat and lon for photos with EXIF

for photos in glob.glob('*.jpg'):
    photo = open(photos, 'rb')
    exifdata = exif.process_file(photo, details=False)
    if bool(exifdata) == True:    
        tags.append(exifdata)
    else:
        noexif.append(i)
        continue
    with open(photos, 'rb') as pic:
        encoded = base64.b64encode(pic.read())
    encoded_images.append(encoded)
    date = tags[index]['EXIF DateTimeOriginal'].__dict__
    year = date['printable'][0:4]
    month = date['printable'][5:7]
    day = date['printable'][8:10]
    hour = date['printable'][11:13]
    minute = date['printable'][14:16]
    second = date['printable'][17:19]
    time.append((hour,minute,second,month,day,year))
    lon.append(tags[index]['GPS GPSLongitude'].__dict__)
    lat.append(tags[index]['GPS GPSLatitude'].__dict__)
    latreff = (tags[index]['GPS GPSLatitudeRef'].__dict__)
    lonreff = (tags[index]['GPS GPSLongitudeRef'].__dict__)
    latref.append(latreff['printable'])
    lonref.append(lonreff['printable'])
    index += 1            

def DMStoDeg(item,ref):
    d = float(item['values'][0].num)/float(item['values'][0].den)
    m = float(item['values'][1].num)/float(item['values'][1].den)
    s = float(item['values'][2].num)/float(item['values'][2].den)
    if ref == 'N' or ref == 'E':
        return d + m/60. + s/3600.
    if ref == 'S' or ref == 'W':
        return -(d + m/60. + s/3600.)

#Makes Folder for KML files
if not os.path.exists(r'%s/KMLs'%location):
    os.makedirs(r'%s/KMLs'%location)
    
    
KML = open('%s/KMLs/Photos(1)through(%i).kml'%(location,len(lat)),'w')
KML.write('<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2"> \n<Document>\n')
for j in range(len(lon)):
    KML.write('<Placemark> \n')
    KML.write('<name>%s:%s:%s %s/%s/%s</name> \n' %(time[j][3],time[j][4],time[j][5],time[j][0],time[j][1],time[j][2]))
    KML.write('<description><![CDATA[<img src="data:image/jpg;base64,%s" alt="Encode Attempt" width = 300 height = 240>]]> </description>\n' %(encoded_images[j]))
    KML.write('<Point> \n')
    KML.write('<coordinates>%f,%f,0</coordinates> \n' %(DMStoDeg(lon[j],lonref[j]),DMStoDeg(lat[j],latref[j])))
    KML.write('</Point> \n</Placemark> \n')
KML.write('</Document> \n</kml>')

#Makes txt file to list photos without EXIF data
NoExif = open('%s/KMLs/PhotosWithoutExif.txt'%location,'w')
for k in noexif:
    NoExif.write('Photo (%i) \n'%(k+1))
