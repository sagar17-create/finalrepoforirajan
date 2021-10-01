from django.shortcuts import render
#from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductViewSet


@api_view(['GET'])
def ProductView(request):
    query_set = Product.objects.all().order_by("-id")
    sterilized = ProductViewSet (query_set, many=True)
    return Response(sterilized.data)

@api_view(['GET'])
def oneProductView(request, id):
    query_set = Product.objects.get(id =id)
    sterilized = ProductViewSet (query_set, many=False)
    return Response(sterilized.data)

@api_view(['POST'])
def createOneProductView (request):
    serialized = ProductViewSet(data=request.data)
    if serialized.is_valid():
        serialized.save()
    else:
        print("Invlaid Data")
    return Response(serialized.data)

@api_view(['POST'])
def updateOneProductView(request, id):
    serialized = ProductViewSet(instance=Product.objects.get(id=id), data=request.data) #instance specifies product
    if serialized.is_valid():
        serialized.save()
    else:
        print("Invlaid Data")
    return Response(serialized.data)

@api_view(['DELETE'])
def deleteOneProductView (request, id):
    Product.objects.get(id=id).delete()
    return Response("Deleted")



def index(request):
    return render(request, 'carousel.html')

def showProduct(request):
    get_data = Product.objects.all()  # get(brand_name="Apple")
    return render(request, 'product.html', {'data': get_data})

def one_product(request, id):
    get_one_data = Product.objects.get(id=id)
    return render(request, 'oneProduct.html', {'product_data': get_one_data})

def showBrand(request):
    get_data = Brand.objects.all()  # get(brand_name="Apple")
    return render(request, 'brand.html', {'brand_data': get_data})

def filtered_product(request):
    filtered_data = Product.objects.all()
    print(filtered_data)
    return render(request, 'filter.html', {'filter_data': filtered_data})



    # get_all_data = Product.objects.all().filter(price=client.id).order_by('check_in')
    # sorted_data = get_all_data.sort()

# def learn(request):
#     return HttpResponse("i am learning django")

    # one to one
    # a = Family.objects.get(home__Home ="Shrestha Niwas")
    # print(a)

    # one to many
    # a = Children.objects.get(belongs_to__parents_cast__startswith = "su")
    # print(a)

    # #create
    # testing.objects.create(firstName = "faran", num = 6)
    # return HttpResponse (f"hello {testing.firstName} {testing.num}")

    # get
    # testing1 = testing.objects.get(num = 1)
    # return HttpResponse (f"hello {testing1.firstName} {testing1.num}")

    # edit/update
    # testing2 = testing.objects.get(num = 2)
    # testing2.firstName = "bishwakarma"
    # testing2.save()
    # return HttpResponse (f"hello {testing2.num} {testing2.firstName}")

    # delete
    # testing3 = testing.objects.get(num = 3).delete() #testing3.delete()
    # return HttpResponse (f"hello")

    # get
    # testing3 = testing.objects.get(num = 3)
    # testing3.firstName = "ramayan"
    # return HttpResponse (f"hello {testing3.firstName}")

    # filter
    # testing4 = testing.objects.filter(firstName__startswith = "am")
    # print(testing4)
    # return HttpResponse (f"hello {testing4.firstName} {testing4.num}")

    # testing4 = testing.objects.filter(firstName__startswith = "am")
    # print(testing4)
    # return HttpResponse (f"hello")
