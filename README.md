# snow_stopped
Handy command-line script to know when snowing stops!

On Linux and Mac it will send a broadcast to all users, visible on command line

# Instructions
$ git clone https://github.com/akshaychhajed/snow_stopped .

$ python snow_stopped.py

# Example
$ python snow_stopped.py

You are located in [city],[region],[country]

Broadcast Message from user@vm1
	(/dev/tty1) at 18:38 EST ...

Snowing stopped!

$

# How it works

It tries to fetch your location based on your IP

It uses this location to get weather information
