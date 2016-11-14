from PIL import Image
from PIL.ExifTags import TAGS

def getMetaData(imgname, out=None):
    try:
        metaData = {}

        imgFile = Image.open(imgname)
        print "Getting meta data..."
        if info:
            print "found meta data!"
            for (tag, value) in info.items():
                tagname = TAGS.get(tag, tag)
                metaData[tagname] = value
                if not out:
                    print tagname, value
    except:
        print "Failed"
