from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status as rest_status


class JSONResponse(HttpResponse):
    def __init__(self, data=None, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json; charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)


class Play2LiveGenericView(GenericAPIView):
    authentication_classes = (BasicAuthentication,)
    lookup_field = 'id'

    def perform_create(self, serializer, **kwargs):
        return serializer.save(**kwargs)

    def create_raw(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer, **kwargs)

        return serializer.data

    def create(self, request, *args, **kwargs):
        data = self.create_raw(request, *args, **kwargs)
        return JSONResponse(data, status=rest_status.HTTP_201_CREATED)

    def perform_update(self, serializer, **kwargs):
        serializer.save(**kwargs)

    def update_raw(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer, **kwargs)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return data

    def update(self, request, *args, **kwargs):
        data = self.update_raw(request, *args, **kwargs)
        return JSONResponse(data)

    def list(self, request, *args, **kwargs):
        data = self.list_raw(request, *args, **kwargs)
        return JSONResponse(data)

    def list_raw(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return serializer.data

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JSONResponse(status=rest_status.HTTP_204_NO_CONTENT)
