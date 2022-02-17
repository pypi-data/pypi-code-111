# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:59:46 2021

@author: olehe
"""
import mido
import os
import time
import numpy as np
import pandas as pd
import scipy.io.wavfile
import pkg_resources
from math import log, e



#%% Functions

def generate_midi(inputArray, tempo=120, loops=1, saveName='MIDIoutput'):
	"""
	Generate MIDI file from a pattern.
	Specify tempo in BPM, loops as positive integers, and a savename for the
	resulting MIDI file
	

	Parameters
	----------
	inputArray : A rhythm pattern
	tempo : Integer denoting tempo in BPM. Default is 120.
	loops : Number of times to repeat the pattern. Default is 1.
	saveName : Name of the resulting MIDI-file

	Returns
	-------
	None.

	"""
	if saveName[0][-4:] != '.mid':
		saveName = saveName + '.mid'
	
	
	
	output = mido.MidiFile(type=1)
	# default is 480 ticks per beat.
	tickResolution = 480
	eventResolution = int(tickResolution / 4)
	tempoTicks = mido.bpm2tempo(tempo)
	
	
	# then write out from the input array
	# GM drums on channel 10 (9 0-indexed), keys 42 hihat 40 snare 36 kick
	# go for 40, 50 and 60 now
	instrKeys = [42, 40, 36]
	
	# so, its 480 ticks per beat (quarter note)
	
	# Just a track to set the tempo
	track = mido.MidiTrack()
	track.append(mido.MetaMessage('set_tempo', tempo=tempoTicks))
	track.append(mido.MetaMessage('end_of_track', time=(32 * eventResolution * loops)))
	
	output.tracks.append(track)
	
	# write one track per instrument
	
	
	count=0
	
	# hold-time for events
	# not implemented yet
	holdTime = int(tempoTicks/32)
	
	# generate tracks
	for key in instrKeys:
		track = mido.MidiTrack()
		
		thisInstr = inputArray[count,]
		count += 1
		previousEventTime = 0
		loopCount = 0
		for loop in range(0, loops):
			for n in range(0, 32):
				thisEventTime = n*eventResolution + (loopCount * eventResolution * 32)
				if thisInstr[n] == 1:
					# insert an event
					deltaTime = thisEventTime - previousEventTime
					track.append(mido.Message('note_on', note=key, velocity=100, channel=9, time=deltaTime))
					track.append(mido.Message('note_off', note=key, velocity=0, channel=9, time=0))
					
					
					previousEventTime = thisEventTime
				#else:
					#lastEventCount += tickResolution
			loopCount += 1
			#track.append(mido.MetaMessage('end_of_track', time=thisEventTime + tickResolution))
		output.tracks.append(track)		
			
	
	output.save(saveName)
	
	
	return


def generate_wav(pattern, tempo=120, loops=1, saveName='audiofile.wav', fs=44100, 
				 dynamics=False, customSound=None):
	"""
	Generate a .wav file from a pattern.
	Specify a tempo (in BPM), loops, name of the file, sampling rate,
	and decide if you want "dynamics". Dynamics adds offsets to the amplitude
	of the onsets, thus generating more naturally sounding rhythm pattern. 

	Parameters
	----------
	pattern : A rhythm pattern.
	tempo : Tempo in BPM, default is 120.
	loops : Number of times to repeat the pattern. 
	saveName : Name of the output file.
	fs : Integer, optional
		Samplerate. The default is 44100.
	dynamics : Boolean, optional
		Setting this to true adds dynamics to the audio file. The default is False.

	Returns
	-------
	saveName : Path and name of saved audio file.

	"""
	
	# input check
	assert pattern.shape[0] == 3, 'Wrong shape of pattern, should be 3xn!'
	
	#this experimentally just adds some dynamics
	if dynamics:
		dynamicsHihat = np.tile([0.7, 0.5, 1, 0.5], 8)
		dynamicsSnare = np.tile([0.8, 0.7, 0.8, 0.5, 1, 0.5, 0.8, 0.5], 4)
		dynamicsKick = np.tile([1, 0.5, 0.7, 0.5, 0.8, 0.5, 0.7, 0.5], 4)
	else:
		dynamicsHihat = np.ones(32)
		dynamicsSnare = np.ones(32)
		dynamicsKick = np.ones(32)
	
	if saveName[-4:] != '.wav':
		saveName = saveName + '.wav'
		
	
	# read samples
	if customSound:
		if customSound == 'amen':
			hihatLoc = pkg_resources.resource_stream(__name__, 'samples/amenRideLong.wav')
			kickLoc = pkg_resources.resource_stream(__name__, 'samples/amenKickLong.wav')
			snareLoc = pkg_resources.resource_stream(__name__, 'samples/amenSnareLong.wav')
		elif customSound == '909':
			hihatLoc = pkg_resources.resource_stream(__name__, 'samples/909hihatStereo.wav')
			kickLoc = pkg_resources.resource_stream(__name__, 'samples/909kickStereo.wav')
			snareLoc = pkg_resources.resource_stream(__name__, 'samples/909snareStereo.wav')
	else:
		hihatLoc = pkg_resources.resource_stream(__name__, 'samples/hihat.wav')
		kickLoc = pkg_resources.resource_stream(__name__, 'samples/kick.wav')
		snareLoc = pkg_resources.resource_stream(__name__, 'samples/snare.wav')
	
	
	rate, hihatSample = scipy.io.wavfile.read(hihatLoc)
	rate, kickSample = scipy.io.wavfile.read(kickLoc)
	rate, snareSample = scipy.io.wavfile.read(snareLoc)
	
	# just pushing down the amplitude a bit
	if not customSound:
		hihatSample = hihatSample * 0.25
		kickSample = kickSample * 0.25
		snareSample = snareSample * 0.25
	
	
	
	maxLengthSample = max([len(hihatSample), len(snareSample), len(kickSample)])
	
	
	if rate != fs:
		print('Error: Sample rate mismatch between samples and specified sample rate')
		return
	
	# create three np arrays for each instrument, fill them, then merge them
	quarter = 60/tempo
	bar = 4 * quarter
	length = 2 * bar * fs

	# figure out a way to set dtype as same as the wav-files
	hihats = np.zeros((int(length + maxLengthSample),2), dtype='int16')
	snare = np.zeros((int(length + maxLengthSample),2), dtype='int16')
	kick = np.zeros((int(length + maxLengthSample),2), dtype='int16')
	
	# three separate loops
	hihatEvents = pattern[0]
	snareEvents = pattern[1]
	kickEvents = pattern[2]
	
	# for fast tempi, need to consider that the length won't be enough.
	
	#hihats
	
	for n in range(0, len(hihatEvents)):
		if hihatEvents[n] == 1:
			thisPosition = int(round((length/32) * n))
			hihats[thisPosition:thisPosition+len(hihatSample),] = hihats[thisPosition:thisPosition+len(hihatSample),] + (hihatSample * dynamicsHihat[n])

	
	#snare
	for n in range(0, len(snareEvents)):
		if snareEvents[n] == 1:
			thisPosition = int(round((length/32) * n))
			snare[thisPosition:thisPosition+len(snareSample),] = snare[thisPosition:thisPosition+len(snareSample),] + (snareSample * dynamicsSnare[n])

	#kick
	for n in range(0, len(kickEvents)):
		if kickEvents[n] == 1:
			thisPosition = int(round((length/32) * n))
			kick[thisPosition:thisPosition+len(kickSample),] = kick[thisPosition:thisPosition+len(kickSample),] + (kickSample * dynamicsKick[n])		
	
	# mix together
	
	jointSample = (hihats * 0.1) + (snare * 0.3) + (kick * 0.3)
	# ensure length
	#jointSample = jointSample[0:int(round(length)),].astype('int16')
	
	# add loops
	
	looped = np.zeros((int(((length) * loops + (2 * length))), 2), dtype='int16')
	#if loops > 1:
	for n in range(0, loops):
		thisPosition = n*int(length)
		looped[thisPosition:thisPosition+len(jointSample)] = looped[thisPosition:thisPosition+len(jointSample)] + jointSample
	# now trim it
	looped = looped[0:(int(round(length*loops))+maxLengthSample)]
		
	#else:
	#	looped = jointSample[0:(int(round(length*loops))+maxLengthSample)]
	
	normalized = np.array((looped / np.max(np.abs(looped.flatten()))) * 32767, dtype='int16')
	
	# write wav
	scipy.io.wavfile.write(saveName, fs, normalized)
	
	return saveName



#%%

def processPattern(pattern, savename='default', tempo=120, loops=1):
	"""
	This function processes a rhythm pattern, creating a MIDI and audio file.
	The files are suffixed with their syncopation level.

	Parameters
	----------
	pattern : Numpy array.
		A rhythm pattern..
	savename : String, optional
		Name of the output files. The default is 'default'.
	tempo : Integer, optional
		Tempo in BPM. The default is 120.
	loops : Integer, optional
		Number of times to repeat the pattern. The default is 1.

	Returns
	-------
	None.

	"""

	# input check
	assert pattern.shape[0] == 3, 'Wrong shape of pattern, should be 3xn!'
	savename.replace(' ', '')
	
	
	SI = calculate(pattern)
	hSI = SI[0]
	wSI = SI[1]
	hSIstring = str(round(hSI, 3))
	wSIstring = str(round(wSI, 3))
	#replace comma with something?
	hSIstring = hSIstring.replace('.', '_')
	hSIformatted = '-hSI-' +hSIstring
	
	wSIstring = wSIstring.replace('.', '_')
	wSIformatted = '-wSI-' +wSIstring

	if not os.path.isdir('stimsWAV'):
		os.mkdir('stimsWAV')
	if not os.path.isdir('stimsMidi'):
		os.mkdir('stimsMidi')

	midiName = 'stimsMidi/' + savename + hSIformatted + wSIformatted
	waveName = 'stimsWAV/' + savename + hSIformatted + wSIformatted
	

	generate_midi(pattern, tempo, loops, midiName)
	generate_wav(pattern, tempo, loops, waveName)

	
	return

#%% Pattern generation


def generateRandomPattern(minEvents=10, maxEvents=20, avoidMultiples=False, maxMultiple=3):
	"""
	This function generates a random rhythm pattern.
	It draws from a power distribution, and returns a pattern with selectable
	minimum and maximum events.

	Parameters
	----------
	minEvents : Integer, optional
		Minimum number of events in the rhythm. The default is 10.
	maxEvents : TYPE, optional
		Maximum number of events in the rhythm. The default is 20.

	Returns
	-------
	pattern : Numpy array
		A rhythm pattern.

	"""
	# just a simple random pattern with some contraints
	
	#maxEvents = 20
	#minEvents = 10
	# collapse over both instruments? Total between 12 and 18?
	
	# set the hi-hat first
	hihat = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
	        1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

	# now generating them both together
	generate = True
	while generate:
		#snare = np.random.randint(0, 1+1, 32)
		snare = np.round(1-np.random.power(1,32)).astype(int)
		kick = np.round(1-np.random.power(1,32)).astype(int)
		both = np.array([snare, kick]).flatten()
		if sum(both) >= minEvents and sum(both) <= maxEvents:
			generate = False
		# adding now a section that will check for too many hits in a row
		if avoidMultiples:
			snareDiff = np.diff(snare)
			
			countCaseSnare = 0
			for n in snareDiff:
				if n == 0:
					countCaseSnare += 1
				else:
					countCaseSnare = 0
				if n >= maxMultiple:
					generate = True
					break
			
			kickDiff = np.diff(kick)
			countCaseKick = 0
			for n in kickDiff:
				if n == 0:
					countCaseKick += 1
				else:
					countCaseKick = 0
				if n >= maxMultiple:
					generate = True
					break
			
	
	pattern = np.array([hihat, snare, kick])

	
	return pattern


def generateConstrainedPattern(minSnare=10, 
							   maxSnare=20,
							   minKick=4,
							   maxKick=20, 
							   avoidMultiples=False, 
							   maxMultiple=3):
	"""
	This function generates a constrainted rhythm pattern.
	TODO

	Parameters
	----------
	minEvents : Integer, optional
		Minimum number of events in the rhythm. The default is 10.
	maxEvents : TYPE, optional
		Maximum number of events in the rhythm. The default is 20.

	Returns
	-------
	pattern : Numpy array
		A rhythm pattern.

	"""
	# just a simple random pattern with some contraints
	# generate them separately
	
	# set the hi-hat first
	hihat = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
	        1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

	# now generating 
	
	# define a bit of probabilities or something
	probArrayKick = np.tile([0.8, 0.2, 0.4, 0.2, 0.6, 0.2, 0.4, 0.2], 4)
	probArraySnare = np.tile([0.3, 0.4, 0.6, 0.4, 0.8, 0.4, 0.5, 0.4], 4)

	
	genSnare = True
	genKick = True
	
	
	while genSnare:
		snare = np.array([])
		for n in range(0, 32):
			snare = np.insert(snare, n, np.random.binomial(1, probArraySnare[n]))	
		genSnare = False
		snare = snare.astype(int)
		if sum(snare) < minSnare or sum(snare) > maxSnare:
			genSnare = True
			continue
		# adding now a section that will check for too many hits in a row
		if avoidMultiples:
			snareDiff = np.diff(snare)		
			countCaseSnare = 0
			for n in snareDiff:
				if n == 0:
					countCaseSnare += 1
				else:
					countCaseSnare = 0
				if n >= maxMultiple:
					genSnare = True
					break

		


	
	while genKick:
		kick = np.array([])
		for n in range(0, 32):	
			kick = np.insert(kick, n, np.random.binomial(1, probArrayKick[n]))
		genKick = False
		kick[0] = 1	
		kick = kick.astype(int)
		if sum(kick) < minKick or sum(kick) > maxKick:
			genKick = True
			continue
		# adding now a section that will check for too many hits in a row
		if avoidMultiples:
			kickDiff = np.diff(kick)
			countCaseKick = 0
			for n in kickDiff:
				if n == 0:
					countCaseKick += 1
				else:
					countCaseKick = 0
				if n >= maxMultiple:
					genKick = True
					break	
		
				
	
	pattern = np.array([hihat, snare, kick])

	
	return pattern






def searchPattern(SImeasure='W', target=30, timeout=60, minEvents=10, maxEvents=30, verbose=True):
	"""
	This function searches for a pattern with a given syncopation index (SI) value.

	Parameters
	----------
	SImeasure : String, optional
		Choose which syncopation index calculation is used. 
		The default is 'W' for Witek's syncopation index. The other option is
		H for Hoels's syncopation index.
	target : Float, optional
		This is the target SI. The default is 30.
	timeout : Integer, optional
		A maximum amount of time to search for, in seconds. The default is 60.
	minEvents : Integer, optional
		Minimum number of events in the rhythm. The default is 10.
	maxEvents : Integer, optional
		Maximum number of events in the rhythm. The default is 30.
	verbose : Boolean, optional
		If verbose the function will report if it fails. The default is True.

	Returns
	-------
	thisPattern : Numpy array
		A rhythm pattern.
	success : Boolean
		A boolean describing if a rhythm to fit the target was found.

	"""
	# select either 'H' for Hoesl's or 'W' for Witek's as a measure.
	if SImeasure == 'H':
		select = 0
	elif SImeasure == 'W':
		select = 1
	else:
		print('Incorrect input for SI measure')
		return
	
	target = float(target)

	generate = True
	timeStart = time.time()
	
	success = False
	count = 0
	if verbose:
		print('Searching for a maximum of ' + str(timeout) + ' seconds')
	while generate:
		count += 1
		thisPattern = generateRandomPattern(minEvents, maxEvents)
		SIs = calculate(thisPattern)
		thisSI = SIs[select]
		
		if thisSI >= target*0.9 and thisSI <= target*1.1:
			generate = False
			success = True
			if verbose:
				print('Pattern found.')
		timeNow = time.time()
		if (timeNow-timeStart) > timeout:
			generate=False
			thisPattern = None
			if verbose:
				print('Failed, tested ' + str(count) + ' patterns.')
			
			
	return thisPattern, success
		
#%% helpful functions

def savePattern(pattern, saveName='pattern', verbose=True):
	"""
	This function saves the pattern as a csv, along with the weights used in
	the syncopation calculation

	Parameters
	----------
	pattern : Numpy array
		The rhythm pattern to save.
	saveName : String, optional
		Name of the output file. The default is 'pattern'.
	verbose : Boolean, optional
		If true, prints that it has saved the pattern. The default is True.

	Returns
	-------
	None.

	"""
	# input check
	assert pattern.shape[0] == 3, 'Wrong shape of pattern, should be 3xn!'
	
	
	output = syncopationIndexHoesl(pattern, wrap = False)
	hWeights = output[1]
	output = syncopationIndexWitek(pattern, wrap = False)
	wWeights = output[1]
	
	data = {'hihat':pattern[0,],
	  'snare':pattern[1,],
	  'kick':pattern[2,],
	  'hWeights':hWeights,
	  'wWeights':wWeights}
	pattern_df = pd.DataFrame(data).T

	print(saveName)
	if saveName[-4:] != '.csv':
		saveName = saveName + '.csv'
	
	pattern_df.to_csv(saveName)
	if verbose:
		print('Pattern saved')
	return

def loadPattern(filename, asArray=True):
	"""
	This function loads a pattern from a csv file. Note that this is likely to
	fail in many cases, and should only really be used for patterns saved
	by the savePattern functions.

	Parameters
	----------
	filename : String
		Path of the file to load.
	asArray : Boolean, optional
		Choose whether to load as a numpy array. The default is True.

	Returns
	-------
	Numpy array
		Rhythm pattern.

	"""
	# this is probably going to fail in many cases, since I don't care to write checks for weird formatting issues
	# defaults to array, otherwise specify false and will return as dataframe
	try:
		pattern = pd.read_csv(filename, index_col=0)	
	except:
		print('Loading file failed')
		return
	
	if asArray:
		pattern_np = pattern.to_numpy()
		pattern_np = pattern_np[0:3,].astype('int32')
		return pattern_np
	
	
	return pattern

		
#%% Syncopation measures
def syncopationIndexHoesl(pattern, wrap = True, weights = None):
	"""
	This function calculates Hoesl's syncopation index from
	X.
	Wrap decides whether the first event is added to the end.
	Weights are hard coded, but can be supplied.

	Parameters
	----------
	patternA : Numpy array
		The first rhythm pattern, usually the snare.
	patternB : Numpy array
		The second rhythm pattern, usually the kick.
	wrap : Boolean, optional
		Whether to add the first event to the end. The default is True.
	weights : Numpy array, optional
		Custom weights for the SI calculation. The default is None.

	Returns
	-------
	Float
		Returns the syncopation index value.

	"""
	# input check
	assert pattern.shape[0] == 3, 'Wrong shape of pattern, should be 3xn!'
	
	patternA = pattern[1,] # snare
	patternB = pattern[2,] # kick
	
	
	
	
	# default to wrapping, meaning that the first event in the patterns
	
	if weights is not None:
		w = weights
		#should probably check that length is same
	else:
		w = (0, -3,-2, -3, -1, -3, -2, -3, -1, -3, -2, -3, -1,-3, -2, -3, 0, -3,-2, -3, -1, -3, -2, -3, -1, -3, -2, -3, -1,-3, -2, -3)
	 
	
	if wrap:
		patternA = np.append(patternA, patternA[0])
		patternB = np.append(patternB, patternB[0])
		w = np.append(w, w[0])
	
	if len(patternA) != len(w):
		print('Error: Length of pattern needs to be same length as the weights.')
		return
	
	def delta(m,n):
		if(m > n):
			return 1
		else:
			return 0
		
	def phi(a,w,i):
		j = i - 1
		if i >= 3 and a[i-1]== 0.0:
			j = i - 1 - delta(a[i-2],a[i-1])*delta(w[i-2],w[i-1])
		if i >= 5 and a[i-1]==0.0 and a[i-2]==0.0:
			j = i - 1 - 3*(delta(a[i-4],a[i-3])*delta(w[i-4],w[i-3])*delta(a[i-4],a[i-2])*delta(w[i-4],w[i-2])*delta(a[i-4],a[i-1])*delta(w[i-4],w[i-1]))
		return j
	
	def syncopation(s,b,w,B):
		# is B supposed to be length of pattern, with or without loop?
		w_out = np.zeros(len(w), dtype = float)
		c = 2.8 # optimized parameter that 'governs the relationship between metric weight'
		d = 1.6 # two-stream syncopation factor, equals d when both instruments are silent on i, otherwise 0
		h = 1.32 # scaling factor, chosen such that the slope of the linear link function (with perceived syncopation)
		n = len(w)
		S = 0
		for i in range(1,n): 
			j = phi(s,w,i)
			k = phi(b,w,i)
			w_out[i] = (delta(w[i],w[k])*delta(b[k],b[i])*(c**(w[i])-c**(w[k]))
             +delta(w[i],w[j])*delta(s[j],s[i])*(c**(w[i])-c**(w[j])))*d**(delta(1,s[i]+b[i]))
		
		S = sum(w_out)
		return S/B*h, w_out
	
	
	
	output = syncopation(patternA,patternB,w,32)
	

	return output


def syncopationIndexWitek(pattern, wrap = True, weights = None):
	"""
	This calculates Witek's syncopation index from X.

	Parameters
	----------
	patternA : Numpy array
		The first rhythm pattern, usually the snare.
	patternB : Numpy array
		The second rhythm pattern, usually the kick.
	wrap : Boolean, optional
		Whether to add the first event to the end. The default is True.
	weights : Numpy array, optional
		Custom weights for the SI calculation. The default is None.

	Returns
	-------
	Float
		Returns the syncopation index.

	"""
	# input check
	assert pattern.shape[0] == 3, 'Wrong shape of pattern, should be 3xn!'
	
	patternA = pattern[1,] # snare
	patternB = pattern[2,] # kick

	
	if weights is not None:
		w = weights
		#should probably check that length is same
	else:
		w = (0, -3,-2, -3, -1, -3, -2, -3, -1, -3, -2, -3, -1,-3, -2, -3, 0, -3,-2, -3, -1, -3, -2, -3, -1, -3, -2, -3, -1,-3, -2, -3)
	 
	
	if wrap:
		patternA = np.append(patternA, patternA[0])
		patternB = np.append(patternB, patternB[0])
		w = np.append(w, w[0])
		
	if len(patternA) != len(w):
		print('Error: Length of pattern needs to be same length as the weights.')
		return
	
	def delta(m,n):
		if(m > n):
			return 1
		else:
			return 0
		
	def phi(a,w,i):
		j = i - 1
		if i >= 3 and a[i-1]== 0.0:
			j = i - 1 - delta(a[i-2],a[i-1])*delta(w[i-2],w[i-1])
		if i >= 5 and a[i-1]==0.0 and a[i-2]==0.0:
			j = i - 1 - 3*(delta(a[i-4],a[i-3])*delta(w[i-4],w[i-3])*delta(a[i-4],a[i-2])*delta(w[i-4],w[i-2])*delta(a[i-4],a[i-1])*delta(w[i-4],w[i-1]))
		return j
	
	def syncopation(patternA, patternB, w, B):
		w_out = np.zeros(len(w), dtype=int)
		n = len(w)
		S = 0
		for i in range(1,n):
			j = phi(patternA, w, i)
			k = phi(patternB, w, i)
			Swb = delta(w[i],w[k])*delta(patternB[k],patternB[i])
			Sws = delta(w[i],w[j])*delta(patternA[j],patternA[i])
			Swb1 = delta(1, Swb)
			Wb = w[i] - w[k] + 2 + 3*delta(1,patternA[i]+patternB[i])
			Ws = w[i] - w[j] + 1 + 4*delta(1,patternA[i]+patternB[i])
			
			w_out[i] = Swb*Wb + Sws*Ws*Swb1
		S = sum(w_out)
		return S, w_out
	
	output = syncopation(patternA, patternB, w, 32)
	
	
	return output

def calculate(pattern, wrap = True, weights = None, verbose=False):
	"""
	This function wraps both syncopation index calculations.

	Parameters
	----------
	patternA : Numpy array
		The first rhythm pattern, usually the snare.
	patternB : Numpy array
		The second rhythm pattern, usually the kick.
	wrap : Boolean, optional
		Whether to add the first event to the end. The default is True.
	weights : Numpy array, optional
		Custom weights for the SI calculation. The default is None.
	verbose : Boolean, optional
		If true, prints the syncopation index values.

	Returns
	-------
	hSI : Float
		Hoesl's syncopation index.
	wSI : Float
		Witek's syncopation index.

	"""
	
	# input check
	assert pattern.shape[0] == 3, 'Wrong shape of pattern, should be 3xn!'
	
	
	# Calculates and reports the SI, only the SI
	

	hSI = syncopationIndexHoesl(pattern, wrap, weights)[0]
	wSI = syncopationIndexWitek(pattern, wrap, weights)[0]
	if verbose:
		print('hSI is: ' + str(round(hSI,3)) + ' wSI is: ' + str(round(wSI,3)))

	
	return hSI, wSI



#%% Work in progress from here and below

def kComplexity(pattern, joint=False):
	'''
	This should calculate the Kolmogorov complexity,
	as defined in Li & Sleep, 2004.

	Parameters
	----------
	pattern : Numpy array
		The rhythm pattern to process.
	joint : Boolean
		Set to true to get the kComplexity over a tiled array of snare and kick
		Set to false to get the sum of kComplexity for snare and kick respectively

	Returns
	-------
	Kest : Integer
		The estimated Kolmogorov complexity

	'''
	def calc_kComplexity(pattern):
		dictionary = {}
		w = ''
		Kest = 0
		
		for n in pattern:
			C = n
			wC = w+C
			if wC in dictionary:
				w = wC;
			else:
				Kest = Kest+1
				dictionary[wC] = wC
				w = ''
		
		if w != '':
			Kest = Kest+1
		return Kest
	
	
	# Run on both snare and kick, then sum?
	if not joint:
		Kest_snare = calc_kComplexity(str(pattern[1,]).replace('[', '').replace(']', '')) # snare
		Kest_kick = calc_kComplexity(str(pattern[2,]).replace('[', '').replace(']', ''))  # kick
		Kout = Kest_snare + Kest_kick
	else:
		tiledPattern = str(pattern[1,]).replace('[', '').replace(']', '')+ str(pattern[2,]).replace('[', '').replace(']', '')
		Kout = calc_kComplexity(tiledPattern)

	
	return Kout


def entropy(singlePattern, base=None):
	'''
	Calculates entropy

	Parameters
	----------
	singlePattern : numpy array
		Pattern to calculate entropy for.
	base : Integer/float, optional
		The base for the entropy. The default is None.

	Returns
	-------
	Integer/float
		Entropy.

	'''

	n_labels = len(singlePattern)

	if n_labels <= 1:
		return 0

	value,counts = np.unique(singlePattern, return_counts=True)
	probs = counts / n_labels
	n_classes = np.count_nonzero(probs)

	if n_classes <= 1:
		return 0

	ent = 0.

	# Compute entropy
	base = e if base is None else base
	for i in probs:
		ent -= i * log(i, base)

	return ent


def movingEntropy(pattern, sliceSize=4, jumpSize=2):
	'''
	Returns the std of the entropies of a moving window over a pattern

	Parameters
	----------
	pattern : Numpy array
		The pattern to do the calculation over.
	sliceSize : Integer, optional
		The length of each slice. The default is 4.
	jumpSize : Integer, optional
		The distance between each window. The default is 2.

	Returns
	-------
	stdEntropy : Float
		The standard deviation of the entropies calculated.

	'''
	
	maxLength = len(pattern)
	entropies = []
	# double pattern to handle end
	pattern = np.tile(pattern,2)
	
	for n in np.arange(0, maxLength, jumpSize):
		thisSlice = pattern[n:n+sliceSize]
		thisEntropy = entropy(thisSlice)
		entropies.append(thisEntropy)
	
	stdEntropy = np.array(entropies).std()
	return stdEntropy


