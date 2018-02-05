from django.conf.urls import url
from stock.top import topview

urlpatterns = [
  url(r'stock/top/toplist', topview.getTopList),
]
