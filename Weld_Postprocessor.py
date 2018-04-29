#!/usr/bin/env python

"""NodeShift_Manual.py: Translates nodes in Abaqus *.inp file"""

__author__ = "Samiel Tesfayohannes"
__version__ = "0.0"
__email__ = "samiel.tesfayohannes@student.manchester.ac.uk"
__status__ = "Demo"

#############################################
import os
import sys

fname='C:\Users\Sami\Documents\Arc welding project 2017\Demo_code_short' #name of .txt file to be processed
fO= (fname + '_new') 	#name of new processed .txt file 
tspeed = 'VEL.CP=0.167'
wspeed = 'VEL.CP=0.003'

print 'Processing %s \nOutputting to %s'%(fname,fO)

#delete old output files if they exist
try:
    os.remove(fO+'.txt')
except OSError:
    pass



with open(fO+'.txt','a+') as f: #create and open new .txt file
	with open(fname+'.txt','r') as fid: #open .txt file to be processed
		fidl =fid.readlines() #read file line by line
		del fidl[0:10] #deleting the file header text from SPRUTCAM

		f.write(';FOLD INI\n;FOLD EXTERNAL DECLARATIONS;%{PE}%MKUKATPBASIS,%CEXT,%VCOMMON,%P\n;FOLD ARCTECHDIGITAL EXT\nEXT A20 (INT :IN,WELD_ST :IN,WELD_FI :IN,INT :IN )\n;ENDFOLD (ARCTECHDIGITAL EXT)\n;FOLD BASISTECH EXT;%{PE}%MKUKATPBASIS,%CEXT,%VEXT,%P\nEXT BAS (BAS_COMMAND :IN,REAL :IN )\nDECL INT SUCCESS\n;ENDFOLD (BASISTECH EXT)\n;FOLD USER EXT;%{E}%MKUKATPUSER,%CEXT,%VEXT,%P\nDECL WELD_ST W_START\nDECL WELD_FI W_END\n;ENDFOLD (USER EXT)\n;ENDFOLD (EXTERNAL DECLARATIONS)\n;FOLD BASISTECH INI\nGLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )\nINTERRUPT ON 3\nBAS (#INITMOV,0 )\n;ENDFOLD (BASISTECH INI)\n;FOLD ARCHTECHDIGITAL INI\nIF ARC20==TRUE THEN\n A20 (ARC_INI)\n INTERRUPT DECL 6 WHEN $CYCFLAG[3]==FALSE DO A20(TECH_STOP2)\n ENDIF\n;ENDFOLD (ARCHTECHDIGITAL INI)\n;FOLD USER INI\n;ENDFOLD (USER INI)\n;ENDFOLD (INI)\nHALT\n;FOLD PULSE 652 \'ERROR RESET\' State=TRUE CONT Time=0.1 sec;%{PE}%R\n5.5.33,%MKUKATPBASIS,%COUT,%VPULSE,%P 2:652, 3:ERROR RESET, 5:TRUE, 6:CONTINUE, 8:0.1\nCONTINUE\nPULSE($OUT[652], TRUE,0.1)\n;ENDFOLD\n;FOLD OUT 646 \'MASTER 1\' State=TRUE ;%{PE}%R 5.5.33,%MKUKATPBASIS,%COUT,%VOUTX,%P\n2:646, 3:MASTER 1, 5:TRUE, 6:\n$OUT[646]=TRUE\n;ENDFOLD\n;FOLD OUT 647 \'MASTER 2\'State=FALSE ;%{PE}%R 5.5.33,%MKUKATPBASIS,%COUT,%VOUTX,%P\n2:647, 3:MASTER 2, 5:FALSE, 6:\n$OUT[647]=FALSE\n;ENDFOLD\n') #insert header to initialise the robot and weld head
		#line above adds the neccesarry header to the .txt file
		for line in fidl:
				if tspeed in line:   #put in the value for the traverse speed here
					f.write('A20(ARC_OFF)\n') #turn weld torch off before changing to the traverse speed
				if wspeed in line:   #put in the value for the working speed here
					f.write('A20(ARC_ON,W_START,MDEFAULT,1)\nA20(ARC_OFF_V,ADEFAULT,W_END,1)\n') #turn weld torch on before changing to working speed
				if line == fidl[-1]:
					f.write('A20(ARC_OFF)\nEND')#turn off weld torch at end of the .txt file
				else: #just write the line from the original file
					f.write('%s'%line)
	fid.close()
f.close()
