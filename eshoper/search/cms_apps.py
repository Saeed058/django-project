from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext as _


class search(CMSApp):
    app_name = "search"
    name = _("search")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["search.urls"]


apphook_pool.register(search)  # register the application