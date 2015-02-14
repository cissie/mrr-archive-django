from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from json import dumps, loads
from library.forms import EditForm, UserForm, UserProfileForm, CoverArtForm, RecordReviewForm
from library.models import Artist, RecordTitle, Country, FormatType, ReleaseYear, RecordLabel, RecordReview, \
    CatalogNumber, IssueNumber, FileUnder, Notes, ReviewerName, ReviewerName
import json
from time import sleep
import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")


# Loads all of the artists and routes them to be listed in the index template.
def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL artists currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    artist_list = Artist.objects.all()

    # We loop through each artist returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    # for artist in artist_list:
    #     artist.url = artist.name.replace(' ', '_')

    # adding pagination
    page = request.GET.get('page')
    number_artists = request.GET.get('artists')

    if not number_artists:
        number_artists = 25
    if not page:
        page = 1
    # passing the artist_list and number_artists to paginator
    paginator = Paginator(artist_list, number_artists)
    try:
        artists = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        artists = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        artists = paginator.page(paginator.num_pages)

# Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the artist passed by the user.
    # The artist detail view will also display the title, country and file_under fields.
    context_dict = {
        "artists": artists
    }

    # Preserve all GET params
    params = []
    for key, value in request.GET.iteritems():
        params.append("&{}={}".format(key, value))

    # if page is not in params this will be appended
    # added because pagination wasn't working at page 0
    if not params:
        params = ["&page=1&"]

    # The first char is a &, which we replace with a ?
    params = '?' + ''.join(params)[1:]

    # Only change the page number
    if artists.has_previous():
        context_dict['prev_page_url'] = re.sub('page=(\d+)', 'page=' + str(artists.previous_page_number()), params)
    if artists.has_next():
        context_dict['next_page_url'] = re.sub('page=(\d+)', 'page=' + str(artists.next_page_number()), params)

    # Render the response and send it back!
    return render_to_response('library/index.html', context_dict, context)


# AJAX practice. Not meant to be a permanent part of the project
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


# Related to the AJAX practice above. Not meant to be a permanent part of the project
def dom(request):
    if request.method == "POST":
        print request.POST

    return render(request, 'library/dom.html')


# Artist detail view. Loops through artists, record titles, country, and file under
# Routes fields to be displayed on artist template
def artist(request, artist_id):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    try:
        # Can we find an artist with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        # Pass artist_id argument to Artist model
        artist = Artist.objects.get(id=artist_id)
        print artist.name

    except Artist.DoesNotExist:
        # We get here if we didn't find the specified artist.
        pass

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the artist passed by the user.
    # The artist detail view will also display the title, country and file_under fields.
    context_dict = {
        "artist": artist,
        "record_title_list": RecordTitle.objects.filter(artist=artist),
        "country": Country.objects.filter(artist=artist),
        "file_under": FileUnder.objects.filter(artist=artist)
    }

    # Go render the response and return it to the client.
    return render_to_response('library/artist.html', context_dict, context)


# Loads all of the record titles and routes them to be listed on the record_title template
def record_title(request):
    context = RequestContext(request)
    record_title_list = RecordTitle.objects.all()

    # adding pagination
    page = request.GET.get('page')
    number_titles = request.GET.get('titles')

    if not number_titles:
        number_titles = 25
    if not page:
        page = 1

    paginator = Paginator(record_title_list, number_titles)
    try:
        record_title_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        record_title_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        record_title_list = paginator.page(paginator.num_pages)

    # Empty context dict
    context_dict = {}

    # Preserve all GET params
    params = []
    for key, value in request.GET.iteritems():
        params.append("&{}={}".format(key, value))

    # If page is not in params this will be appended
    # Added because pagination wasn't working at page 0
    if not params:
        params = ["&page=1&"]

    # The first char is a &, which we replace with a ?
    params = '?' + ''.join(params)[1:]

    # Only change the page number
    if record_title_list.has_previous():
        context_dict['prev_page_url'] = re.sub('page=(\d+)', 'page=' + str(record_title_list.previous_page_number()), params)
    if record_title_list.has_next():
        context_dict['next_page_url'] = re.sub('page=(\d+)', 'page=' + str(record_title_list.next_page_number()), params)

    # Populates the context dict
    context_dict["record_title"] = record_title_list

    return render_to_response('library/record_title.html', context_dict, context)


