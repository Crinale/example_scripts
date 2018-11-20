def timeConversion(s):
    #
    # Write your code here.
    #
    hh = s[:2]
    mm = s[3:5]
    ss = s[6:8]
    ampm = s[-2:]
    
    if ampm == "PM":
        if hh != "12":
            newhour = 12 + int(hh)
        else:
            newhour = hh
        print (newhour,":",mm,":",ss)
        return "%s:%s:%s"%(newhour,mm,ss)
    
    
    
    if  ampm == "AM":
        if hh == "12":
            hh = "00"
        print (hh,":",mm,":",ss)
    return "%s:%s:%s"%(hh,mm,ss)