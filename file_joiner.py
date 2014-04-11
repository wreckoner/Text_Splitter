#!\usr\bin\py env
#Author : Dibyendu Das
#Method to join several files into one.

def joinFile(fileIn, fileOut):                              #pass list of input files and output file name
    i,j,a = 0,0,[]
    with open(fileOut, 'w') as fileOutObj:                  #load output file
        for singleFile in fileIn:                           #iterates over input file list
            with open(singleFile, 'r') as singleFileObj:    #loads a file from input file list
                for line in singleFileObj:                  #iterate over lines in loaded input file
                    fileOutObj.write(line)                  #write the line to output file
                    ++i
                    ++j
                a.append(i)
                print 'Number of lines in ',singleFile,' : ',i
                i = 0
    print 'Total number of lines joined : ',j
    print 'Join complete. ',fileOut,' saved.'



if __name__ == '__main__':
    filein = ['NewBedford.csv','NewBedford2.csv','NewBedford3.csv','NewBedford4.csv','NewBedford5.csv','NewBedford6.csv']
    fileout = 'NewBedford_joined.csv'
    try:
        joinFile(filein, fileout)
    except Exception, e:
        print 'Error ',str(e)
    raw_input('Program execution complete. Press enter to exit.')
