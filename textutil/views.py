# work
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get tex 
    djtext = request.POST.get('text','default')
    # check ckeckbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    puncuation = '''[]{}-!"#$%&'()*+,./:;<=>?@`|\\^_'''
    # check which check box is on

    if (removepunc == 'on'):
        analyzed = ''
        for char in djtext:
            if char not in puncuation:
                analyzed = analyzed + char

        params = {'purpose' : 'Remove Puncuation' , 'analyzed_text' : analyzed}
        djtext = analyzed
        
    if(fullcaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
            
        params = {'purpose' : 'Change to uppercase' , 'analyzed_text' : analyzed}
        djtext = analyzed
    
    if(spaceremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != ' ':
                analyzed = analyzed + char
            else:
                pass
        params = {'purpose' : 'Remove spaces' , 'analyzed_text' : analyzed}
        djtext = analyzed
        
    if(extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose' : 'Remove all the extra spaces' , 'analyzed_text' : analyzed}
        djtext = analyzed
        
    if(charcount == 'on'):
        analyzed = ''
        length = len(djtext)
        params = {'purpose' : 'count characters' , 'analyzed_text' :length}
    
    return render(request,'analyze.html',params)
    