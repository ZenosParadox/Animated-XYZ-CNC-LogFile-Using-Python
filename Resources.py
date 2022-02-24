import sys, re, os, pandas as pd, numpy as np

def wfile(fileName, text):
# OVERWRITE TO FILE - DELETE WHAT WAS THERE BEFORE
        f = open(fileName, 'w')
        f.write(text)
        f.close()
        return

#APPEND TO EXISTING FILE DATA
def afile(fileName, text):
        f = open(fileName, 'a')
        f.write('\n' + text)
        f.close()
        return
#READ
def readText(fileName):
    f = open(fileName)
    t = f.read()
    f.close
    return t

def filesInWorkFolder(folder, fileType_withoutDot):
    #Regular Expression
    file_regex = re.compile(r'.*\.' + fileType_withoutDot, re.IGNORECASE) 
    #dot star means find everything
    file_list = []

    #folders, subfolders, filenames
    for _, _, filenames in os.walk(folder):
        for file in filenames:
            file_search = file_regex.findall(file)
            if file_search:                           #if file_search is not empty
                file_list.append(file)
    return file_list

def readLogFile(logFileAddress):
    logFile = readText(logFileAddress).split()
    Layers = list()
    Passes = list()
    X = list() 
    Y = list()
    Z = list()
    
    for i,v in enumerate(logFile):
        #ORIGINAL
        if v == "L":
            X.append(float(logFile[i+5]))
            Y.append(float(logFile[i+6]))
            Z.append(float(logFile[i+7]))
            Layers.append(float(logFile[i+1]))
            Passes.append(float(logFile[i+3][1:]))
    return X,Y,Z,Layers,Passes

def read_LogFile(logFileAddress):
	column_names = ['Time_Stamp', 'Label', 
					'X_Cmd_High', 'X_Cmd_Low', 'X_Act_High', 'X_Act_Low', 'X_Telem_High', 'X_Telem_Low',
					'Y_Cmd_High', 'Y_Cmd_Low', 'Y_Act_High', 'Y_Act_Low', 'Y_Telem_High', 'Y_Telem_Low',
					'Z_Cmd_High', 'Z_Cmd_Low', 'Z_Act_High', 'Z_Act_Low', 'Z_Telem_High', 'Z_Telem_Low']
	logFile = pd.read_csv(logFileAddress, skiprows=5, names=column_names, index_col=False)
	return logFile


def XYZ_Telem_LogFile(logFileAddress):
	logFile = read_LogFile(logFileAddress)
	X = np.array(logFile['X_Telem_High'])
	Y = np.array(logFile['Y_Telem_High'])
	Z = np.array(logFile['Z_Telem_High'])
	return X, Y, Z

def XYZ_LogFile_Read(logFileAddress):
	column_names = ['X', 'Y', 'Z']
	logfile = pd.read_csv(logFileAddress, names=column_names, index_col=False, skiprows=1)
	X = np.array(logfile['X'])
	Y = np.array(logfile['Y'])
	Z = np.array(logfile['Z'])
	return X, Y, Z