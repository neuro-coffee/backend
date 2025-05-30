from rest_framework.routers import DefaultRouter

from apps.products import views

app_name = 'products'

urlpatterns = []

router = DefaultRouter()

router.register('menus', views.MenuView, 'menus')
router.register('promos', views.PromoView, 'promos')
router.register('baskets', views.BasketView, 'baskets')
router.register('', views.ProductView, 'products')

urlpatterns += router.urls
