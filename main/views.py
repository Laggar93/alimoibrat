from django.shortcuts import render


def main_page_view(request):

    content = {
    }

    return render(request, 'index.html', content)