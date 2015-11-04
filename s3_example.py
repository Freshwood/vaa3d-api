import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key

AWS_ACCESS_KEY = os.getenv('VAA3D_AWS_ACCESS_KEY', 'password')
AWS_SECRET_KEY = os.getenv('VAA3D_AWS_SECRET_KEY', 'password')

# Connect to bucket
conn = S3Connection(AWS_ACCESS_KEY, AWS_SECRET_KEY)
bucket = conn.get_bucket('vaa3d-test-data', validate=False)

# List files in bucket
files = bucket.list()
for f in files:
	print f

# Check if key exists
possible_key = bucket.get_key('mynonexistingkey')
print possible_key == None

# Store and retrieve string
k = Key(bucket)
k.key = 'foobar'
k.set_contents_from_string('This is a test of S3')
contents = k.get_contents_as_string()
print contents

# Store and retrieve file
testfile = open('inputfile.txt','w') # Trying to create a new file or open one
testfile.write('hello, world!')
testfile.close()
k = Key(bucket)
k.key = 'mytestfile'
k.set_contents_from_filename('inputfile.txt')
contents = k.get_contents_to_filename('outputfile.txt')

# Clean up
os.remove('inputfile.txt')
os.remove('outputfile.txt')

