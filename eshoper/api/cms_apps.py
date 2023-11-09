from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext as _


class api(CMSApp):
    app_name = "api"
    name = _("api")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["api.urls"]


apphook_pool.register(api)  # register the application