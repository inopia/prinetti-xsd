from lxml import etree

document = etree.parse("example.xml")
xmlschema_doc = etree.parse("schema.xml")
xmlschema = etree.XMLSchema(xmlschema_doc)

xmlschema.assertValid(document)
