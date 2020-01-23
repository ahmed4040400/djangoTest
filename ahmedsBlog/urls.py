
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import posts.views
import about.views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', posts.views.home),
    #the ?P<>[] stuff is called regex
    #it used to add some sort of variables to the urlpattern
    #the name of the variable is in this brackets <>
    #and we can access this variable from any where
    #in the project wide
    #the reason we use it instade of http parameters
    #that it uses validation
    #see that square brackets []
    #we're telling that we want the data to be numbers in it
    #otherwise it'll return 404 not found error
    url(r'^post/(?P<post_id>[0-9]+)/$', posts.views.post_info),

    url(r'^about/', about.views.about),


#using static to add the urlpattern of the images dir
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
