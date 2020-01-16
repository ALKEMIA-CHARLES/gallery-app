from django.shortcuts import render , redirect
from dashboard.models import Images, Location, Category
# Create your views here.
def index(request):
    images = Images.show_images()
    return render(request, "dashboard/index.html", context={"images":images})

def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search", None)
        searched_images = Images.search_image_by_category(search_term)
        results = len(searched_images)
        message = "{}".format(search_term)
        
        return render(request, "dashboard/search.html", context={"message":message,
                                                            "images":searched_images,
                                                            "results":results})
    else:
        message = "You have not searched for any photo"
        return render(request, "dashboard/index.html", context={"message":message})
def location_filter(request, id):
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
