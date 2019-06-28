import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
print root.attrib

for child in root:
    book_cat = root.getchildren()
    for book in book_cat:
        book_children = book.getchildren()
        print child.attrib
        for book_child in book_children:
            print("%s=%s" % (book_child.tag, book_child.text))

