from django.conf.urls.defaults import *
from haystack.backends.dummy_backend import SearchBackend, SearchQuery
from haystack.query import SearchQuerySet
from haystack.views import SearchView, FacetedSearchView


import haystack
haystack.autodiscover()


urlpatterns = patterns('haystack.views',
    url(r'^$', SearchView(), name='haystack_search'),
    url(r'^faceted/$', FacetedSearchView(searchqueryset=SearchQuerySet().facet('author')), name='haystack_faceted_search'),
)
