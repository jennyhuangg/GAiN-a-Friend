#!/usr/bin/env python3
import houndify
import sys
from gtts import gTTS 
import os
import base64


CLIENT_ID = "Rco-d2ARwyAUSvklEH_ePg=="
CLIENT_KEY = "V6TzSgIOkx0CW4AkBSxgLNrcHMEZ26PSB4uLaG-n8t6PsjZSEzBF-aGfXQv-mWXha0_grVB-TO5MGdKhx9XNFA=="
BUFFER_SIZE = 512

#
# Simplest HoundListener; just print out what we receive.
# You can use these callbacks to interact with your UI.
#
class MyListener(houndify.HoundListener):
  def onPartialTranscript(self, transcript):
    print("Partial transcript: " + transcript)
  def onFinalResponse(self, response):
    # Playing the converted file 
    response_text = response["AllResults"][0]["SpokenResponse"]
    # get response audio bytes string
    response_bytes = response["AllResults"][0]["ResponseAudioBytes"]
    os.system("say {}".format(response_text)) 
    print("Response bytes:" + response_bytes)
    print("Final response: " + str(response))

    # convert bytes string to binary
    decoded = base64.decodebytes(response_bytes.encode("ascii"))

    # writes response to wav file
    with open('myfile.wav', mode='bx') as f:
      f.write(decoded)
      
  
  def onError(self, err):
    print("Error: " + str(err))


client = houndify.StreamingHoundClient(CLIENT_ID, CLIENT_KEY, "test_user")
client.setLocation(37.388309, -121.973968)
client.setHoundRequestInfo("ResponseAudioVoice", "Sharon")
client.setHoundRequestInfo("ResponseAudioShortOrLong", "Short")

## Uncomment the lines below to see an example of using a custom
## grammar for matching.  Use the file 'turnthelightson.wav' to try it.
# clientMatches = [ {
#   "Expression" : '([1/100 ("can"|"could"|"will"|"would")."you"].[1/10 "please"].("turn"|"switch"|(1/100 "flip"))."on".["the"].("light"|"lights").[1/20 "for"."me"].[1/20 "please"])|([1/100 ("can"|"could"|"will"|"would")."you"].[1/10 "please"].[100 ("turn"|"switch"|(1/100 "flip"))].["the"].("light"|"lights")."on".[1/20 "for"."me"].[1/20 "please"])|((("i".("want"|"like"))|((("i".["would"])|("i\'d")).("like"|"want"))).["the"].("light"|"lights").["turned"|"switched"|("to"."go")|(1/100"flipped")]."on".[1/20"please"])"',
#   "Result" : { "Intent" : "TURN_LIGHT_ON" },
#   "SpokenResponse" : "Ok, I\'m turning the lights on.",
#   "SpokenResponseLong" : "Ok, I\'m turning the lights on.",
#   "WrittenResponse" : "Ok, I\'m turning the lights on.",
#   "WrittenResponseLong" : "Ok, I\'m turning the lights on."
# } ]
# client.setHoundRequestInfo('ClientMatches', clientMatches)

client.start(MyListener())

while True:
  samples = sys.stdin.buffer.read(BUFFER_SIZE)
  if len(samples) == 0: break
  if client.fill(samples): break

client.finish()