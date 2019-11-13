import os
import lxml.etree as ET


def read_xpaths(pageName,elementNmae):
    path=  os.path.normpath(os.getcwd() + os.sep + os.pardir) + "\\utility\\locators\\locators.xml"
    root = ET.parse(path)

    xpathvalue = ".//{}/element[name/text()='{}']/value/text()".format(pageName,elementNmae)
    print(xpathvalue)
    value = root.xpath(xpathvalue)


    return str(value[0])


# read_xpaths("animationPage","btn0")
