from django.db import models
from apps.specuser.models import *

class DocumentCreateModel(models.Model):
    incomingdoc = models.BooleanField(("Gelen Evrak"), default=False)
    outgoingdoc = models.BooleanField(("Giden Evrak"), default=False)
    amount = models.BooleanField(("Tutanak"), default=False)
    high = models.BooleanField(("Yüksek"), default=False)
    middle = models.BooleanField(("Orta"), default=False)
    low = models.BooleanField(("Düşük"), default=False)
    docno = models.CharField(("Evrak No"), max_length=150)
    docdate = models.DateField(("Evrak Tarihi"), auto_now=False, auto_now_add=False)
    doccount = models.IntegerField(("Evrak Sayisi"))
    relevantunit = models.CharField(("İlgili Birim"), max_length=150)
    relevantinstitution = models.CharField(("İlgili Kurum"), max_length=150)
    docsubject = models.CharField(("Evrak Konusu"), max_length=150)
    user = models.ForeignKey(
        SiteUser, verbose_name=("Formu Dolduran"), on_delete=models.CASCADE
    )
    files = models.FileField(("Evrak Yükleme"), upload_to="document", max_length=100)
    detail = models.TextField(("Rapor Detay"))

    def __str__(self) -> str:
        return self.docsubject