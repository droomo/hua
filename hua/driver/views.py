from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from hua.models import Driver


@csrf_exempt
def check_number(request):
    driver_number = request.POST.get('driver_id', 0)
    response = dict(
        status=400,
        message=u'Params error'
    )
    if driver_number != 0:
        try:
            Driver.objects.get(driver_number=driver_number)
        except Driver.DoesNotExist:
            response['message'] = u'ID %s Not Found.' % driver_number
        else:
            response = dict(
                status=200,
                message='success'
            )
    return JsonResponse(response)

@csrf_exempt
def update_info(request):
    driver_number = request.POST.get('driver_id', 0)
    response = dict(
        status=400,
        message=u'Params error'
    )
    print request.POST
    if driver_number != 0:
        try:
            driver = Driver.objects.get(driver_number=driver_number)
            driver.longitude, driver.latitude = float(request.POST.get('longitude', 0)), float(request.POST.get('latitude', 0))
            driver.update_at = timezone.now()

            driver.save()
        except Driver.DoesNotExist:
            response['message'] = u'ID %s Not Found.' % driver_number
        else:
            response = dict(
                status=200,
                message='success'
            )
    return JsonResponse(response)

def get_location(request):
    drivers = list(Driver.objects.values('driver_number', 'latitude', 'longitude', 'update_at').all())

    return JsonResponse(drivers, safe=False)

def follow(request):

    return render(request, 'follow.html', context={})

