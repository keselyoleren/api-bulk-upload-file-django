from django.shortcuts import render
from gallery.models import Gallery, BulkFile
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from gallery.serialize import BullFielSerialize
from io import BytesIO
from zipfile import ZipFile
from PIL import Image
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class BulkUploadApiView(generics.CreateAPIView):
    serializer_class = BullFielSerialize
    queryset = BulkFile.objects.all()

    def _generate_file(self, instance):
        with ZipFile(instance.file.file, 'r') as zipObj:
            listOfFilename = zipObj.namelist():

            for filename in listOfFilename:
                # read image file
                file = zipObj.read(filename)
                image = Image.open(BytesIO(file))
                image.load()
                image = Image.open(BytesIO(file))
                weigth, height = image.size

                # save content zip to db
                file_path = os.path.join(os.path.dirname(BASE_DIR), 'media/') + filename
                image.save(file_path, format="JPEG")

                galery = Gallery()
                galery.image = filename
                galery.name = filename
                galery.save()

    # delete zip file after extract
    def _re_assign_files(self, instace):
        instace.file.delete()  # deletes the uploaded file
        instace.save()  # saving the model instance
            

    def post(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data)
        serialize.is_valid(True)
        instance = serialize.save()

        extract = self._generate_file(instance)
        self._re_assign_files(instance)
        return Response(serialize.data, status=HTTP_200_OK)

        
        

