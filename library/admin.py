from django.contrib import admin
from library.models import Artist, RecordTitle, Format, Country, Year, Label, Discography, \
    Member, Review, IssueNumber, Reviewer

admin.site.register(Artist)
admin.site.register(RecordTitle)
admin.site.register(Format)
admin.site.register(Country)
admin.site.register(Year)
admin.site.register(Label)
admin.site.register(Discography)
admin.site.register(Member)
admin.site.register(Review)
admin.site.register(IssueNumber)
admin.site.register(Reviewer)


