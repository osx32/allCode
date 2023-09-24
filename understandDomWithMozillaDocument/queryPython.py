#Python dom example
import xml.dom.minidom as m
doc = m.parse(r'C:\Projects\Py\chap1.xml')
doc.nodeName
p_list = doc.getElementsByTagName('para')