# GAiN-a-Friend
Treehacks 2020. A GAN-generated virtual friend that allows older folks to have companionship.


## Python (Commandline Program)
To run the houndify live small talk with voice and wav file response, go to houndify_python3_sdk_1.2.5 and then run: 

```
rec -p | sox - -c 1 -r 16000 -t s16 -L - | ./sample_stdin.py "Rco-d2ARwyAUSvklEH_ePg==" "V6TzSgIOkx0CW4AkBSxgLNrcHMEZ26PSB4uLaG-n8t6PsjZSEzBF-aGfXQv-mWXha0_grVB-TO5MGdKhx9XNFA==" 
```
The logic is under `sample_stdin.py` in the method `onFinalResponse`.

https://docs.houndify.com/sdks/docs/python

## JS (Interactive Web App)
Currently just uses houndify small talk and acapela to generate responses and audio. Under `houndify-3.1.1/example`, run `node server.js` . It'll start up a local server with a UI to ask questios, and it logs an audio bytes string with the response.


https://docs.houndify.com/sdks/docs/javascript
