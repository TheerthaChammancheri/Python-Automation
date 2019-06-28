import os, datetime
for root, dirs, files in os.walk("."):
    for filename in files:
        print 'Created date : {2}    Filename : {0}    File size : {1}'.format(filename,os.path.getsize(filename),datetime.datetime.fromtimestamp(os.path.getmtime(filename)).isoformat())

