occurence = {}

ciphertext = 'UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSUPQUZWYMXVZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUMTMOHMQ'

for i in ciphertext:
    if i in occurence:
        occurence[i] += 1
    else:
        occurence[i] = 1
    
for key in occurence:
    occurence[key] /= 120
    occurence[key] *= 100

print('Count for each alphabet: ',occurence)
print('Original ciphertext',ciphertext)
        
new = ciphertext.replace('Z','t').replace('S','a').replace('V','d').replace('W','h').replace('U','i').replace('Q','w').replace('O','s').replace('H','c').replace('X','l').replace('M','o').replace('P','e').replace('G','y').replace('P','e').replace('E','r').replace('F','v').replace('E','r').replace('D','n').replace('B','f').replace('T','m').replace('A','b').replace('I','u').replace('Y','p')

print('\n\n',new)