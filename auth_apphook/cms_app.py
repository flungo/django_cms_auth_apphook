from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class DjangoAuthApphook(CMSApp):
    name = _("Django Auth Apphook")
    urls = ["django.contrib.auth.urls"]


apphook_pool.register(DjangoAuthApphook)