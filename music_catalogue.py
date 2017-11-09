#!/usr/bin/env python3
'''An MP3 audio file cataloging program. 

Creates a database holding information extracted from metadata(ID3 tags).
    + Title
    + Artist
    + Album
    + Bitrate
    + Genre
    + Playtime
    + Track No.
    + Year
    + Filesize
    + Path (Location)
    + Filename
'''
__AUTHOR__='Greg Walters'
__CONTRIBUTORS__ = 'Arthur Ngondo'

from mutagen.mp3 import MP3
import os
from os.path import join, getsize, exists
import sys
import apsw

def init_database():
    '''If it doesn\'t exist, creates database music_catalogue.db 
    Create the connection and cursor to database  
    '''
    pass

def make_db_table():
    '''If it doesn\'t exist, creates database table - mp3
    Otherwise, ignore (\'IF NOT EXIST\' clause).  
    '''
    pass

def seconds_to_hr_min_secs_format(time_in_secs):
    '''Takes time_in_secs, the total time in seconds for each mp3 file.   
    Returns a string formatted H:mm:ss
    '''
    pass

def walk_the_path(music_path):
    '''Takes music_path, the path(location) of mp3 files and traverses the 
    directories,extracting the relevant info from ID3 tags and writes it 
    to the dadabase - music_catalogue.db 
    '''
    pass

def error_msg(message):
    '''Takes argument message custom error message on how to use the script.
    Displays a string with an elaborate error message.'''
    
    print >> sys.stderr, str(message) # Redirect output to stderr stream

def usage():
    '''Defines the proper usage error message.
    Display error message if user attempts to run without all required 
    parameters, then exit.  
    '''
    message = (
        '===================================================================\n'
        'music_catalogue\n' 
        '\tFinds all *.mp3 files in a given folder (and sub-folders),\n'
        '\tRead the ID3 tags, write that info to a SQLite database.\n\n'
        'Usage:\n'
        '\t{0} <foldername>\n'
        '\t Where <foldername> is the path to mp3 files.\n\n'
        '===================================================================\n'
        ).format(sys.argv[0])   # Include app name

    error_msg(message) # Output the err-msg
    sys.exit(1) # Exit the app

if __name__ == '__main__':
    init_database()


