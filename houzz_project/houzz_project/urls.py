
from django.contrib import admin
from django.urls import path, include

from houzz import urls
from sign_in import sign_inurls
from sign_up import sign_upurls
from sales import saleurl
from join import join_url
from cart import carturl
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your other URL patterns ...
        path('admin/', admin.site.urls),
        # path('', include(urls)),
        path('', include(sign_inurls)),
        path('signup/', include(sign_upurls)),
        path('sale/', include(saleurl)),
        path('join/', include(join_url)),
        path('cart/', include(carturl)),
        path('register_user/', include(join_url)),
        path('add_to_cart/', include(carturl)),
        path('sell/', include(carturl)),
        path('logout/', include(sign_inurls)),



]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

