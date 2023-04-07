from django.shortcuts import render


def IndexView(request):
    return render(request, template_name='index.html')


# Edit Index //TODO
def EditIndex(request):
    return render(request, template_name='edit_index.html')