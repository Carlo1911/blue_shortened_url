from django.db import models
from django.utils.translation import gettext_lazy as _


class TransformerUrl(models.Model):
    url = models.CharField(_("Url destino"), max_length=255)
    title = models.CharField(_("Título"), max_length=255, blank=True)
    slug = models.SlugField(_("Url generada"), max_length=255, unique=True)
    visited_count = models.IntegerField(_("Cantidad de visitads"), default=0)
    created_at = models.DateTimeField(_("Fecha de creación"), auto_now_add=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _("Url generada")
        verbose_name_plural = _("Urls generadas")
