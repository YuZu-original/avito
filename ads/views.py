import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, ListView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Category, Selection
from ads.permissions import AdEditPermission, SelectionEditPermission
from ads.serializers import AdDetailSerializer, AdSerializer, SelectionSerializer, SelectionDetailSerializer, \
    SelectionListSerializer, AdCreateSerializer, CategoryCreateSerializer
from avito import settings
from users.models import User


def index(request):
    return JsonResponse({
        "status": "ok"
    })


class CategoryView(ListView):
    models = Category
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("name")

        response = []
        for category in self.object_list:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        self.object.name = category_data["name"]

        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class AdView(ListView):
    models = Ad
    queryset = Ad.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        if categories := request.GET.getlist("cat", None):
            self.object_list = self.object_list.filter(category_id__in=categories)

        if text := request.GET.get("text"):
            self.object_list = self.object_list.filter(name__icontains=text)

        if location := request.GET.get("location"):
            self.object_list = self.object_list.filter(author__locations__name__icontains=location)

        if price_from := request.GET.get("price_from"):
            self.object_list = self.object_list.filter(price__gte=price_from)

        if price_to := request.GET.get("price_to"):
            self.object_list = self.object_list.filter(price__lte=price_to)

        self.object_list = self.object_list.select_related('author').order_by("-price")
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "author": ad.author.first_name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "image": ad.image.url if ad.image else None,
            })

        response = {
            "items": ads,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }

        return JsonResponse(response, safe=False)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated, AdEditPermission]


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES.get("image", None)
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None,
        })


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdEditPermission]


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionRetrieveView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]
