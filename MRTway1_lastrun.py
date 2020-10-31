#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Mon Oct 26 09:44:17 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'MRTway1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Session': '001', 'Age': '', 'Sex': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sabrinado/Library/CELSYS/MRTway1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "testName"
testNameClock = core.Clock()
WelcomeScreen = visual.TextStim(win=win, name='WelcomeScreen',
    text='Mental Rotation Test (MRT)',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
introduction = visual.TextStim(win=win, name='introduction',
    text='This is a test of your ability to look at a drawing of a given object and find the same object within a set of dissimilar objects. The only diference between the original object and the chosen object will be that they are presented at different angles. An illustration of this principle is given below where the same single object is given in five different positions. Look at each of them to satisfy yourself that they are only presented at different angles from one another.',
    font='Times New Roman',
    pos=(0, 0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()
exampleText = visual.TextStim(win=win, name='exampleText',
    text='\nBelow are two drawings of new objects. They cannot be made to match the above five drawings. Please note that you may not turn over the objects. Satisfy yourself that they are different from the above.',
    font='Times New Roman',
    pos=(0, 0), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
responseIndicator = visual.TextStim(win=win, name='responseIndicator',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
example = visual.ImageStim(
    win=win,
    name='example', 
    image='example.jpg', mask=None,
    ori=0, pos=(0, 0.17), size=(0.80, 0.18),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sample2.jpg', mask=None,
    ori=0, pos=(0, -0.25), size=(0.70, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)

# Initialize components for Routine "Example"
ExampleClock = core.Clock()
practiceProblemInstructions = visual.TextStim(win=win, name='practiceProblemInstructions',
    text='Now let’s do some sample problems. For each problem there is a primary object on the far left. You are to determine which two of four objects to the right are the same object given on the far left. In each problem always two of the four drawings are the same object as the one on the left. You are to put Xs in the boxes below the correct ones, and leave the incorrect ones blank. The first sample problem is done for you.',
    font='Times New Roman',
    pos=(0, 0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
practiceProblemImage = visual.ImageStim(
    win=win,
    name='practiceProblemImage', 
    image='sampleProblem.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.70, 0.38),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
inputIndicatorPractice = visual.TextStim(win=win, name='inputIndicatorPractice',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
responseExample = keyboard.Keyboard()

# Initialize components for Routine "SameQuestion1"
SameQuestion1Clock = core.Clock()
sampleQuestionImage1 = visual.ImageStim(
    win=win,
    name='sampleQuestionImage1', 
    image='1example.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.60, 0.38),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
inputIndicatorSampleQuestion1 = visual.TextStim(win=win, name='inputIndicatorSampleQuestion1',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseSampleQuestion1 = keyboard.Keyboard()
SampleQuestionsInstructions = visual.TextStim(win=win, name='SampleQuestionsInstructions',
    text='Do the rest of the sample problems yourself. Which two drawings of the four on the right show the same object as the one on the left? There are always two and only two correct answers for each problem. Select the two correct drawings by pressing “1”, “2”,”3”, or “4”, selecting the picture from left to right. ',
    font='Times New Roman',
    pos=(0, 0.35), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "SampleQuestion2"
SampleQuestion2Clock = core.Clock()
sampleQuestionImage2 = visual.ImageStim(
    win=win,
    name='sampleQuestionImage2', 
    image='2example.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.60, 0.38),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
inputIndicatorSampleQuestion2 = visual.TextStim(win=win, name='inputIndicatorSampleQuestion2',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseSampleQuestion2 = keyboard.Keyboard()

# Initialize components for Routine "SampleQuestion3"
SampleQuestion3Clock = core.Clock()
sampleQuestionImage3 = visual.ImageStim(
    win=win,
    name='sampleQuestionImage3', 
    image='3example.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.60, 0.38),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
inputIndicatorSampleQuestion3 = visual.TextStim(win=win, name='inputIndicatorSampleQuestion3',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseSampleQuestion3 = keyboard.Keyboard()

# Initialize components for Routine "Answer"
AnswerClock = core.Clock()
SampleAnswers = visual.TextStim(win=win, name='SampleAnswers',
    text='Answers:       (1) first and second drawings are correct\n                    (2) first and third drawings are correct\n                       (3) second and third drawings are correct',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
inputIndicatorAnswer = visual.TextStim(win=win, name='inputIndicatorAnswer',
    text='Please press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.030, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseAnswer = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionsText = visual.TextStim(win=win, name='InstructionsText',
    text='This test has two parts. You will have 3 minutes for each of the two part has 10 questions. When you have finished Part I, STOP. Please do not go on to Part II until you are asked to do so. Remember: There are always two and only two correct answers for each item.\n\nWork as quickly as you can without sacrificing accuracy. Your score on this test will reflect both the correct and incorrect responses. Therefore, it will not be to your advantage to guess unless you have some idea which choice is correct.',
    font='Times New Roman',
    pos=(0, 0.15), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
IndicatorWarning = visual.TextStim(win=win, name='IndicatorWarning',
    text='Do Not Continue Until Asked To Do So. \n\nPress ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.050, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseInstructions = keyboard.Keyboard()

# Initialize components for Routine "Part1"
Part1Clock = core.Clock()
Part1Text = visual.TextStim(win=win, name='Part1Text',
    text='Part I.',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
responsePart1 = keyboard.Keyboard()

# Initialize components for Routine "Question1"
Question1Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.40, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='Press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.050, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
responseQuestion1 = keyboard.Keyboard()
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instrStop = visual.TextStim(win=win, name='instrStop',
    text='Stop.\n\nDo Not Continue Until Asked To Do So.',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stopIndicator = keyboard.Keyboard()

# Initialize components for Routine "Part2"
Part2Clock = core.Clock()
part2Indicator = visual.TextStim(win=win, name='part2Indicator',
    text='Part II',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
part2IndicatorResponse = keyboard.Keyboard()

# Initialize components for Routine "part2Questions"
part2QuestionsClock = core.Clock()
indicatorQuestionPart2 = visual.TextStim(win=win, name='indicatorQuestionPart2',
    text='Press ‘space’ to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.050, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyboardIndicator = keyboard.Keyboard()
part2Response = keyboard.Keyboard()
part2Images = visual.ImageStim(
    win=win,
    name='part2Images', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.40, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
EndScreen = visual.TextStim(win=win, name='EndScreen',
    text='Congrats! You have finished the test.\n\nThe End',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endResponse = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "testName"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
testNameComponents = [WelcomeScreen, key_resp_2]
for thisComponent in testNameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testNameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testName"-------
while continueRoutine:
    # get current time
    t = testNameClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testNameClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeScreen* updates
    if WelcomeScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeScreen.frameNStart = frameN  # exact frame index
        WelcomeScreen.tStart = t  # local t and not account for scr refresh
        WelcomeScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeScreen, 'tStartRefresh')  # time at next scr refresh
        WelcomeScreen.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testNameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testName"-------
for thisComponent in testNameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeScreen.started', WelcomeScreen.tStartRefresh)
thisExp.addData('WelcomeScreen.stopped', WelcomeScreen.tStopRefresh)
# the Routine "testName" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome_Screen"-------
continueRoutine = True
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
_keyWelcome_allKeys = []
# keep track of which components have finished
Welcome_ScreenComponents = [introduction, keyWelcome, exampleText, responseIndicator, example, image_2]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction* updates
    if introduction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        introduction.frameNStart = frameN  # exact frame index
        introduction.tStart = t  # local t and not account for scr refresh
        introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction, 'tStartRefresh')  # time at next scr refresh
        introduction.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
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
    
    # *exampleText* updates
    if exampleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exampleText.frameNStart = frameN  # exact frame index
        exampleText.tStart = t  # local t and not account for scr refresh
        exampleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exampleText, 'tStartRefresh')  # time at next scr refresh
        exampleText.setAutoDraw(True)
    
    # *responseIndicator* updates
    if responseIndicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator.frameNStart = frameN  # exact frame index
        responseIndicator.tStart = t  # local t and not account for scr refresh
        responseIndicator.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator, 'tStartRefresh')  # time at next scr refresh
        responseIndicator.setAutoDraw(True)
    
    # *example* updates
    if example.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        example.frameNStart = frameN  # exact frame index
        example.tStart = t  # local t and not account for scr refresh
        example.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example, 'tStartRefresh')  # time at next scr refresh
        example.setAutoDraw(True)
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction.started', introduction.tStartRefresh)
thisExp.addData('introduction.stopped', introduction.tStopRefresh)
thisExp.addData('exampleText.started', exampleText.tStartRefresh)
thisExp.addData('exampleText.stopped', exampleText.tStopRefresh)
thisExp.addData('responseIndicator.started', responseIndicator.tStartRefresh)
thisExp.addData('responseIndicator.stopped', responseIndicator.tStopRefresh)
thisExp.addData('example.started', example.tStartRefresh)
thisExp.addData('example.stopped', example.tStopRefresh)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Example"-------
continueRoutine = True
# update component parameters for each repeat
responseExample.keys = []
responseExample.rt = []
_responseExample_allKeys = []
# keep track of which components have finished
ExampleComponents = [practiceProblemInstructions, practiceProblemImage, inputIndicatorPractice, responseExample]
for thisComponent in ExampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Example"-------
while continueRoutine:
    # get current time
    t = ExampleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExampleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceProblemInstructions* updates
    if practiceProblemInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceProblemInstructions.frameNStart = frameN  # exact frame index
        practiceProblemInstructions.tStart = t  # local t and not account for scr refresh
        practiceProblemInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceProblemInstructions, 'tStartRefresh')  # time at next scr refresh
        practiceProblemInstructions.setAutoDraw(True)
    
    # *practiceProblemImage* updates
    if practiceProblemImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceProblemImage.frameNStart = frameN  # exact frame index
        practiceProblemImage.tStart = t  # local t and not account for scr refresh
        practiceProblemImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceProblemImage, 'tStartRefresh')  # time at next scr refresh
        practiceProblemImage.setAutoDraw(True)
    
    # *inputIndicatorPractice* updates
    if inputIndicatorPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inputIndicatorPractice.frameNStart = frameN  # exact frame index
        inputIndicatorPractice.tStart = t  # local t and not account for scr refresh
        inputIndicatorPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inputIndicatorPractice, 'tStartRefresh')  # time at next scr refresh
        inputIndicatorPractice.setAutoDraw(True)
    
    # *responseExample* updates
    waitOnFlip = False
    if responseExample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseExample.frameNStart = frameN  # exact frame index
        responseExample.tStart = t  # local t and not account for scr refresh
        responseExample.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseExample, 'tStartRefresh')  # time at next scr refresh
        responseExample.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseExample.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseExample.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseExample.status == STARTED and not waitOnFlip:
        theseKeys = responseExample.getKeys(keyList=['space'], waitRelease=False)
        _responseExample_allKeys.extend(theseKeys)
        if len(_responseExample_allKeys):
            responseExample.keys = _responseExample_allKeys[-1].name  # just the last key pressed
            responseExample.rt = _responseExample_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Example"-------
for thisComponent in ExampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceProblemInstructions.started', practiceProblemInstructions.tStartRefresh)
thisExp.addData('practiceProblemInstructions.stopped', practiceProblemInstructions.tStopRefresh)
thisExp.addData('practiceProblemImage.started', practiceProblemImage.tStartRefresh)
thisExp.addData('practiceProblemImage.stopped', practiceProblemImage.tStopRefresh)
thisExp.addData('inputIndicatorPractice.started', inputIndicatorPractice.tStartRefresh)
thisExp.addData('inputIndicatorPractice.stopped', inputIndicatorPractice.tStopRefresh)
# the Routine "Example" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SameQuestion1"-------
continueRoutine = True
# update component parameters for each repeat
responseSampleQuestion1.keys = []
responseSampleQuestion1.rt = []
_responseSampleQuestion1_allKeys = []
# keep track of which components have finished
SameQuestion1Components = [sampleQuestionImage1, inputIndicatorSampleQuestion1, responseSampleQuestion1, SampleQuestionsInstructions]
for thisComponent in SameQuestion1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SameQuestion1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SameQuestion1"-------
while continueRoutine:
    # get current time
    t = SameQuestion1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SameQuestion1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sampleQuestionImage1* updates
    if sampleQuestionImage1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleQuestionImage1.frameNStart = frameN  # exact frame index
        sampleQuestionImage1.tStart = t  # local t and not account for scr refresh
        sampleQuestionImage1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleQuestionImage1, 'tStartRefresh')  # time at next scr refresh
        sampleQuestionImage1.setAutoDraw(True)
    
    # *inputIndicatorSampleQuestion1* updates
    if inputIndicatorSampleQuestion1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inputIndicatorSampleQuestion1.frameNStart = frameN  # exact frame index
        inputIndicatorSampleQuestion1.tStart = t  # local t and not account for scr refresh
        inputIndicatorSampleQuestion1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inputIndicatorSampleQuestion1, 'tStartRefresh')  # time at next scr refresh
        inputIndicatorSampleQuestion1.setAutoDraw(True)
    
    # *responseSampleQuestion1* updates
    waitOnFlip = False
    if responseSampleQuestion1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseSampleQuestion1.frameNStart = frameN  # exact frame index
        responseSampleQuestion1.tStart = t  # local t and not account for scr refresh
        responseSampleQuestion1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseSampleQuestion1, 'tStartRefresh')  # time at next scr refresh
        responseSampleQuestion1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseSampleQuestion1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseSampleQuestion1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseSampleQuestion1.status == STARTED and not waitOnFlip:
        theseKeys = responseSampleQuestion1.getKeys(keyList=['space'], waitRelease=False)
        _responseSampleQuestion1_allKeys.extend(theseKeys)
        if len(_responseSampleQuestion1_allKeys):
            responseSampleQuestion1.keys = _responseSampleQuestion1_allKeys[-1].name  # just the last key pressed
            responseSampleQuestion1.rt = _responseSampleQuestion1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *SampleQuestionsInstructions* updates
    if SampleQuestionsInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SampleQuestionsInstructions.frameNStart = frameN  # exact frame index
        SampleQuestionsInstructions.tStart = t  # local t and not account for scr refresh
        SampleQuestionsInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SampleQuestionsInstructions, 'tStartRefresh')  # time at next scr refresh
        SampleQuestionsInstructions.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SameQuestion1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SameQuestion1"-------
for thisComponent in SameQuestion1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sampleQuestionImage1.started', sampleQuestionImage1.tStartRefresh)
thisExp.addData('sampleQuestionImage1.stopped', sampleQuestionImage1.tStopRefresh)
thisExp.addData('inputIndicatorSampleQuestion1.started', inputIndicatorSampleQuestion1.tStartRefresh)
thisExp.addData('inputIndicatorSampleQuestion1.stopped', inputIndicatorSampleQuestion1.tStopRefresh)
thisExp.addData('SampleQuestionsInstructions.started', SampleQuestionsInstructions.tStartRefresh)
thisExp.addData('SampleQuestionsInstructions.stopped', SampleQuestionsInstructions.tStopRefresh)
# the Routine "SameQuestion1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SampleQuestion2"-------
continueRoutine = True
# update component parameters for each repeat
responseSampleQuestion2.keys = []
responseSampleQuestion2.rt = []
_responseSampleQuestion2_allKeys = []
# keep track of which components have finished
SampleQuestion2Components = [sampleQuestionImage2, inputIndicatorSampleQuestion2, responseSampleQuestion2]
for thisComponent in SampleQuestion2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SampleQuestion2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SampleQuestion2"-------
while continueRoutine:
    # get current time
    t = SampleQuestion2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SampleQuestion2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sampleQuestionImage2* updates
    if sampleQuestionImage2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleQuestionImage2.frameNStart = frameN  # exact frame index
        sampleQuestionImage2.tStart = t  # local t and not account for scr refresh
        sampleQuestionImage2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleQuestionImage2, 'tStartRefresh')  # time at next scr refresh
        sampleQuestionImage2.setAutoDraw(True)
    
    # *inputIndicatorSampleQuestion2* updates
    if inputIndicatorSampleQuestion2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inputIndicatorSampleQuestion2.frameNStart = frameN  # exact frame index
        inputIndicatorSampleQuestion2.tStart = t  # local t and not account for scr refresh
        inputIndicatorSampleQuestion2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inputIndicatorSampleQuestion2, 'tStartRefresh')  # time at next scr refresh
        inputIndicatorSampleQuestion2.setAutoDraw(True)
    
    # *responseSampleQuestion2* updates
    waitOnFlip = False
    if responseSampleQuestion2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseSampleQuestion2.frameNStart = frameN  # exact frame index
        responseSampleQuestion2.tStart = t  # local t and not account for scr refresh
        responseSampleQuestion2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseSampleQuestion2, 'tStartRefresh')  # time at next scr refresh
        responseSampleQuestion2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseSampleQuestion2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseSampleQuestion2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseSampleQuestion2.status == STARTED and not waitOnFlip:
        theseKeys = responseSampleQuestion2.getKeys(keyList=['space'], waitRelease=False)
        _responseSampleQuestion2_allKeys.extend(theseKeys)
        if len(_responseSampleQuestion2_allKeys):
            responseSampleQuestion2.keys = _responseSampleQuestion2_allKeys[-1].name  # just the last key pressed
            responseSampleQuestion2.rt = _responseSampleQuestion2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SampleQuestion2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SampleQuestion2"-------
for thisComponent in SampleQuestion2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sampleQuestionImage2.started', sampleQuestionImage2.tStartRefresh)
thisExp.addData('sampleQuestionImage2.stopped', sampleQuestionImage2.tStopRefresh)
thisExp.addData('inputIndicatorSampleQuestion2.started', inputIndicatorSampleQuestion2.tStartRefresh)
thisExp.addData('inputIndicatorSampleQuestion2.stopped', inputIndicatorSampleQuestion2.tStopRefresh)
# the Routine "SampleQuestion2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SampleQuestion3"-------
continueRoutine = True
# update component parameters for each repeat
responseSampleQuestion3.keys = []
responseSampleQuestion3.rt = []
_responseSampleQuestion3_allKeys = []
# keep track of which components have finished
SampleQuestion3Components = [sampleQuestionImage3, inputIndicatorSampleQuestion3, responseSampleQuestion3]
for thisComponent in SampleQuestion3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SampleQuestion3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SampleQuestion3"-------
while continueRoutine:
    # get current time
    t = SampleQuestion3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SampleQuestion3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sampleQuestionImage3* updates
    if sampleQuestionImage3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleQuestionImage3.frameNStart = frameN  # exact frame index
        sampleQuestionImage3.tStart = t  # local t and not account for scr refresh
        sampleQuestionImage3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleQuestionImage3, 'tStartRefresh')  # time at next scr refresh
        sampleQuestionImage3.setAutoDraw(True)
    
    # *inputIndicatorSampleQuestion3* updates
    if inputIndicatorSampleQuestion3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inputIndicatorSampleQuestion3.frameNStart = frameN  # exact frame index
        inputIndicatorSampleQuestion3.tStart = t  # local t and not account for scr refresh
        inputIndicatorSampleQuestion3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inputIndicatorSampleQuestion3, 'tStartRefresh')  # time at next scr refresh
        inputIndicatorSampleQuestion3.setAutoDraw(True)
    
    # *responseSampleQuestion3* updates
    waitOnFlip = False
    if responseSampleQuestion3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseSampleQuestion3.frameNStart = frameN  # exact frame index
        responseSampleQuestion3.tStart = t  # local t and not account for scr refresh
        responseSampleQuestion3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseSampleQuestion3, 'tStartRefresh')  # time at next scr refresh
        responseSampleQuestion3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseSampleQuestion3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseSampleQuestion3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseSampleQuestion3.status == STARTED and not waitOnFlip:
        theseKeys = responseSampleQuestion3.getKeys(keyList=['space'], waitRelease=False)
        _responseSampleQuestion3_allKeys.extend(theseKeys)
        if len(_responseSampleQuestion3_allKeys):
            responseSampleQuestion3.keys = _responseSampleQuestion3_allKeys[-1].name  # just the last key pressed
            responseSampleQuestion3.rt = _responseSampleQuestion3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SampleQuestion3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SampleQuestion3"-------
for thisComponent in SampleQuestion3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sampleQuestionImage3.started', sampleQuestionImage3.tStartRefresh)
thisExp.addData('sampleQuestionImage3.stopped', sampleQuestionImage3.tStopRefresh)
thisExp.addData('inputIndicatorSampleQuestion3.started', inputIndicatorSampleQuestion3.tStartRefresh)
thisExp.addData('inputIndicatorSampleQuestion3.stopped', inputIndicatorSampleQuestion3.tStopRefresh)
# the Routine "SampleQuestion3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Answer"-------
continueRoutine = True
# update component parameters for each repeat
responseAnswer.keys = []
responseAnswer.rt = []
_responseAnswer_allKeys = []
# keep track of which components have finished
AnswerComponents = [SampleAnswers, inputIndicatorAnswer, responseAnswer]
for thisComponent in AnswerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
AnswerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Answer"-------
while continueRoutine:
    # get current time
    t = AnswerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=AnswerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SampleAnswers* updates
    if SampleAnswers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SampleAnswers.frameNStart = frameN  # exact frame index
        SampleAnswers.tStart = t  # local t and not account for scr refresh
        SampleAnswers.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SampleAnswers, 'tStartRefresh')  # time at next scr refresh
        SampleAnswers.setAutoDraw(True)
    
    # *inputIndicatorAnswer* updates
    if inputIndicatorAnswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inputIndicatorAnswer.frameNStart = frameN  # exact frame index
        inputIndicatorAnswer.tStart = t  # local t and not account for scr refresh
        inputIndicatorAnswer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inputIndicatorAnswer, 'tStartRefresh')  # time at next scr refresh
        inputIndicatorAnswer.setAutoDraw(True)
    
    # *responseAnswer* updates
    waitOnFlip = False
    if responseAnswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseAnswer.frameNStart = frameN  # exact frame index
        responseAnswer.tStart = t  # local t and not account for scr refresh
        responseAnswer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseAnswer, 'tStartRefresh')  # time at next scr refresh
        responseAnswer.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseAnswer.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseAnswer.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseAnswer.status == STARTED and not waitOnFlip:
        theseKeys = responseAnswer.getKeys(keyList=['space'], waitRelease=False)
        _responseAnswer_allKeys.extend(theseKeys)
        if len(_responseAnswer_allKeys):
            responseAnswer.keys = _responseAnswer_allKeys[-1].name  # just the last key pressed
            responseAnswer.rt = _responseAnswer_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AnswerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Answer"-------
for thisComponent in AnswerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SampleAnswers.started', SampleAnswers.tStartRefresh)
thisExp.addData('SampleAnswers.stopped', SampleAnswers.tStopRefresh)
thisExp.addData('inputIndicatorAnswer.started', inputIndicatorAnswer.tStartRefresh)
thisExp.addData('inputIndicatorAnswer.stopped', inputIndicatorAnswer.tStopRefresh)
# the Routine "Answer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
responseInstructions.keys = []
responseInstructions.rt = []
_responseInstructions_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstructionsText, IndicatorWarning, responseInstructions]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsText* updates
    if InstructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText.frameNStart = frameN  # exact frame index
        InstructionsText.tStart = t  # local t and not account for scr refresh
        InstructionsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText, 'tStartRefresh')  # time at next scr refresh
        InstructionsText.setAutoDraw(True)
    
    # *IndicatorWarning* updates
    if IndicatorWarning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IndicatorWarning.frameNStart = frameN  # exact frame index
        IndicatorWarning.tStart = t  # local t and not account for scr refresh
        IndicatorWarning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IndicatorWarning, 'tStartRefresh')  # time at next scr refresh
        IndicatorWarning.setAutoDraw(True)
    
    # *responseInstructions* updates
    waitOnFlip = False
    if responseInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseInstructions.frameNStart = frameN  # exact frame index
        responseInstructions.tStart = t  # local t and not account for scr refresh
        responseInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseInstructions, 'tStartRefresh')  # time at next scr refresh
        responseInstructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responseInstructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responseInstructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responseInstructions.status == STARTED and not waitOnFlip:
        theseKeys = responseInstructions.getKeys(keyList=['space'], waitRelease=False)
        _responseInstructions_allKeys.extend(theseKeys)
        if len(_responseInstructions_allKeys):
            responseInstructions.keys = _responseInstructions_allKeys[-1].name  # just the last key pressed
            responseInstructions.rt = _responseInstructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionsText.started', InstructionsText.tStartRefresh)
