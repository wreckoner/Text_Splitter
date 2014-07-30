'''
Created on Feb 13, 2014

@author: Dibyendu
'''

def main(filename, num):
    i,c=1,1
    print 'creating : '+str(filename[:-4]+'_part'+str(c)+filename[-4:])
    with open(filename, 'r') as fileobject:
        for line in fileobject:
            print line.strip()
            x=open(str(filename[:-4]+'_part'+str(c)+filename[-4:]),'a')
            x.write(line)
            x.close
            i = i+1
            if i > num:
                i,c=1,c+1
                print 'creating : '+str(filename[:-4]+'_part'+str(c)+filename[-4:])
        print 'total number of parts created : ',c
        print 'total number of lines read : ',i+c*num
    pass



if __name__ == '__main__':
    print '====================================================Text Splitter==========================================================='
    print 'This program will split any text file into smaller parts. It takes the file name and number of lines per part as parameters.'
    print 'Will be generated in original file directory'
    print '============================================================================================================================'
    try:
        filename = raw_input('Enter file name : ')
        open(filename,'r')
        num = raw_input('Enter number of lines per file : ')
        int(num)
    except Exception, e:
        print str(e)+'\nRestart Program.'
        exit()
    main(filename, int(num))