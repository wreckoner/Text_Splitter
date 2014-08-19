'''
Created on Aug 13, 2014
@author: Dibyendu
Contains functions which handles errors.
'''

def Python_IO_Error_Handler(errno):
    if errno == 13:
        message = 'Select Output Directory!!!'
    elif errno == 22:
        message = 'Select a File!!!'
    else:
        message = 'Unknown Error. Report Bug!!!'
    return message

def Python_Value_Error_Handler(error):
    if str(error[0]).find('invalid literal for int() with base 10:') == 0:
        message = 'Enter proper number of lines!!!'
    else:
        message = 'Unknown Error. Report Bug!!!'
    return message