thisExp.addData('InstructionsText.stopped', InstructionsText.tStopRefresh)
thisExp.addData('IndicatorWarning.started', IndicatorWarning.tStartRefresh)
thisExp.addData('IndicatorWarning.stopped', IndicatorWarning.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Part1"-------
continueRoutine = True
# update component parameters for each repeat
responsePart1.keys = []
responsePart1.rt = []
_responsePart1_allKeys = []
# keep track of which components have finished
Part1Components = [Part1Text, responsePart1]
for thisComponent in Part1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Part1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Part1"-------
while continueRoutine:
    # get current time
    t = Part1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Part1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Part1Text* updates
    if Part1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Part1Text.frameNStart = frameN  # exact frame index
        Part1Text.tStart = t  # local t and not account for scr refresh
        Part1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Part1Text, 'tStartRefresh')  # time at next scr refresh
        Part1Text.setAutoDraw(True)
    
    # *responsePart1* updates
    waitOnFlip = False
    if responsePart1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responsePart1.frameNStart = frameN  # exact frame index
        responsePart1.tStart = t  # local t and not account for scr refresh
        responsePart1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responsePart1, 'tStartRefresh')  # time at next scr refresh
        responsePart1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(responsePart1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(responsePart1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if responsePart1.status == STARTED and not waitOnFlip:
        theseKeys = responsePart1.getKeys(keyList=['space'], waitRelease=False)
        _responsePart1_allKeys.extend(theseKeys)
        if len(_responsePart1_allKeys):
            responsePart1.keys = _responsePart1_allKeys[-1].name  # just the last key pressed
            responsePart1.rt = _responsePart1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part1"-------
for thisComponent in Part1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Part1Text.started', Part1Text.tStartRefresh)
thisExp.addData('Part1Text.stopped', Part1Text.tStopRefresh)
# the Routine "Part1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial1234.xlsx'),
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
    
    # ------Prepare to start Routine "Question1"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Image)
    responseQuestion1.keys = []
    responseQuestion1.rt = []
    _responseQuestion1_allKeys = []
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    Question1Components = [image, text, responseQuestion1, key_resp]
    for thisComponent in Question1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Question1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Question1"-------
    while continueRoutine:
        # get current time
        t = Question1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Question1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *responseQuestion1* updates
        waitOnFlip = False
        if responseQuestion1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            responseQuestion1.frameNStart = frameN  # exact frame index
            responseQuestion1.tStart = t  # local t and not account for scr refresh
            responseQuestion1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responseQuestion1, 'tStartRefresh')  # time at next scr refresh
            responseQuestion1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(responseQuestion1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(responseQuestion1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if responseQuestion1.status == STARTED and not waitOnFlip:
            theseKeys = responseQuestion1.getKeys(keyList=['space'], waitRelease=False)
            _responseQuestion1_allKeys.extend(theseKeys)
            if len(_responseQuestion1_allKeys):
                responseQuestion1.keys = _responseQuestion1_allKeys[-1].name  # just the last key pressed
                responseQuestion1.rt = _responseQuestion1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Question1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Question1"-------
    for thisComponent in Question1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if responseQuestion1.keys in ['', [], None]:  # No response was made
        responseQuestion1.keys = None
    trials.addData('responseQuestion1.keys',responseQuestion1.keys)
    if responseQuestion1.keys != None:  # we had a response
        trials.addData('responseQuestion1.rt', responseQuestion1.rt)
    trials.addData('responseQuestion1.started', responseQuestion1.tStartRefresh)
    trials.addData('responseQuestion1.stopped', responseQuestion1.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "Question1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
stopIndicator.keys = []
stopIndicator.rt = []
_stopIndicator_allKeys = []
# keep track of which components have finished
instrComponents = [instrStop, stopIndicator]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrStop* updates
    if instrStop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrStop.frameNStart = frameN  # exact frame index
        instrStop.tStart = t  # local t and not account for scr refresh
        instrStop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrStop, 'tStartRefresh')  # time at next scr refresh
        instrStop.setAutoDraw(True)
    
    # *stopIndicator* updates
    waitOnFlip = False
    if stopIndicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stopIndicator.frameNStart = frameN  # exact frame index
        stopIndicator.tStart = t  # local t and not account for scr refresh
        stopIndicator.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stopIndicator, 'tStartRefresh')  # time at next scr refresh
        stopIndicator.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(stopIndicator.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(stopIndicator.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if stopIndicator.status == STARTED and not waitOnFlip:
        theseKeys = stopIndicator.getKeys(keyList=['space'], waitRelease=False)
        _stopIndicator_allKeys.extend(theseKeys)
        if len(_stopIndicator_allKeys):
            stopIndicator.keys = _stopIndicator_allKeys[-1].name  # just the last key pressed
            stopIndicator.rt = _stopIndicator_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrStop.started', instrStop.tStartRefresh)
thisExp.addData('instrStop.stopped', instrStop.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Part2"-------
continueRoutine = True
# update component parameters for each repeat
part2IndicatorResponse.keys = []
part2IndicatorResponse.rt = []
_part2IndicatorResponse_allKeys = []
# keep track of which components have finished
Part2Components = [part2Indicator, part2IndicatorResponse]
for thisComponent in Part2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Part2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Part2"-------
while continueRoutine:
    # get current time
    t = Part2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Part2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *part2Indicator* updates
    if part2Indicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part2Indicator.frameNStart = frameN  # exact frame index
        part2Indicator.tStart = t  # local t and not account for scr refresh
        part2Indicator.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part2Indicator, 'tStartRefresh')  # time at next scr refresh
        part2Indicator.setAutoDraw(True)
    
    # *part2IndicatorResponse* updates
    waitOnFlip = False
    if part2IndicatorResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part2IndicatorResponse.frameNStart = frameN  # exact frame index
        part2IndicatorResponse.tStart = t  # local t and not account for scr refresh
        part2IndicatorResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part2IndicatorResponse, 'tStartRefresh')  # time at next scr refresh
        part2IndicatorResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(part2IndicatorResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(part2IndicatorResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if part2IndicatorResponse.status == STARTED and not waitOnFlip:
        theseKeys = part2IndicatorResponse.getKeys(keyList=['space'], waitRelease=False)
        _part2IndicatorResponse_allKeys.extend(theseKeys)
        if len(_part2IndicatorResponse_allKeys):
            part2IndicatorResponse.keys = _part2IndicatorResponse_allKeys[-1].name  # just the last key pressed
            part2IndicatorResponse.rt = _part2IndicatorResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part2"-------
for thisComponent in Part2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('part2Indicator.started', part2Indicator.tStartRefresh)
thisExp.addData('part2Indicator.stopped', part2Indicator.tStopRefresh)
# the Routine "Part2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('partQuestions2!.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "part2Questions"-------
    continueRoutine = True
    # update component parameters for each repeat
    keyboardIndicator.keys = []
    keyboardIndicator.rt = []
    _keyboardIndicator_allKeys = []
    part2Response.keys = []
    part2Response.rt = []
    _part2Response_allKeys = []
    part2Images.setImage(image)
    # keep track of which components have finished
    part2QuestionsComponents = [indicatorQuestionPart2, keyboardIndicator, part2Response, part2Images]
    for thisComponent in part2QuestionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    part2QuestionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "part2Questions"-------
    while continueRoutine:
        # get current time
        t = part2QuestionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=part2QuestionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *indicatorQuestionPart2* updates
        if indicatorQuestionPart2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            indicatorQuestionPart2.frameNStart = frameN  # exact frame index
            indicatorQuestionPart2.tStart = t  # local t and not account for scr refresh
            indicatorQuestionPart2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(indicatorQuestionPart2, 'tStartRefresh')  # time at next scr refresh
            indicatorQuestionPart2.setAutoDraw(True)
        
        # *keyboardIndicator* updates
        waitOnFlip = False
        if keyboardIndicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyboardIndicator.frameNStart = frameN  # exact frame index
            keyboardIndicator.tStart = t  # local t and not account for scr refresh
            keyboardIndicator.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyboardIndicator, 'tStartRefresh')  # time at next scr refresh
            keyboardIndicator.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyboardIndicator.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyboardIndicator.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyboardIndicator.status == STARTED and not waitOnFlip:
            theseKeys = keyboardIndicator.getKeys(keyList=['space'], waitRelease=False)
            _keyboardIndicator_allKeys.extend(theseKeys)
            if len(_keyboardIndicator_allKeys):
                keyboardIndicator.keys = _keyboardIndicator_allKeys[-1].name  # just the last key pressed
                keyboardIndicator.rt = _keyboardIndicator_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *part2Response* updates
        waitOnFlip = False
        if part2Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            part2Response.frameNStart = frameN  # exact frame index
            part2Response.tStart = t  # local t and not account for scr refresh
            part2Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(part2Response, 'tStartRefresh')  # time at next scr refresh
            part2Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(part2Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(part2Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if part2Response.status == STARTED and not waitOnFlip:
            theseKeys = part2Response.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _part2Response_allKeys.extend(theseKeys)
            if len(_part2Response_allKeys):
                part2Response.keys = [key.name for key in _part2Response_allKeys]  # storing all keys
                part2Response.rt = [key.rt for key in _part2Response_allKeys]
                # was this correct?
                if (part2Response.keys == str(corrAns2)) or (part2Response.keys == corrAns2):
                    part2Response.corr = 1
                else:
                    part2Response.corr = 0
        
        # *part2Images* updates
        if part2Images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            part2Images.frameNStart = frameN  # exact frame index
            part2Images.tStart = t  # local t and not account for scr refresh
            part2Images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(part2Images, 'tStartRefresh')  # time at next scr refresh
            part2Images.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in part2QuestionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "part2Questions"-------
    for thisComponent in part2QuestionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('indicatorQuestionPart2.started', indicatorQuestionPart2.tStartRefresh)
    trials_2.addData('indicatorQuestionPart2.stopped', indicatorQuestionPart2.tStopRefresh)
    # check responses
    if keyboardIndicator.keys in ['', [], None]:  # No response was made
        keyboardIndicator.keys = None
    trials_2.addData('keyboardIndicator.keys',keyboardIndicator.keys)
    if keyboardIndicator.keys != None:  # we had a response
        trials_2.addData('keyboardIndicator.rt', keyboardIndicator.rt)
    trials_2.addData('keyboardIndicator.started', keyboardIndicator.tStartRefresh)
    trials_2.addData('keyboardIndicator.stopped', keyboardIndicator.tStopRefresh)
    # check responses
    if part2Response.keys in ['', [], None]:  # No response was made
        part2Response.keys = None
        # was no response the correct answer?!
        if str(corrAns2).lower() == 'none':
           part2Response.corr = 1;  # correct non-response
        else:
           part2Response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('part2Response.keys',part2Response.keys)
    trials_2.addData('part2Response.corr', part2Response.corr)
    if part2Response.keys != None:  # we had a response
        trials_2.addData('part2Response.rt', part2Response.rt)
    trials_2.addData('part2Response.started', part2Response.tStartRefresh)
    trials_2.addData('part2Response.stopped', part2Response.tStopRefresh)
    trials_2.addData('part2Images.started', part2Images.tStartRefresh)
    trials_2.addData('part2Images.stopped', part2Images.tStopRefresh)
    # the Routine "part2Questions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
endResponse.keys = []
endResponse.rt = []
_endResponse_allKeys = []
# keep track of which components have finished
EndComponents = [EndScreen, endResponse]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndScreen* updates
    if EndScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndScreen.frameNStart = frameN  # exact frame index
        EndScreen.tStart = t  # local t and not account for scr refresh
        EndScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndScreen, 'tStartRefresh')  # time at next scr refresh
        EndScreen.setAutoDraw(True)
    
    # *endResponse* updates
    waitOnFlip = False
    if endResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResponse.frameNStart = frameN  # exact frame index
        endResponse.tStart = t  # local t and not account for scr refresh
        endResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResponse, 'tStartRefresh')  # time at next scr refresh
        endResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endResponse.status == STARTED and not waitOnFlip:
        theseKeys = endResponse.getKeys(keyList=None, waitRelease=False)
        _endResponse_allKeys.extend(theseKeys)
        if len(_endResponse_allKeys):
            endResponse.keys = _endResponse_allKeys[-1].name  # just the last key pressed
            endResponse.rt = _endResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndScreen.started', EndScreen.tStartRefresh)
thisExp.addData('EndScreen.stopped', EndScreen.tStopRefresh)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
