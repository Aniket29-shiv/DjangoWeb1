# # #  I have created this file - Aniket
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def nav1(request):
    return HttpResponse('''<center><h1>Welcome to Navigation bar</h1><table border=20>
        <tr><td>Link</td><td>Description</td></tr>
        <tr><td><a href="google.com">Google</a></td><td>This is search Engine</td></tr>
        <tr><td><a href="facebook.com">FB</a></td><td>This is social network</td></tr>
        <tr><td><a href="youtube.com">Uthub</a></td><td>This is video platform</td></tr>
        
        </table></center>''')


def analyze(request):
    djtext = request.POST.get('text', 'default')


    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    removespace = request.POST.get('removespace', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Lower case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremove=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char.lower()
        params = {'purpose': 'Newline Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (removespace == "on"):
        analyzed=""
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        # return HttpResponse("Remove space <a href='/'>Back</a>")
    if (removepunc!="on" and fullcaps!="on" and newlineremove!="on" and removespace!="on" ):
        return HttpResponse("Plz select any operation!!")
        
    # else:
    #     return HttpResponse("Error")
    return render(request, 'analyze.html', params)





#
