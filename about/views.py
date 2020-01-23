from django.http import JsonResponse

def about(req):
    return JsonResponse({
    "about":"this page is about lurum ipsum lurum ipsum"
    })
