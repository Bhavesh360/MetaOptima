from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from time import time

from .forms import NameForm

def removedups(str):
	myList = []
	for letters in str:
		if letters not in myList:
			myList.append(letters)
	str = "".join(myList)
	return str

def rev(str):
    x=str[::-1]
    x = removedups(x)
    return x
    #could also use the logic below:
	# newstring = ""
	# x = len(str)
	# while x:
	# 	x = x-1
	# 	newstring += str[x]
	# return newstring


def get_name(request):
    request.start_time = time()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data.get('name')
            inputstring = form.cleaned_data.get('inputstring')
            executiontime = 0

            map = {
                'name': name,
                'inputstring': inputstring,
                'exececutiontime': executiontime
            }
            template = loader.get_template('response.html')
            map['inputstring']=rev(map['inputstring'])
            # map['exececutiontime'] = float(((time() - request.start_time))/60) --- could have done this to get in mins.
                                                                                        # But the value is too small so its better to represent in secs.
            map['exececutiontime'] = float(((time() - request.start_time)))
            map['exececutiontime'] = repr(map['exececutiontime']) + ' seconds'
            # returing the template
            return HttpResponse(template.render(map, request))
            # return HttpResponseRedirect('/check/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def response(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    return render(request, "response.html")