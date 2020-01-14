from django.shortcuts import render , redirect
from dashboard.models import Images, Location, Category
# Create your views here.
def index(request):
    image = Images.objects.all()
    return render(request, "dashboard/index.html", context={"image":image})

def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        searched_images = Images.search_photo_by_category(search_term)
        results = len(searched_photos)
        message = "{}".format(search_term)
        
        return render(request, "dashboard/search.html", context={"message":message,
                                                            "searched_photos":searched_photos,
                                                            "results":results})
    else:
        message = "You have not searched for any photo"
        return render(request, "dashboard/search.html", context={"message":message})
def location_filter(request):
    images = Images.objects.filter(location__id = id)
    results = len(images)
    location = Location.objects.get(id = id)
    locations = Location.objects.all()

    return render(request, "dashboard/location.html", context={"images":images,
                                                             "results":results,
                                                             "location":location,
                                                             "locations":locations})
def scroll(request):
    images = Images.show_all_photos()
    locations = Location.objects.all()
    return render(request, "dashboard/scroll.html", context={"images":images,
                                                           "locations":locations})