# Record title detail view. Loops through record titles and corresponding foreign key fields.
# Fields will be displayed on record_title_detail template
def record_title_detail(request, record_title_id):
    context = RequestContext(request)
    try:
        # The .get() method returns one model instance or raises an exception.
        # Pass record_title_id argument to RecordTitle model
        record_title = RecordTitle.objects.get(id=record_title_id)
        print record_title

    except RecordTitle.DoesNotExist:
        pass

    context_dict = {
        "record_title": record_title,
    }
    return render_to_response('library/record_title_detail.html', context_dict, context)


# Loads all of the record labels and routes them to be listed on the record_label template
def record_label(request):
    context = RequestContext(request)
    record_label_list = RecordLabel.objects.all()

    # adding pagination
    page = request.GET.get('page')
    number_labels = request.GET.get('labels')

    if not number_labels:
        number_labels = 25
    if not page:
        page = 1

    paginator = Paginator(record_label_list, number_labels)
    try:
        record_label_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        record_label_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        record_label_list = paginator.page(paginator.num_pages)

    context_dict = {
        "record_labels": record_label_list
    }

    params = []
    for key, value in request.GET.iteritems():
        params.append("&{}={}".format(key, value))

    # if page is not in params this will be appended
    # added because pagination wasn't working at page 0
    if not params:
        params = ["&page=1&"]

    # The first char is a &, which we replace with a ?
    params = '?' + ''.join(params)[1:]

    # Only change the page number
    if record_label_list.has_previous():
        context_dict['prev_page_url'] = re.sub('page=(\d+)', 'page=' + str(record_label_list.previous_page_number()), params)
    if record_label_list.has_next():
        context_dict['next_page_url'] = re.sub('page=(\d+)', 'page=' + str(record_label_list.next_page_number()), params)

    return render_to_response('library/record_label.html', context_dict, context)


# Record label detail view. Loops through record labels and corresponding titles.
# Associated titles will be displayed through the record_label_detail template.
def record_label_detail(request, record_label_id):
    context = RequestContext(request)

    try:
        # The .get() method returns one model instance or raises an exception.
        # Pass record_label_id argument to RecordLabel model
        record_label = RecordLabel.objects.get(id=record_label_id)
    except RecordLabel.DoesNotExist:
        pass

    try:
        # filters record title data to appropriate record label
        record_title_list = RecordTitle.objects.filter(record_label=record_label)
    except RecordTitle.DoesNotExist:
        pass

    # The record label detail view will also display all the titles for a particular label
    context_dict = {
        "record_label": record_label,
        "record_title_list": record_title_list
    }
    return render_to_response('library/record_label_detail.html', context_dict, context)


# Loads all of the countries and routes them to be listed on the country template.
def country(request):
    context = RequestContext(request)
    country_list = Country.objects.all()
    context_dict = {
        "countries": country_list
    }
    return render_to_response('library/country.html', context_dict, context)


# Country detail view. Loops through countries and corresponding artists and titles.
# Associated artists and titles will be displayed through the country template.
def country_detail(request, country_id):
    context = RequestContext(request)
    try:
        # The .get() method returns one model instance or raises an exception.
        # Pass country id argument to Country model
        country = Country.objects.get(id=country_id)
    except Country.DoesNotExist:
        pass
    try:
        # filters artist data to corresponding country
        artist_list = Artist.objects.filter(country=country)
    except Artist.DoesNotExist:
        pass

    # The country detail view will display the country along with corresponding artists and record titles
    context_dict = {
        "country": country,
        "artist_list": artist_list,
        "record_title": record_title
    }
    return render_to_response('library/country_detail.html', context_dict, context)


