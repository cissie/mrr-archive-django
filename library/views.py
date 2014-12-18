from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from json import dumps, loads
from library.forms import ArtistForm, UserForm, UserProfileForm
from library.models import Artist, RecordTitle, Country, FormatType, ReleaseYear, RecordLabel, RecordReview, \
    CatalogNumber, IssueNumber, FileUnder, Notes
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")


def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL artists currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    artist_list = Artist.objects.all()
    context_dict = {'artists': artist_list}

    # The following two lines are new.
    # We loop through each artist returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    for artist in artist_list:
        artist.url = artist.name.replace(' ', '_')

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


def artist(request, artist_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the artist name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    artist_name = artist_name_url.replace('_', ' ')

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the artist passed by the user.
    context_dict = {'artist_name': artist_name}

    try:
        # Can we find an artist with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        artist = Artist.objects.get(artist=artist_name)

        # Retrieve all of the associated titles.
        # Note that filter returns >= 1 model instance.
        record_title = RecordTitle.objects.filter(artist=artist)

        # Adds our results list to the template context under name pages.
        context_dict['record_title'] = record_title
        # We also add the artist object from the database to the context dictionary.
        # We'll use this in the template to verify that the artist exists.
        context_dict['artist'] = artist
    except Artist.DoesNotExist:
        # We get here if we didn't find the specified artist.
        # Don't do anything - the template displays the "no artist" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('library/artist.html', context_dict, context)

def record_title(request):
    record_title = RecordTitle.objects.get
    return render(request, 'library/record_title.html')


def record_label(request):
    record_label = RecordLabel.objects.get
    return render(request, 'library/record_label.html')


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
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'library/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/library/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your MRR Archive account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('library/login.html', {}, context)

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


def load_data(request):
    with open("record_collection.json") as f:
        json_data = json.load(f)
        last_artist = ""
        for d in json_data:
            if last_artist != d["artist"]:
                print d["artist"]
                new_artist = Artist()
                new_artist.name = d["artist"]
                new_artist.save()
                last_artist = d["artist"]
            #start adding records at same indentation as above

            # for k, v in d.iteritems():
                # print k, v
        # artist = Artist()
        # record_title = RecordTitle()
        # country = Country()
        # format_type = FormatType()
        # release_year = ReleaseYear()
        # record_label = RecordLabel()
        # catalog_number = CatalogNumber()
        # issue_number = IssueNumber()
        # file_under = FileUnder()
        # notes = Notes()
        return HttpResponse(content_type='application/json')












