from django.http import HttpResponse, JsonResponse


def health(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return JsonResponse({"message": "Hello World"})

def getFibonacciList():
    numbers = {}
    n1 = 0
    n2 = 1
    nextTerm = n2
    
    for i in range(1, 1001):
        nextTerm = n1 + n2
        n1 = n2
        n2 = nextTerm
        numbers[i] = n1
    
    return numbers

def fibonacci(request):
    fibonacci = getFibonacciList()
    return JsonResponse(fibonacci)
