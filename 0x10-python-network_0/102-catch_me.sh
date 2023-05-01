#!/bin/bash
# Makes a request and the response is You got me!
curl -s -X PUT -H "Origin: HolbertonSchool" -L 0.0.0.0:5000/catch_me --data ""
