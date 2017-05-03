from django.shortcuts import render
def post_list(request):
    return render(request, 'details_entry/post_list.html', {})
