# GAiN-a-Friend
Treehacks 2020. A GAN-generated virtual friend that allows older folks to have companionship.


To run the houndify live small talk with voice: 

```
rec -p | sox - -c 1 -r 16000 -t s16 -L - | ./sample_stdin.py <CLIENT ID> <CLIENT KEY>
```

Currently just uses houndify small talk and acapela to generate responses and audio. Under `houndify-3.1.1/example`, run `node server.js` . It'll return an audio bytes string with the response.
