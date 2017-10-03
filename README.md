# Raspberry-MidiKeyboard
Raspberry Pi Midi-keyboard project I made as a degree work at school.

The needed packages for the project are Python 2.7 and Pygame for it, ALSA (Advanced Linux Sound Architecture) and Timidity. 
You can install them straight through apt-get or by downloading them with wget.  
Timidity needs to be set to use ALSA to produce the sounds and this can be done by going to 
/etc/init.d/timidity (It’s there so it launches when the device boots) and adding parameters 
”-iAD -B2,10 -Os”
The parameters “iAD” and “-Os” make Timidity use ALSA as the sound driver and “-B2,10” sets the buffer size to 1024. 
The bigger the buffer size is, the more there’s latency (if it’s too small the sound distorts). 
You can change the sound “fonts” by changing the .sf2-file path in Timidity’s config file at /etc/timidity/timidity.cfg.