# Displays all the titles that a reviewer has reviewed
def record_reviewer_detail(request, reviewer_name_id):
    context = RequestContext(request)
    try:
        # The .get() method returns one model instance or raises an exception.
        # Pass reviewer_name_id argument to ReviewerName model
        reviewer_name = ReviewerName.objects.get(id=reviewer_name_id)
    except ReviewerName.DoesNotExist:
        pass
    try:
        # filters record title data to corresponding Reviewer
        record_title_list = RecordTitle.objects.filter(reviewer_name=reviewer_name)
    except RecordTitle.DoesNotExist:
        pass

    # The record reviewer detail view will display the reviewer along with corresponding titles they've reviewed
    context_dict = {
        "record_title_list": record_title_list
    }
    return render_to_response('library/record_reviewer_detail.html', context_dict, context)


# To do. Still need to add more of a UI and a form to upload record reviews.
def record_review(request):
    record_review = RecordReview.objects.get
    return render(request, 'library/record_review.html')


@login_required
def edit_form(request, record_title_id):
    # Grab the right title to be edited
    record_title = RecordTitle.objects.get(id=record_title_id)
    # Load the record title to display on page
    context_dict = {
        'record_title': record_title,
        'form': EditForm(instance=record_title)
        }
    if request.method == 'POST':
        form = EditForm(request.POST, instance=record_title)
        if form.is_valid():
            form.save()
            return redirect('/') # name of view stated in urls
        else:
            form = EditForm(record_title)

    return render_to_response("library/edit_form.html", context_dict, context_instance=RequestContext(request))

# View for cover art upload form
@login_required
def upload_art(request, record_title_id):
    if request.method == 'POST':
        print "We got to post"
        img_form = CoverArtForm(request.POST, request.FILES)
        if img_form.is_valid():
            print "Form is valid"
            img = RecordTitle.objects.get(pk=record_title_id)
            img.cover_art = img_form.cleaned_data['cover_art']
            img.save()
            return HttpResponse('image upload success')
        else:
            print "Form is not valid"
            print img_form.errors
    return render_to_response("library/cover_art_form.html", context_instance=RequestContext(request))


@login_required
def add_review(request, record_title_id):
    # Grab the right title to be edited
    record_title = RecordTitle.objects.get(id=record_title_id)
    # Load the record title to display on page
    context_dict = {
        'record_title': record_title,
        }
    if request.method == 'POST':
        review_form = RecordReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('/') # name of view stated in urls
        else:
            form = RecordReviewForm(record_title)

    return render_to_response("library/record_review_form.html", context_dict, context_instance=RequestContext(request))


# Corresponds to form and template to add a review. Not very savvy. Needs a lot of work.
# Will probably switch to django crispy forms.
# def add_review(request):
#     # Get the context from the request.
#     context = RequestContext(request)
#
#     # A HTTP POST?
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#
#         # Have we been provided with a valid form?
#         if form.is_valid():
#             # Save the new category to the database.
#             form.save(commit=True)
#
#             # Now call the index() view.
#             # The user will be shown the homepage.
#             return index(request)
#         else:
#             # The supplied form contained errors - just print them to the terminal.
#             print form.errors
#     else:
#         # If the request was not a POST, display the form to enter details.
#         form = ReviewForm()
#
#     # Bad form (or form details), no form supplied...
#     # Render the form with error messages (if any).
#     return render_to_response('library/add_review.html', {'form': form}, context)


# User registration. Still undeveloped.
def register(request):
    if request.method == "POST":
        User.objects.create_user(request.POST["username"], None, request.POST["password"])
    return render(request, 'library/register.html')


# User login
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


# One day this will route to a live type search form with AJAX functionality
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


# leaving function commented out so that the url is accessible only when the data needs to be loaded
# def load_data(request):
#     with open("record_collection.json") as f:
#         json_data = json.load(f)
#           # creating an empty list so that artists are only loaded once
#         checked = []
#         count = 0
#           # looping through each data set in json_data to join the fields to the corresponding model
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
#                   # save the artist after the models that have a foreign key to it
#                 new_artist.save()
#                 artist_id = new_artist.id
#                   # using sleep to slow rate of the loading data
#                 sleep(0.015)
#                   # appends an artist if they have not yet been added to the checked list
#                 checked.append(new_artist)
#                   # using print to monitor the data in the console as it loads
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
#               # allows the same release year for multiple titles/artists
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
#               # save the titles after the models that have a foreign key to it
#             new_title.save()
#               # using sleep to slow rate of the loading data
#             sleep(0.015)
#     return HttpResponse(content_type='application/json')















