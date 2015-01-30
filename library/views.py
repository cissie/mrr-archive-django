from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from json import dumps, loads
from library.forms import ArtistForm, UserForm, UserProfileForm
from library.models import Artist, RecordTitle, Country, FormatType, ReleaseYear, RecordLabel, RecordReview, \
    CatalogNumber, IssueNumber, FileUnder, Notes
from time import sleep
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")


def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL artists currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    artist_list = Artist.objects.all()

    # The following two lines are new.
    # We loop through each artist returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    # for artist in artist_list:
    #     artist.url = artist.name.replace(' ', '_')

    page = request.GET.get('page')
    number_artists = request.GET.get('artists')

    if not number_artists:
        number_artists = 25

    paginator = Paginator(artist_list, number_artists)
    try:
        artists = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        artists = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        artists = paginator.page(paginator.num_pages)

    context_dict = {'artists': artists}

    # Render the response and send it back!
    return render_to_response('library/index.html', context_dict, context)

@csrf_exempt
def ajax(request):
    if request.method == "POST":
        new_artist = Artist()
        new_artist.name = request.POST["artist"]
        new_artist.save()

    # Query the database for a list of ALL artists currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    artist_list = list(Artist.objects.all())
    ajax_artist_list = []
    for a in artist_list:
        ajax_artist_list.append({
            "artist": a.name
        })

    return HttpResponse(dumps(ajax_artist_list, indent=4), content_type="application/json")


def dom(request):
    if request.method == "POST":
        print request.POST

    return render(request, 'library/dom.html')


def artist(request, artist_id):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    try:
        # Can we find an artist with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        artist = Artist.objects.get(id=artist_id)
        print artist.name
        # Retrieve all of the associated titles.
        # Note that filter returns >= 1 model instance.

    except Artist.DoesNotExist:
        # We get here if we didn't find the specified artist.
        # Don't do anything - the template displays the "no artist" message for us.
        pass

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the artist passed by the user.
    context_dict = {
        "artist": artist,
        "record_title_list": RecordTitle.objects.filter(artist=artist),
        "country": Country.objects.filter(artist=artist),
        "file_under": FileUnder.objects.filter(artist=artist)
    }



    # Go render the response and return it to the client.
    return render_to_response('library/artist.html', context_dict, context)

def record_title(request):
    context = RequestContext(request)
    record_title_list = RecordTitle.objects.all()
    context_dict = {
        "record_title": record_title_list
    }
    return render_to_response('library/record_title.html', context_dict, context)

def record_title_detail(request, record_title_id):
    context = RequestContext(request)
    try:
        record_title = RecordTitle.objects.get(id=record_title_id)
        print record_title

    except RecordTitle.DoesNotExist:
        pass

    context_dict = {
        "record_title": record_title,
    }
    return render_to_response('library/record_title_detail.html', context_dict, context)


def record_label(request):
    context = RequestContext(request)
    record_label_list = RecordLabel.objects.all()
    context_dict = {
        "record_labels": record_label_list
    }
    return render_to_response('library/record_label.html', context_dict, context)

def record_label_detail(request, record_label_id):
    context = RequestContext(request)
    try:
        record_label = RecordLabel.objects.get(id=record_label_id)

    except RecordLabel.DoesNotExist:
        pass
    try:
        record_title_list = RecordTitle.objects.filter(record_label=record_label)
    except RecordTitle.DoesNotExist:
        pass
    context_dict = {
        "record_label": record_label,
        "record_title_list": record_title_list
    }
    return render_to_response('library/record_label_detail.html', context_dict, context)


def record_review(request):
    record_review = RecordReview.objects.get
    return render(request, 'library/record_review.html')


def add_artist(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = ArtistForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ArtistForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('library/add_artist.html', {'form': form}, context)


def register(request):
    if request.method == "POST":
        User.objects.create_user(request.POST["username"], None, request.POST["password"])
    return render(request, 'library/register.html')


def login(request):
    if request.method == "POST":
        user =auth.authenticate(username=request.POST["username"],
                                password=request.POST["password"])
        if user is not None:
            # the password verified for the user
            if user.is_active:
                auth.login(request, user)
                print("User is valid, active and authenticated")
                return redirect('index')
            else:
                print("The password is valid, but the account has been disabled.")

        else:
            print("The username and password were incorrect.")
    return render(request, 'library/login.html')


# def search(request, text):
#     if request.method == 'GET':
#         results = {
#             record_titles: RecordTitle.objects.filter(record_title__startswith=""),
#             artists: Artist.objects.filter(artist__startswith=""),
#             record_labels: RecordLabel.objects.filter(record_label__startswith="")
#         }
#
#
#     return HttpResponse(results, content_type='application/json')


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/library/')

# def load_data(request):
#     with open("record_collection.json") as f:
#         json_data = json.load(f)
#         checked = []
#         count = 0
#         for d in json_data:
#             if d["artist"] not in checked:
#                 try:
#                     new_artist = Artist.objects.get(name=d["artist"])
#                 except Artist.DoesNotExist:
#                     new_artist = Artist(name=d["artist"])
#                 try:
#                     country = Country.objects.get(country=d["country"])
#                 except Country.DoesNotExist:
#                     country = Country(country=d["country"])
#                     country.save()
#                 new_artist.country = country
#                 try:
#                     file_under = FileUnder.objects.get(file_under=d["file_under"])
#                 except FileUnder.DoesNotExist:
#                     file_under = FileUnder(file_under=d["file_under"])
#                     file_under.save()
#                 new_artist.file_under = file_under
#                 new_artist.save()
#                 artist_id = new_artist.id
#                 sleep(0.015)
#                 checked.append(new_artist)
#                 print len(checked)
#             new_title = RecordTitle()
#             new_title.artist = new_artist
#             new_title.record_title = d["record_title"]
#             try:
#                 format_type = FormatType.objects.get(format_type=d["format_type"])
#             except FormatType.DoesNotExist:
#                 format_type = FormatType(format_type=d["format_type"])
#                 format_type.save()
#             new_title.format_type = format_type
#             if d["release_year"] is not None:
#                 try:
#                     release_year = ReleaseYear.objects.get(release_year=d["release_year"])
#                 except ReleaseYear.DoesNotExist:
#                     release_year = ReleaseYear(release_year=d["release_year"])
#                     release_year.save()
#                 new_title.release_year = release_year
#             try:
#                 record_label = RecordLabel.objects.get(record_label=d["label_name"])
#             except RecordLabel.DoesNotExist:
#                 record_label = RecordLabel(record_label=d["label_name"])
#                 record_label.save()
#             new_title.record_label = record_label
#             try:
#                 catalog_number = CatalogNumber.objects.get(catalog_number=d["catalog_number"])
#             except CatalogNumber.DoesNotExist:
#                 catalog_number = CatalogNumber(catalog_number=d["catalog_number"])
#                 catalog_number.save()
#             new_title.catalog_number = catalog_number
#             if d["issue_number"] is not None:
#                 try:
#                     issue_number = IssueNumber.objects.get(issue_number=d["issue_number"])
#                 except IssueNumber.DoesNotExist:
#                     issue_number = IssueNumber(issue_number=d["issue_number"])
#                     issue_number.save()
#                 new_title.issue_number = issue_number
#                 if d["notes"] is not None:
#                     try:
#                         notes = Notes.objects.get(notes=d["notes"])
#                     except Notes.DoesNotExist:
#                         notes = Notes(notes=d["notes"])
#                         notes.save()
#                     new_title.notes = notes
#             new_title.save()
#             sleep(0.015)
#     return HttpResponse(content_type='application/json')












