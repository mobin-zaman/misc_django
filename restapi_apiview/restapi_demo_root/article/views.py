from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializer import ArticleSerializer

# Create your views here.

class ArticleView(APIView):
    def get(self, request):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response({"articles":serializer.data})
    def post(self, request):
        article=request.data.get('article')

        


