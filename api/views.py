import io

from django.http import JsonResponse

from .models import Post, Category
from .serializers import PostSerializer, PostIntroSerializer, CategorySerializer


def post_list(request):
    posts = Post.objects.all()
    serialized_data = PostIntroSerializer(posts, many=True)
    return JsonResponse(serialized_data.data, safe=False)


def post_detail(request, pk):
    post = Post.objects.get(slug=pk)
    serialized_data = PostSerializer(post)
    return JsonResponse(serialized_data.data)


def post_search(request, query):
    posts = Post.objects.filter(tags__icontains=query)
    serialized_data = PostIntroSerializer(posts, many=True)
    return JsonResponse(serialized_data.data, safe=False)


def category_list(request):
    categories = Category.objects.all()
    serialized_data = CategorySerializer(categories, many=True)
    return JsonResponse(serialized_data.data, safe=False)