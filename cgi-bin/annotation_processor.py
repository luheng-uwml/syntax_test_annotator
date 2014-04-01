import cgi
import cgitb
import codecs
import json
import os.path.join as join
import socket
import sys

cgitb.enable()

sents = json.loads(cgi.FieldStorage()["data"].value);
filepath = cgi.FieldStorage()["filepath"].value
sys.stderr.write(str(sents) + "\n")

output_file = codecs.open(join("../saved", filepath), 'w')
output_file.write(json.dumps(sents, indent=4))
output_file.write('\n')
output_file.close()

print 'Content-type: application/json\n\n' 
print json.dumps( {"saved" : "success"} )

