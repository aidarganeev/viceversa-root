from django.shortcuts import render
import re

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	word_count = len(re.findall(r'\w+', user_text))
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'wordcount':word_count})



