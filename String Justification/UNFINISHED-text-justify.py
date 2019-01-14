# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:18:41 2019

@author: CPMC
"""

import re
text = '''Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.'''

text = text.replace('\n',' ')
text = text.replace(' ', '-')

pattern = re.compile(r"-+" )
matches = pattern.findall(text)
for match in matches:
    text = text.replace(match, ' ')

pattern_word = re.compile(r"\b\w+\W*")
matches_w = pattern_word.findall(text)
words=[word for word in matches_w]
words_stats=[(word,len(word)) for word in matches_w]



#Forth Try --------------------------------------------------



def justify(text, width):
    words = text.split()
    result = ""
    x = len(text)
    while x > 0:
        line = []   
        let_counter = 0
        
#making the primary list of words in a line-------------------
        while let_counter < width:
            if len(words)>0:
                line.append(words[0]+" ")
                words.remove(words[0])
                let_counter += len(line[-1])
            
                
        if let_counter > width:
            words.insert(0,line[-1])
            let_counter -= len(line[-1])
            line.remove(line[-1])
            
            print(let_counter)
            print(line)
            
#ok---------ok---------ok---------ok---------ok---------ok---------ok           

            
#ading space between words if line's width is less than width required-------
            if let_counter < width:
                for word in line[:-1]:
                    while let_counter < width:
                        word = word + " "
                        let_counter += 1
                result = result + ''.join(line)+"\n"
                x -= width
                
#---------------------------------------------------------------------------ok
            
            elif let_counter == width:
                line.append("\n")
                result = result + ''.join(line)
                x -= width
        else:
            
                
#    return result

                        





#Third Try --------------------------------------------------



def justify(text, width):
    words = text.split()
    result = ""
    while len(text) > 0:
        line = []
        count = 0
        sum_line = sum([len(word) for word in line])
        print(sum_line)
        for word in words:
#            while sum_line < width:
                word += " "
                print(word)
                line.append(word)
                sum_line = sum([len(word) for word in line])
                print(line)
            if sum_line < width:
                for word in line:
                    while sum(line) < width:
                        word = word + " "
            elif sum_line == width:
                line.append("\n")
                text = text[width+1:]
                result = result + line[0]
    return result





#second try ------------------------------------------------
line = ""
for word in words_stats:
    while len(line) <= 30:
        line = line + word[0]
        if len(line) == 30:
            line = line[:-1]+"\n"
            text = text[31:]
        elif len(line) < 30:
            while len(line) < 30:
                for word in line.split():
                    
            
# First Try -------------------------------------------------
l = []
space = " "
line = ""
module = 30
count = 1
while len(line)<module:
    for word in words:
        print(word)
        line = line+word
        print(line)
    if len(line) == module:
        l.append(line+"\n")
    else:
        line = line+word+space
        
        
#    elif len(line) < module:
#        for 
#        
#    elif len(line) > count*module:
#        count += 1
#        line = line+"\n"
    



