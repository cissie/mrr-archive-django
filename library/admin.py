from django.contrib import admin
from library.models import Artist, RecordTitle, Country, RecordLabel, CatalogNumber, Discography, BandMember, \
    RecordReview, IssueNumber, ReviewerName

class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(RecordTitle)
admin.site.register(Country)
admin.site.register(RecordLabel)
admin.site.register(CatalogNumber)
admin.site.register(Discography)
admin.site.register(BandMember)
admin.site.register(RecordReview)
admin.site.register(IssueNumber)
admin.site.register(ReviewerName)




