"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


#=============================Important============================================================

#####  defination of url function

##    def url(regex, view, kwargs=None, name=None):

   # regex : A regular expression for matching URL patterns in strings
   # view : A view function used to process the user request for a matched URL
   # name : A unique identifier for a given URL. This is a very important feature.  
            #Always remember to name your URLs. With this, you can change a specific URL in the whole project 
            #by just changing the regex. So it’s important to never hard code URLs in the views or templates, and always refer to the URLs by its name

#####

#=================================================================================================

from django.conf.urls import url
from django.contrib import admin
from boards import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^boards/(?P<pk>\d+)/$',views.board_topics,name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$',views.new_topic,name='new_topic'),
    url(r'^admin/', admin.site.urls)
]




##========== slug filed ====================
#Regex 	(?P<slug>[-\w]+)
#Example 	url(r'^posts/(?P<slug>[-\w]+)/$', views.post, name='post')
#Valid URL 	/posts/hello-world/
#Captures 	{'slug': 'hello-world'}

##========= username =====================
#regex (?P<username>[\w.@+-]+)
#Valid URL 	/profile/vitorfs/
#Captures 	{'username': 'vitorfs'}