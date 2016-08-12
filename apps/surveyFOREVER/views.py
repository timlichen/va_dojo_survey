from django.shortcuts import render, redirect
import cgi

# Create your views here.


# QueryDict: {u'favbev': [u"Manny's Pale Ale"], u'favLang': [u'english', u'pig-latin', u'esperanto', u'parsley-tounge'], u'csrfmiddlewaretoken': [u'5NYP2STrmvV0xoheutAmHgbJG4zhBKmA'], u'name': [u'Tim Chen']}>

def index(request):
    print "Hi python people! Slither your way to success!"
    return render(request, 'surveyFOREVER/index.html')

def create(request):
    favLangArr = request.POST.getlist('favLang')
    stuff = {
        "langArr": favLangArr,
        "beverage": request.POST['favbev'],
        "name": request.POST['name']
    }
    request.session['stuff'] = stuff
    return redirect('/results')

def showmestuff(request):
    return render(request, 'surveyFOREVER/results.html')
