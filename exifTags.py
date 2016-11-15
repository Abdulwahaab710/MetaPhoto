from PIL import Image
from PIL.ExifTags import TAGS


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
            if not out:
                print tagname, value
    return metaData
