from django.contrib import admin
from library.models import Artist, RecordTitle, Country, FormatType, ReleaseYear, RecordLabel, CatalogNumber, \
    IssueNumber, Discography, RecordReview, ReviewerName

class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(RecordTitle)
admin.site.register(Country)
admin.site.register(FormatType)
admin.site.register(ReleaseYear)
admin.site.register(RecordLabel)
admin.site.register(CatalogNumber)
admin.site.register(IssueNumber)
admin.site.register(Discography)
admin.site.register(RecordReview)
admin.site.register(ReviewerName)




