from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from library.models import Artist
from library.models import RecordTitle
from library.forms import ArtistForm
from json import dumps


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


def ajax(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL artists currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    artist_list = list(Artist.objects.all())
    ajax_artist_list = []
    for a in artist_list:
        ajax_artist_list.append({
            "artist": a.name
        })

    return HttpResponse(dumps(ajax_artist_list, indent=4), content_type="application/json")


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

# def record_title(request):
    # context = RequestContext(request)

    # record_title = record_title_url.replace('_', ' ')

    # context_dict = {'record_title': record_title}

    # try:
        # record_title = RecordTitle.objects.get(record_title=record_title)
        # artist = Artist.objects.get(artist=artist_name)

        # context_dict['record_title'] = record_title
        # context_dict['artist'] = artist
    # except RecordTitle.DoesNotExist:
        # pass

    # return render_to_response('library/record_title.html, context_dict, context)


# def record_label(request):
    # context = RequestContext(request)

    # record_label_name = record_label_name_url.replace('_', ' ')

    # context_dict = {'record_label_name': record_label_name}

    # try:
        # record_label_name = RecordLabel.objects.get(record_label=record_label_name)

        # context_dict['record_label'] = record_label
    # except RecordLabel.DoesNotExist:
        # pass

    # return render_to_response('library/record_label.html', context_dict, context)


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
