# music_catalogue - An MP3 audio file cataloging program
<table>
    <caption>Creates a database holding information extracted from metadata(ID3 tags).</caption>
    <thead>
        <th>pkid</th>
        <th>title</th>
        <th>artist</th>
        <th>album</th>
        <th>bitrate</th>
        <th>genre</th>
        <th>playtime</th>
        <th>track no.</th>
        <th>year</th>
        <th>filesize</th>
        <th>path</th>
        <th>filename</th>
    </thead>
    <tbody>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
    </tbody>
</table>


DATA
====
Music track information stored in the [Database](music_catalogue.db)

Usage
=====
Run:
<pre>
$ <kbd>python3 music_catalogue.py &lt;foldername&gt;</kbd>
</pre>
<p>Where &lt;foldername&gt; is the path to MP3 files</p> 

Dependencies
============
Requires:
    1. Database Engine

    SQLite3 - A small database engine that does not require separate database server

OnLinuxRun:
<pre>
$ <kbd>sudo apt-get install sqlite3</kbd>
</pre>

    2. python3 modules 
    apsw - Another python SQLite wrapper. A quick way to communicate with SQLite.
    mutagen - all purpose multimedia tagging library.
					
Install - OnLinuxRun:
<pre>
$ <kbd>sudo pip3 install apsw</kbd>
</pre>
<pre>
$ <kbd>sudo pip3 install mutagen</kbd>
</pre>

Attribution
===========
Originally Written By:
Greg D. Walters - RainyDay Solutions, LLC


Full circle magazine Issue #35 - Program In Python part 9
[full circle magazine](www.fullcirclemagazine.org)

License - Creative Commons Attribution-Share Alike 3.0 Unported license
==========================================================================
More on the licence, 

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-wilih:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.

