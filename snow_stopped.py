import urllib2
import json
import os
import time
import platform

def get_loc():
    try:
        loc_request = urllib2.Request('http://ipinfo.io')
        # Responds with html if User agent is not curl
        loc_request.add_header('User-Agent','curl/7.30.0')
        opener = urllib2.build_opener()
        response = opener.open(loc_request).read()
        loc_info = json.loads(response)
        if(loc_info is None or
            loc_info["city"] is None or
            loc_info["region"] is None or
            loc_info["country"] is None):
            print "Your location could not be determined!"
            exit(1)
        return loc_info
    except Exception, e:
        raise e

def get_weather(loc_info):
    try:
        args=loc_info["city"]+","+loc_info["region"]+","+loc_info["country"]
        request = urllib2.Request(
                "http://api.openweathermap.org/data/2.5/weather?q=" + \
                urllib2.quote(args)
                )
        response = urllib2.urlopen(request).read()
        return json.loads(response)
    except Exception, e:
        raise e

def main():

    try:
        if os.fork():
            exit()
    except OSError, e:
        raise e

    loc_info = get_loc()
    print "Your are located in "+loc_info["city"]+","+ \
        loc_info["region"]+","+ \
        loc_info["country"]

    while(True):
        weather_info = get_weather(loc_info)
        # weather ids between 600 and 700 indicate its snowing
        if(600 <= weather_info["weather"][0]["id"] < 700):
            time.sleep(300)
        else:
            if( platform.platform().startswith("Darwin") or
                    platform.platform().startswith("Linux") ):
                os.system('echo Snowing stopped! | wall')
            else:
                print "Snowing stopped!"
            exit()

if __name__ == "__main__":
    main()
