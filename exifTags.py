from PIL import Image
from PIL.ExifTags import TAGS
import re


def getMetaData(imgname, out=None):
    metaData = {}
    imgFile = Image.open(imgname)
    print "Getting meta data..."
    print imgFile
    info = imgFile._getexif()
    print info
    if info:
        print "found meta data!"
        for (tag, value) in info.items():
            tagname = TAGS.get(tag, tag)
            metaData[tagname] = value
    else:
        info = str(imgFile)
        print info
        metaData['Mode'] = re.search('(?<=mode=)[A-Za-z]+', info).group()
        metaData['Size'] = re.search('(?<=size=)[0-9x]+', info).group()
    return metaData
