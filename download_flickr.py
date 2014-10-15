
#!/usr/bin/python           # This is server.py file

import flickr
import urllib, urlparse
import os
import sys
import socket               # Import socket module

def fetch( theme ):
   #if len(sys.argv)>1:
    
#else:
 #   print 'no tag specified'

    # downloading image data
    f = flickr.photos_search(tags=theme)
    urllist = [] #store a list of what was downloaded

    # downloading images
    for k in f:
        url = k.getURL(size='Medium', urlType='source')
        urllist.append(url) 
        image = urllib.URLopener()
        image.retrieve(url, os.path.basename(urlparse.urlparse(url).path)) 
        print 'downloading:', url

    return 

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   data=''
   data = c.recv(1024).decode()
   fetch(data)

   c.send('Thank you for connecting')
   c.close()                # Close the connection







