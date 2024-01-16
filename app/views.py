import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.models import Blog
from rest_framework.response import Response


# Create your views here.

def index(request):
    return render(request, 'index.html')


# add blog post
@csrf_exempt
def add_blog(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            title = data['title']
            body = data['body']
            image_url = data['image_url']
            print(title, body, image_url)
            blog = Blog(title=title, body=body, image_url=image_url)
            blog.save()
            return JsonResponse({'message': 'Blog post added successfully'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=400)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)


def get_blog_by_id(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            blog_id = data['blog_id']
            blog = Blog.objects.get(id=blog_id)
            return JsonResponse({'message': 'Blog post fetched successfully',
                                 'data': {'title': blog.title, 'body': blog.body, 'image_url': blog.image_url}},
                                status=200)
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=400)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)


