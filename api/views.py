from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from notebook.TextSummary import extractive_summarizer

# Create your views here.

@api_view(['GET', 'POST'])
def getRoutes(request):
    if request.method == 'POST':
        text = request.data.get('text', '')
        text_length = len(text)
        if text_length < 100:
            num_sentences = 3
        elif text_length > 100 and text_length < 300:
            num_sentences = 4
        elif text_length > 300 and text_length < 500:
            num_sentences = 5
        elif text_length > 500 and text_length < 700:
            num_sentences = 6
        elif text_length > 700 and text_length < 900:
            num_sentences = 7
        elif text_length > 900 and text_length < 1100:
            num_sentences = 8
        elif text_length > 1100 and text_length < 1300:
            num_sentences = 9
        elif text_length > 1300:
            num_sentences = 10  
        print(f"The text length is: {text_length}")

        summary = extractive_summarizer(text, num_sentences)
        return Response({'summary': summary})