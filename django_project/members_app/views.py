from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import My_Forms


def session_data(request):
	if request.method == "POST":
		form = My_Forms(request.POST)
		if form.is_valid():
			request.session['user_input'] = form.cleaned_data
			return redirect('display_page')
	else:
		form = My_Forms()

	return render(request, 'input_page.html', {"form": form})


def display_view(request):
	user_input = request.session.get("user_input", {})
	return render(request, 'display_page.html', {'user_input':user_input})


def is_authorized_user(request):
	user_input = request.session.get("user_input", {})
	if user_input['name'] != '':
		return render(request, 'is_authorized_user.html', {'user_input': user_input})
	else:
		return HttpResponse("Hello, guest!")