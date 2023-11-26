# machine learning client 
This is the machine learning client
portion of our app, that uses the deepface
library to process images from the webcam 
of a user.
# Run instructions
It runs as a flask web app with ```flask --app main run```
and is meant to run on port 3000, along with the web-app portion
which is to run on port 3001.

# Tests
It comes with unit tests in the tests folder, which can be run with 
```pytest maintests.py```