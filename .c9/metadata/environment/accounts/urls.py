{"filter":false,"title":"urls.py","tooltip":"/accounts/urls.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":15},"end":{"row":6,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":43,"mode":"ace/mode/python"}},"hash":"6dae2d85a62c56bb69494b829e02c662c83c7df6","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from . import urls_reset","from .views import index, register, profile, logout, login","","urlpatterns = [","    url(r'^register/$', register, name='register'),","    url(r'^profile/$', profile, name='profile'),","    url(r'^logout/$', logout, name='logout'),","    url(r'^login/$', login, name='login'),","    url(r'^password-reset/', include(urls_reset)),","]"],"id":3},{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from . import urls_reset","from .views import index, register, profile, logout, login","","urlpatterns = [","    url(r'^register/$', register, name='register'),","    url(r'^profile/$', profile, name='profile'),","    url(r'^logout/$', logout, name='logout'),","    url(r'^login/$', login, name='login'),","    url(r'^password-reset/', include(urls_reset)),","]"]}],[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from . import urls_reset","from .views import index, register, profile, logout, login","","urlpatterns = [","    url(r'^register/$', register, name='register'),","    url(r'^profile/$', profile, name='profile'),","    url(r'^logout/$', logout, name='logout'),","    url(r'^login/$', login, name='login'),","    url(r'^password-reset/', include(urls_reset)),","]"],"id":4},{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from accounts.views import logout, login, registration, user_profile","from accounts import url_reset","","urlpatterns = [","    url(r'^logout/', logout, name=\"logout\"),","    url(r'^login/', login, name=\"login\"),","    url(r'^register/', registration, name=\"registration\"),","    url(r'^profile/', user_profile, name=\"profile\"),","    url(r'^password-reset/', include(url_reset))","]"]}],[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from accounts.views import logout, login, registration, user_profile","from accounts import url_reset","","urlpatterns = [","    url(r'^logout/', logout, name=\"logout\"),","    url(r'^login/', login, name=\"login\"),","    url(r'^register/', registration, name=\"registration\"),","    url(r'^profile/', user_profile, name=\"profile\"),","    url(r'^password-reset/', include(url_reset))","]"],"id":5},{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from accounts.views import logout, login, registration, user_profile","from accounts import url_reset","","urlpatterns = [","    url(r'^logout/', logout, name=\"logout\"),","    url(r'^login/', login, name=\"login\"),","    url(r'^register/', registration, name=\"registration\"),","    url(r'^profile/', user_profile, name=\"profile\"),","    url(r'^password-reset/', include(url_reset))","]"]}]]},"timestamp":1587044450013}