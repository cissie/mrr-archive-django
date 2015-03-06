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

admin.site.register(Artist, ArtistAdmin)
admin.site.register(RecordTitle, RecordTitleAdmin)
admin.site.register(BandMember)
admin.site.register(Country)
admin.site.register(FormatType)
admin.site.register(ReleaseYear)
admin.site.register(RecordLabel, RecordLabelAdmin)
admin.site.register(CatalogNumber)
admin.site.register(IssueNumber)
admin.site.register(RecordReview)
admin.site.register(ReviewerName)
admin.site.register(TrackName)
admin.site.register(FileUnder)
admin.site.register(Notes)
admin.site.register(UserProfile)




