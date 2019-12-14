import stepic
from PIL import Image
#To decode message
def decode(image):
    o=Image.open(image)
    d=stepic.decode(o)
    return d
#To encode message
def encode(a,b,c):
    b=b.encode("ascii")
    open_=Image.open(a)
    modify= stepic.encode(open_,b)
    modify.save(c+".png")
while True:
    print('1)Encode\n2)Decode\n3)Exit')
    i=int(input('Enter corresponding number to carry out an action: '))
    if i==1:
        name=input('Enter the name of the image in which you want to hide a message (Please Include Extension):')
        text=input('Enter the text which you want to hide in the image:')
        output=input('Enter the name of the new file which will be created (no extension):')
        encode(name,text,output)
        print('A copy of the image has been created which contains your message.')
    elif i==2:
        k=input("Enter the name of the image you wish to decode (include extension):")
        print('The message:\'',decode(k),'\'has been found')
    elif i==3:
        break
    