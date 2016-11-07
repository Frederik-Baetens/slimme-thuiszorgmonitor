lijst=[4095,4095,255,1000,1500,100,0,0,0,4095,4095,255]
lijst2=[]
for i in range(len(lijst)):
    if i%3==0 or i%3==1:
        if lijst[i]<16:
            lijst2.append('0x0')
            lijst2.append('0x0')
            lijst2.append(hex(lijst[i]))
        elif lijst[i]<256:
            lijst2.append('0x0')
            lijst2.append(hex(lijst[i]))
        else:
            lijst2.append(hex(lijst[i]))
    else:
        if lijst[i]<16:
            lijst2.append('0x0')
            lijst2.append(hex(lijst[i]))
        else:
            lijst2.append(hex(lijst[i]))
lijst3=[

