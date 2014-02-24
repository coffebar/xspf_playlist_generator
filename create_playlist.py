#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Odarchenko N.D.'

# xspf playlist generator from online audio book sites

# first file in playlist (url from book site)
first_file = 'http://okgift.ru/audio/1/Phantastika/Kamenisty/9-Korshunov/2/1.mp3'
# how many files to save
files_count = 54
# out file to save playlist
out_playlist = 'book.xspf'


xml_code = """<?xml version="1.0" encoding="UTF-8"?>
<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">
    <title>Playlist</title>
    <trackList>
"""

for i in range(1, files_count):
    xml_code += '    <track><location>' + first_file.replace('/1.mp3', '/' + str(i) + '.mp3')
    xml_code += '</location><extension application="http://www.videolan.org/vlc/playlist/0">'
    xml_code += '<vlc:id>' + str(i - 1) + '</vlc:id></extension></track>\r\n'
xml_code += '    </trackList>\r\n    <extension application="http://www.videolan.org/vlc/playlist/0">\r\n'
for i in range(0, files_count - 1):
    xml_code += '        <vlc:item tid="' + str(i) + '"/>\r\n'
xml_code += '    </extension>\r\n</playlist>'

with open(out_playlist, 'w') as handle:
    handle.write(xml_code)
