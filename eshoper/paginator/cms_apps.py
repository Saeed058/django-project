from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext as _


class paginator(CMSApp):
    app_name = "paginator"
    name = _("paginator")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["paginator.urls"]


apphook_pool.register(paginator)  # register the application