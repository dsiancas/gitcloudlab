#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/alumnos', 'list_users',
    '/alumnos/(.*)', 'get_user',
    '/status', 'status'
)

app = web.application(urls, globals())


class status:
    def GET(self):
        web.header('Content-Type', 'text/plain')
        #resp = app.request("/alumnos")
        return web.ctx.status

class list_users:        
    def GET(self):
	output = 'alumnos:[';
	for child in root:
                print 'child', child.tag, child.attrib
                output += str(child.attrib) + ','
	output += ']';

        return output

class get_user:
    def GET(self, user):
	for child in root:
		if child.attrib['id'] == user:
		    return str(child.attrib)

if __name__ == "__main__":
    app.run()