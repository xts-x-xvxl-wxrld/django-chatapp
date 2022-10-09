from django.shortcuts import render

def frontpage(request):
    return render(request, ('Core/frontpage.html'))

#comment1