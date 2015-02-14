import urllib2
import json
import os
import time

def get_loc():
    loc_request = urllib2.Request('http://ipinfo.io')
    # Responds with html if User agent is not curl
    loc_request.add_header('User-Agent','curl/7.30.0')
    opener = urllib2.build_opener()
    response = opener.open(loc_request).read()
    loc_info = json.loads(response)
    if(loc_info==None or
        loc_info["city"]==None or
        loc_info["region"]==None or
        loc_info["country"]==None):
        print "Your location could not be determined!"
        exit(1)
    return loc_info

def get_weather(loc_info):
    args='q='+loc_info["city"]+","+loc_info["region"]+","+loc_info["country"]
    request = urllib2.Request("http://api.openweathermap.org/data/2.5/weather?"+args)
    response = urllib2.urlopen(request).read()
    return json.loads(response)


def main():

    loc_info = get_loc()
    print "Your are located in "+loc_info["city"]+","+ \
        loc_info["region"]+","+ \
        loc_info["country"]

    while(True):
        weather_info = get_weather(loc_info)
        if(600 <= weather_info["weather"][0]["id"] < 700):
            time.sleep(300)
        else:
            if( "Darwin" or "Linux" in platform.platform()):
                os.system('echo Snowing stopped! | wall')
            else:
                print "Snowing stopped!"
            exit()

if __name__ == "__main__":
    main()
