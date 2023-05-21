#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on maio 12, 2023, at 15:34
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Motor Imagery'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'name': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\migue\\OneDrive\\Ambiente de Trabalho\\EEG stuff\\Motor Imagery\\Protocol\\MotorImageryExp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "WelcomeScreen" ---
textWelcomeMessage = visual.TextStim(win=win, name='textWelcomeMessage',
    text='Bem-Vindo ao Experimento!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "blank200" ---
textBlank200 = visual.TextStim(win=win, name='textBlank200',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "StartScreen" ---
textOrientationMessage = visual.TextStim(win=win, name='textOrientationMessage',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()

# --- Initialize components for Routine "start" ---
polygon_start = visual.Rect(
    win=win, name='polygon_start',
    width=(0.2, 0.4)[0], height=(0.2, 0.4)[1],
    ori=0.0, pos=(-0.80,-0.5), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 1.0000, 1.0000], fillColor=[-1.0000, 1.0000, 1.0000],
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "rest" ---
textrest = visual.TextStim(win=win, name='textrest',
    text='Descansa durante 4s',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
polygon_rest = visual.Rect(
    win=win, name='polygon_rest',
    width=(0.2, 0.4)[0], height=(0.2, 0.4)[1],
    ori=0.0, pos=(-0.80,-0.5), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "task" ---
polygonDE = visual.Rect(
    win=win, name='polygonDE',
    width=(0.2, 0.4)[0], height=(0.2, 0.4)[1],
    ori=0.0, pos=(-0.80,-0.5), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "Start2Screen" ---
textOrientationMessage2 = visual.TextStim(win=win, name='textOrientationMessage2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyOrientation2Message = keyboard.Keyboard()

# --- Initialize components for Routine "start" ---
polygon_start = visual.Rect(
    win=win, name='polygon_start',
    width=(0.2, 0.4)[0], height=(0.2, 0.4)[1],
    ori=0.0, pos=(-0.80,-0.5), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 1.0000, 1.0000], fillColor=[-1.0000, 1.0000, 1.0000],
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "rest" ---
textrest = visual.TextStim(win=win, name='textrest',
    text='Descansa durante 4s',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
polygon_rest = visual.Rect(
    win=win, name='polygon_rest',
    width=(0.2, 0.4)[0], height=(0.2, 0.4)[1],
    ori=0.0, pos=(-0.80,-0.5), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "task2" ---
polygonPP = visual.Rect(
    win=win, name='polygonPP',
    width=(0.2, 0.4)[0], height=(0.2, 0.4)[1],
    ori=0.0, pos=(-0.80,-0.5), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "GoodByeScreen" ---
textGoodBuyMessage = visual.TextStim(win=win, name='textGoodBuyMessage',
    text='Obrigado por participar',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "WelcomeScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
WelcomeScreenComponents = [textWelcomeMessage]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "WelcomeScreen" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcomeMessage* updates
    if textWelcomeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcomeMessage.frameNStart = frameN  # exact frame index
        textWelcomeMessage.tStart = t  # local t and not account for scr refresh
        textWelcomeMessage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcomeMessage, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textWelcomeMessage.started')
        textWelcomeMessage.setAutoDraw(True)
    if textWelcomeMessage.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textWelcomeMessage.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            textWelcomeMessage.tStop = t  # not accounting for scr refresh
            textWelcomeMessage.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcomeMessage.stopped')
            textWelcomeMessage.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "WelcomeScreen" ---
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "blank200" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank200Components = [textBlank200]
for thisComponent in blank200Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank200" ---
while continueRoutine and routineTimer.getTime() < 0.2:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank200* updates
    if textBlank200.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank200.frameNStart = frameN  # exact frame index
        textBlank200.tStart = t  # local t and not account for scr refresh
        textBlank200.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank200, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textBlank200.started')
        textBlank200.setAutoDraw(True)
    if textBlank200.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank200.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            textBlank200.tStop = t  # not accounting for scr refresh
            textBlank200.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBlank200.stopped')
            textBlank200.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank200Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank200" ---
for thisComponent in blank200Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.200000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Stimulation.xlsx'),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "StartScreen" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        textOrientationMessage.setText(instructions1)
        keyWelcome.keys = []
        keyWelcome.rt = []
        _keyWelcome_allKeys = []
        # keep track of which components have finished
        StartScreenComponents = [textOrientationMessage, keyWelcome]
        for thisComponent in StartScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "StartScreen" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textOrientationMessage* updates
            if textOrientationMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textOrientationMessage.frameNStart = frameN  # exact frame index
                textOrientationMessage.tStart = t  # local t and not account for scr refresh
                textOrientationMessage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOrientationMessage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOrientationMessage.started')
                textOrientationMessage.setAutoDraw(True)
            
            # *keyWelcome* updates
            waitOnFlip = False
            if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyWelcome.frameNStart = frameN  # exact frame index
                keyWelcome.tStart = t  # local t and not account for scr refresh
                keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyWelcome.started')
                keyWelcome.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyWelcome.status == STARTED and not waitOnFlip:
                theseKeys = keyWelcome.getKeys(keyList=['space'], waitRelease=False)
                _keyWelcome_allKeys.extend(theseKeys)
                if len(_keyWelcome_allKeys):
                    keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
                    keyWelcome.rt = _keyWelcome_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StartScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "StartScreen" ---
        for thisComponent in StartScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if keyWelcome.keys in ['', [], None]:  # No response was made
            keyWelcome.keys = None
        trials_3.addData('keyWelcome.keys',keyWelcome.keys)
        if keyWelcome.keys != None:  # we had a response
            trials_3.addData('keyWelcome.rt', keyWelcome.rt)
        # the Routine "StartScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "start" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        startComponents = [polygon_start]
        for thisComponent in startComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_start* updates
            if polygon_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_start.frameNStart = frameN  # exact frame index
                polygon_start.tStart = t  # local t and not account for scr refresh
                polygon_start.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_start, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_start.started')
                polygon_start.setAutoDraw(True)
            if polygon_start.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_start.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_start.tStop = t  # not accounting for scr refresh
                    polygon_start.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_start.stopped')
                    polygon_start.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start" ---
        for thisComponent in startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        imageryTrials = data.TrialHandler(nReps=15.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Stimulation.xlsx'),
            seed=None, name='imageryTrials')
        thisExp.addLoop(imageryTrials)  # add the loop to the experiment
        thisImageryTrial = imageryTrials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisImageryTrial.rgb)
        if thisImageryTrial != None:
            for paramName in thisImageryTrial:
                exec('{} = thisImageryTrial[paramName]'.format(paramName))
        
        for thisImageryTrial in imageryTrials:
            currentLoop = imageryTrials
            # abbreviate parameter names if possible (e.g. rgb = thisImageryTrial.rgb)
            if thisImageryTrial != None:
                for paramName in thisImageryTrial:
                    exec('{} = thisImageryTrial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            restComponents = [textrest, polygon_rest]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            while continueRoutine and routineTimer.getTime() < 4.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textrest* updates
                if textrest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textrest.frameNStart = frameN  # exact frame index
                    textrest.tStart = t  # local t and not account for scr refresh
                    textrest.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textrest, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textrest.started')
                    textrest.setAutoDraw(True)
                if textrest.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textrest.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        textrest.tStop = t  # not accounting for scr refresh
                        textrest.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textrest.stopped')
                        textrest.setAutoDraw(False)
                
                # *polygon_rest* updates
                if polygon_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_rest.frameNStart = frameN  # exact frame index
                    polygon_rest.tStart = t  # local t and not account for scr refresh
                    polygon_rest.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_rest, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_rest.started')
                    polygon_rest.setAutoDraw(True)
                if polygon_rest.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_rest.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_rest.tStop = t  # not accounting for scr refresh
                        polygon_rest.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_rest.stopped')
                        polygon_rest.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.000000)
            
            # --- Prepare to start Routine "task" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            polygonDE.setFillColor([0.0000, 0.0000, 0.0000])
            polygonDE.setLineColor([0.0000, 0.0000, 0.0000])
            image.setImage(individual_punho)
            # keep track of which components have finished
            taskComponents = [polygonDE, image]
            for thisComponent in taskComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "task" ---
            while continueRoutine and routineTimer.getTime() < 4.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *polygonDE* updates
                if polygonDE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygonDE.frameNStart = frameN  # exact frame index
                    polygonDE.tStart = t  # local t and not account for scr refresh
                    polygonDE.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygonDE, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygonDE.started')
                    polygonDE.setAutoDraw(True)
                if polygonDE.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygonDE.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        polygonDE.tStop = t  # not accounting for scr refresh
                        polygonDE.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygonDE.stopped')
                        polygonDE.setAutoDraw(False)
                # Run 'Each Frame' code from codeDE
                # Altera a cor do polígono com base em uma variável
                if individual_punho == "Imagens/right.png":
                    polygonDE.fillColor = (-0.35, -0.35, -0.35)
                
                # *image* updates
                if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.started')
                    image.setAutoDraw(True)
                if image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in taskComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "task" ---
            for thisComponent in taskComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.000000)
            thisExp.nextEntry()
            
        # completed 15.0 repeats of 'imageryTrials'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_3'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Stimulation.xlsx'),
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Start2Screen" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        textOrientationMessage2.setText(instructions2)
        keyOrientation2Message.keys = []
        keyOrientation2Message.rt = []
        _keyOrientation2Message_allKeys = []
        # keep track of which components have finished
        Start2ScreenComponents = [textOrientationMessage2, keyOrientation2Message]
        for thisComponent in Start2ScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Start2Screen" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textOrientationMessage2* updates
            if textOrientationMessage2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textOrientationMessage2.frameNStart = frameN  # exact frame index
                textOrientationMessage2.tStart = t  # local t and not account for scr refresh
                textOrientationMessage2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOrientationMessage2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOrientationMessage2.started')
                textOrientationMessage2.setAutoDraw(True)
            
            # *keyOrientation2Message* updates
            waitOnFlip = False
            if keyOrientation2Message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyOrientation2Message.frameNStart = frameN  # exact frame index
                keyOrientation2Message.tStart = t  # local t and not account for scr refresh
                keyOrientation2Message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyOrientation2Message, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyOrientation2Message.started')
                keyOrientation2Message.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyOrientation2Message.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyOrientation2Message.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyOrientation2Message.status == STARTED and not waitOnFlip:
                theseKeys = keyOrientation2Message.getKeys(keyList=['space'], waitRelease=False)
                _keyOrientation2Message_allKeys.extend(theseKeys)
                if len(_keyOrientation2Message_allKeys):
                    keyOrientation2Message.keys = _keyOrientation2Message_allKeys[-1].name  # just the last key pressed
                    keyOrientation2Message.rt = _keyOrientation2Message_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Start2ScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Start2Screen" ---
        for thisComponent in Start2ScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if keyOrientation2Message.keys in ['', [], None]:  # No response was made
            keyOrientation2Message.keys = None
        trials_4.addData('keyOrientation2Message.keys',keyOrientation2Message.keys)
        if keyOrientation2Message.keys != None:  # we had a response
            trials_4.addData('keyOrientation2Message.rt', keyOrientation2Message.rt)
        # the Routine "Start2Screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "start" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        startComponents = [polygon_start]
        for thisComponent in startComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_start* updates
            if polygon_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_start.frameNStart = frameN  # exact frame index
                polygon_start.tStart = t  # local t and not account for scr refresh
                polygon_start.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_start, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_start.started')
                polygon_start.setAutoDraw(True)
            if polygon_start.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_start.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_start.tStop = t  # not accounting for scr refresh
                    polygon_start.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_start.stopped')
                    polygon_start.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start" ---
        for thisComponent in startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        imageryTrials2 = data.TrialHandler(nReps=15.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Stimulation.xlsx'),
            seed=None, name='imageryTrials2')
        thisExp.addLoop(imageryTrials2)  # add the loop to the experiment
        thisImageryTrials2 = imageryTrials2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisImageryTrials2.rgb)
        if thisImageryTrials2 != None:
            for paramName in thisImageryTrials2:
                exec('{} = thisImageryTrials2[paramName]'.format(paramName))
        
        for thisImageryTrials2 in imageryTrials2:
            currentLoop = imageryTrials2
            # abbreviate parameter names if possible (e.g. rgb = thisImageryTrials2.rgb)
            if thisImageryTrials2 != None:
                for paramName in thisImageryTrials2:
                    exec('{} = thisImageryTrials2[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            restComponents = [textrest, polygon_rest]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest" ---
            while continueRoutine and routineTimer.getTime() < 4.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textrest* updates
                if textrest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textrest.frameNStart = frameN  # exact frame index
                    textrest.tStart = t  # local t and not account for scr refresh
                    textrest.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textrest, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textrest.started')
                    textrest.setAutoDraw(True)
                if textrest.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textrest.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        textrest.tStop = t  # not accounting for scr refresh
                        textrest.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textrest.stopped')
                        textrest.setAutoDraw(False)
                
                # *polygon_rest* updates
                if polygon_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_rest.frameNStart = frameN  # exact frame index
                    polygon_rest.tStart = t  # local t and not account for scr refresh
                    polygon_rest.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_rest, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_rest.started')
                    polygon_rest.setAutoDraw(True)
                if polygon_rest.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_rest.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_rest.tStop = t  # not accounting for scr refresh
                        polygon_rest.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_rest.stopped')
                        polygon_rest.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.000000)
            
            # --- Prepare to start Routine "task2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            polygonPP.setFillColor([-0.5500, -0.5500, -0.5500])
            polygonPP.setLineColor([-0.5500, -0.5500, -0.5500])
            image_2.setImage(ambos_punhos_pes)
            # keep track of which components have finished
            task2Components = [polygonPP, image_2]
            for thisComponent in task2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "task2" ---
            while continueRoutine and routineTimer.getTime() < 4.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *polygonPP* updates
                if polygonPP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygonPP.frameNStart = frameN  # exact frame index
                    polygonPP.tStart = t  # local t and not account for scr refresh
                    polygonPP.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygonPP, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygonPP.started')
                    polygonPP.setAutoDraw(True)
                if polygonPP.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygonPP.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        polygonPP.tStop = t  # not accounting for scr refresh
                        polygonPP.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygonPP.stopped')
                        polygonPP.setAutoDraw(False)
                # Run 'Each Frame' code from code
                # Altera a cor do polígono com base em uma variável
                if ambos_punhos_pes == "Imagens/up.png":
                    polygonPP.fillColor = (-0.9, -0.9, -0.9)
                
                # *image_2* updates
                if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.tStart = t  # local t and not account for scr refresh
                    image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.started')
                    image_2.setAutoDraw(True)
                if image_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_2.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        image_2.tStop = t  # not accounting for scr refresh
                        image_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_2.stopped')
                        image_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in task2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "task2" ---
            for thisComponent in task2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.000000)
            thisExp.nextEntry()
            
        # completed 15.0 repeats of 'imageryTrials2'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_4'
    
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials'


# --- Prepare to start Routine "GoodByeScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
GoodByeScreenComponents = [textGoodBuyMessage]
for thisComponent in GoodByeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GoodByeScreen" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textGoodBuyMessage* updates
    if textGoodBuyMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textGoodBuyMessage.frameNStart = frameN  # exact frame index
        textGoodBuyMessage.tStart = t  # local t and not account for scr refresh
        textGoodBuyMessage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textGoodBuyMessage, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textGoodBuyMessage.started')
        textGoodBuyMessage.setAutoDraw(True)
    if textGoodBuyMessage.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textGoodBuyMessage.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            textGoodBuyMessage.tStop = t  # not accounting for scr refresh
            textGoodBuyMessage.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textGoodBuyMessage.stopped')
            textGoodBuyMessage.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodByeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GoodByeScreen" ---
for thisComponent in GoodByeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
