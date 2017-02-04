import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
url_str = 'http://205.221.97.102/Iowa.Sims.AllSites.C2C/IADOT_SIMS_AllSites_C2C.asmx/OP_ShareTrafficDetectorData?MSG_TrafficDetectorDataRequest=string%20HTTP/1.1'
request = urllib2.Request(url_str, headers={"Accept" : "text/xml"})
contents = urllib2.urlopen(request).read()
f = open('stream.xml','w')
f.write(contents)
f.close()


tree = ET.parse('stream.xml')
root = tree.getroot()

#Get the 'Detector-id' and its 'status' from XML
for i in range(1,100,1):
    z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
    print z.getchildren()[0].text, '|', z.getchildren()[1].text

for i in range(1,100,1):
    z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
    streamdata= [z.getchildren()[0].text, '|', z.getchildren()[1].text]
print streamdata
import csv
streamdata= "<C:\Users\rhamz\Desktop>"
with open(streamdata, "w") as output:
        writer=csv.writer(output, lineterminator='\n')
        writer.writerows(streamdata)
