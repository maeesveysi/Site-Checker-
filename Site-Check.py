import urllib.request  as urllib

print ('This is Site Connectivity Chekcer')
input_ur1 = input (" Pls Enter your URL :")

def main (url) :
    print ('Checking Connectivity.. ')

    response = urllib.urlopen (url)

    print ('Connected to : ', url , 'Succecsfully')
    print ("The Response code is " , response.getcode ())

main (input_ur1)