from django.contrib import admin
from library.models import Artist, RecordTitle, BandMember, Country, FormatType, ReleaseYear, RecordLabel, \
    CatalogNumber, IssueNumber, RecordReview, ReviewerName, TrackName, FileUnder, Notes, UserProfile

class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

class RecordTitleAdmin(admin.ModelAdmin):
    search_fields = ["record_title"]
    ordering = ["artists"]

class RecordLabelAdmin(admin.ModelAdmin):
    search_fields = ["record_label"]

class CatalogNumberAdmin(admin.ModelAdmin):
    search_fields = ["catalog_number"]

class CountryAdmin(admin.ModelAdmin):
    search_fields = ["country"]
    ordering = ["country"]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(RecordTitle, RecordTitleAdmin)
admin.site.register(BandMember)
admin.site.register(Country, CountryAdmin)
admin.site.register(FormatType)
admin.site.register(ReleaseYear)
admin.site.register(RecordLabel, RecordLabelAdmin)
admin.site.register(CatalogNumber, CatalogNumberAdmin)
admin.site.register(IssueNumber)
admin.site.register(RecordReview)
admin.site.register(ReviewerName)
admin.site.register(TrackName)
admin.site.register(FileUnder)
admin.site.register(Notes)
admin.site.register(UserProfile)




