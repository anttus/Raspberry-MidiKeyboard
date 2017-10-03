#coding=latin-1

import pygame as pg
import csv
from pygame import midi
from time import sleep

pg.init()
pg.midi.init()
screen = pg.display.set_mode((1,1))

#Variables

instrument = 0
velocity = 80
noteOffset = 0
shiftDown = 0
ctrlDown = 0
endDown = 0
r = 0

#Midi
midiout = pg.midi.Output(3)
midiout.set_instrument(instrument)

#Notes with Janko-layout:

notes = {
	"caps lock":59, "left shift":58, "world 7":57, "tab":58, "1":59, "<":60, "a":61, "z":62, "s":63, "x":64, "d":65, "c":66, "f":67,"v":68, "g":69, "b":70, "h":71,
	"n":72, "j":73, "m":74, "k":75, ",":76, "l":77, ".":78, "world 86":79, "-":80, "world 68":81, "right shift":82, "'":83, 
	"q":60, "2":61, "w":62, "3":63, "e":64, "4":65, "r":66, "5":67, "t":68, "6":69, "y":70, "7":71, 
	"u":72, "8":73, "i":74, "9":75, "o":76, "0":77, "p":78, "+":79, "world 69":80, "backspace":81, "return":84,

	"[0]":84, "enter":85, "[1]":86, "[2]":87, "[3]":88, "[4]":89, "[5]":90, "[6]":91, "[+]":92, "[7]":93, "[8]":94, "[9]":95, "[/]":96, "[*]":97, "[-]":98
	} 


#Checks and waits if key is pressed or released. 
#Also plays the note when a button is pressed and shuts it down if the button is released.

def keypress():
	
	event = pg.event.wait()
	key = pg.key.name(event.key)
	if event.type == pg.KEYDOWN:
		if notes.get(key,0):
			midiout.note_on(notes.get(key) + noteOffset, velocity)
		return "d_" + key
	if event.type == pg.KEYUP:
		if notes.get(key,0):
			midiout.note_off(notes.get(key) + noteOffset, 0)
		return "u_" + key	

midiout.set_instrument(4)
sleep(.2)
midiout.note_on(84,120)
sleep(.8)	
midiout.note_off(84,0)
sleep(.1)
midiout.note_on(91,120)
sleep(.1)
midiout.note_off(91,0)
sleep(.1)
midiout.note_on(94,120)
sleep(.8)
midiout.note_off(94,0)
midiout.set_instrument(instrument)


#Main loop
while 1:
	key = keypress()

#Checks if the left shift button is pressed 

	if key == "d_left shift":
		shiftDown = 1
	elif key == "u_left shift":
		shiftDown = 0

#Select instrument type

	if shiftDown:
		if key == "d_f12":
			instrument = 104
			midiout.set_instrument(instrument)	 
		if key == "d_f11":
			instrument = 88
			midiout.set_instrument(instrument)
		if key == "d_f10":
			instrument = 80
			midiout.set_instrument(instrument)
		if key == "d_f9":
			instrument = 72
			midiout.set_instrument(instrument)
		if key == "d_f8":
			instrument = 64
			midiout.set_instrument(instrument)
		if key == "d_f7":
			instrument = 56
			midiout.set_instrument(instrument)
		if key == "d_f6":
			instrument = 48
			midiout.set_instrument(instrument)
		if key == "d_f5":
			instrument = 40
			midiout.set_instrument(instrument)
		if key == "d_f4":
			instrument = 32
			midiout.set_instrument(instrument)
		if key == "d_f3":
			instrument = 24
			midiout.set_instrument(instrument)
		if key == "d_f2":
			instrument = 16
			midiout.set_instrument(instrument)
		if key == "d_f1":
			instrument = 1
			midiout.set_instrument(instrument)

#Next or previous instrument
	else:
		if key == "d_right":
			instrument += 1 * (instrument != 103)
			midiout.set_instrument(instrument)
		elif key == "d_left":
			instrument -= 1  * (instrument != 0)
			midiout.set_instrument(instrument)

#Jump to the first or the last instrument

		elif key == "d_f3":
			instrument = 0
			midiout.set_instrument(instrument)
		elif key == "d_f4":
			instrument = 104
			midiout.set_instrument(instrument)

#Increase or decrease volume
	
		elif key == "d_up":
			velocity += 8 * (velocity != 120)
		elif key == "d_down":
			velocity -= 8 * (velocity != 0)

#Change octave (2-4)

		elif key == "d_f8":	
			noteOffset += 12 * (noteOffset != 24)
		elif key == "d_f7":
			noteOffset -= 12 * (noteOffset != -24)
		elif key == "d_f6":
			noteOffset = 0
			

#Quit/reboot the program


	if key == "d_r":
		r = 1
	elif key == "u_r":
		r = 0
	if key == "d_left ctrl":
		ctrlDown = 1
	elif key == "u_left ctrl":
		ctrlDown = 0
	if key == "d_end":
		endDown = 1
	elif key == "u_end":
		endDown = 0
	if shiftDown and ctrlDown and endDown:
		os.system("sudo halt -p")
	elif shiftDown and ctrlDown and r:
		os.system("sudo reboot")		

	if (key == "d_escape") and endDown:
		pg.midi.quit()
		pg.display.quit()
		break

	


	
	


