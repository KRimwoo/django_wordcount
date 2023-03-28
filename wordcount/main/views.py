from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['text']
    text_list = text.split()
    text_dict = {}
    num_words = 0
    for word in text_list:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    words = sorted(text_dict.items(), key=lambda x:x[1], reverse=True)
    context = {
        'text_list' : text_list,
        'words' : words
    }
    return render(request, 'result.html', context)