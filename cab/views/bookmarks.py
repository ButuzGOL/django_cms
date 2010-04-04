from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from cab.models import Bookmark, Snippet
from django.views.generic.list_detail import object_list

def add_bookmark(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    try:
         Bookmark.objects.get(user__pk=request.user.id,
                              snippet__pk=snippet.id)
    except Bookmark.DoesNotExist:
         bookmark = Bookmark.objects.create(user=request.user,
                                            snippet=snippet)
    return HttpResponseRedirect(snippet.get_absolute_url())

add_bookmark = login_required(add_bookmark)

def user_bookmarks(request):
    return object_list(
                    queryset=Bookmark.objects.filter(user__pk=request.user.id),
                       template_name='cab/user_bookmarks.html',
                       paginate_by=20)