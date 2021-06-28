



# def ind(request):
#     ##prahlad={'name':'lokesh','team':'punjab'}
#     return render(request,'insert.html')
#    return HttpResponse("home")
# def rock(request):
#     #get the text
#     # djtext=request.GET.get('text', 'default')
#     removepunc=request.GET.get('removepunc','off')
#     uppercaset=request.GET.get('upppercase','off')# request file first take parameter of html file name that' who get the value of type  of html heading and second parameter is you can write default or off
#     print(removepunc)
#     print(djtext)# analyze the text
#     analyze=""
#     if removepunc=='on':
#
#
#         punc='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
#         for i in djtext:
#             if i not in punc:
#                 analyze=analyze+i
#         params = {'parameters': 'remove punctuation', 'analyzed_text': analyze}
#         return render(request, 'analyze.html', params)
#     if uppercaset=='on':
#         analyzey=""
#         for i in djtext:
#             analyze=analyze+i.upper()
#         params = {'parameters': 'remove punctuation', 'analyzed_text': analyzey}
#         return render(request, 'analyze.html', params)
#
#
#

#
# def spaceremover(request):
#    return HttpResponse("this is this  prahlad <a href='/'>back </a>")
#################################################work on videos webcam########################################################
# def webcam(request):
#
#     webcamera=request.GET.get('videos',"off")
#     if webcamera=='on':
#         cap = cv2.VideoCapture(0)  # 0 take default web cam
#         cap.set(3,640)
#         cap.set(4,480)
#         cap.set(10,100)#3rd of set function is for setting brightness
#
#         while True:
#            success,img=cap.read()#read take two argument first you take anything it giveen the value in boolean 0,1 and second store the data and readable file
#            cv2.imshow("videos",img)
#            if cv2.waitKey(1)==ord("q"):# for if we want to terminate the video then i should put the q
#                 break
#
#     return render(request, 'cam.html')
# def webcam(request):
#     return HttpResponse("i am prahlad kumar i am hard working boy of my college ")
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')