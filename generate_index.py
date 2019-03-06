#!/usr/bin/env python
mw=3000
mh=3000
s="""<!DOCTYPE html>
<html lang="en">
<head>
  <title>CSS Screen Meter</title>
  <style>
    body { 
      background-color: skyblue;
      font-size:5vmin;
      font-family:monospace;
    }
    div.x {
      width:50vw;
      text-align:center;
      position:absolute;
      top:50%;
      left:50%;
      margin-top:-5vmin;
      margin-left:-25vw;
    }
    span {display:none};"""
for i in range(mw):
  s+="""
    @media screen and (min-width: """+str(i+1)+"""px) and (max-width: """+str(i+1)+"""px) {
      span#w"""+str(i+1)+""" {display:inline-block;}
    }"""
for i in range(mh):
  s+="""
    @media screen and (min-height: """+str(i+1)+"""px) and (max-height: """+str(i+1)+"""px) {
      span#h"""+str(i+1)+""" {display:inline-block;}
    }"""
s+="""
  </style>
</head>
<body>
  <div class="x">"""
for i in range(mw):
  s+="""
    <span id="w"""+str(i+1)+"""">"""+str(i+1)+"""</span>"""
s+="""
    X """
for i in range(mh):
  s+="""
    <span id="h"""+str(i+1)+"""">"""+str(i+1)+"""</span>"""
s+="""
</div></body>
</html>
"""

print s;
