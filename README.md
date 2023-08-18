# WasteTracker-RPI
This code in intended to work with https://github.com/alexkosla/WasteTracker.
It is designed to pull data from HCSR-04 sensor mounted on the underside of a bin lid, process it into a distance float, and stick it onto a JSON payload along with the current time. The payload is then sent as a POST request to a web server.

Dependencies:
* https://github.com/alaudet/hcsr04sensor

To use this file, first install the dependencies above (look at the README). 

Next, you'll need to edit the `post_url` variable to correspond to the IP/url of whatever web server you're attempting to post to. By default, the code calculates distance based on the speed of sound at 20C. For relatively short distances (distances in cm) the difference is quite small for various indoor temperatures, so adjusting it may not be necessary for reasonably accurate results. However, if you are determined to do so, change the `temp` variable to the temperature of your choice, and then set `data['distance']` equal to `distance_room_temp`.

To run the file once, simply run it from the command line.

To run the file every thirty minutes on Linux, set up a crontab via the command `crontab -e`. Add in the following lines:

`0 * * * * python3 /path/to/file/reading.py`

`30 * * * * python3 /path/to/file/reading.py`

Save it and your raspberry pi will read the sensor data every 30 minutes and send a POST request to the web server of your choosing.
