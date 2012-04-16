"""
Simplified functions for using the Fred API.
"""

import os
from .core import Fred


def key(api_key):
    os.environ['FRED_API_KEY'] = api_key
    return Fred()


#####################
# Category
#####################

def category(**kwargs):
    """Get a category."""
    if 'series' in kwargs:
        kwargs.pop('series')
        path = 'series'
    else:
        path = None
    return Fred().category(path, **kwargs)


def children(**kwargs):
    """Get child categories for a specified parent category."""
    return Fred().category('children', **kwargs)


def related(**kwargs):
    """Get related categories for a specified category."""
    return Fred().category('related', **kwargs)


def category_series(**kwargs):
    """Get the series in a category."""
    return Fred().category('series', **kwargs)


#####################
# Releases
#####################

def releases(release_id=None, **kwargs):
    """Get all releases of economic data."""
    if not 'id' in kwargs and release_id is not None:
        kwargs['release_id'] = id
        return Fred().release(**kwargs)
    return Fred().releases(**kwargs)


def dates(**kwargs):
    """Get release dates for economic data."""
    return Fred().releases('dates', **kwargs)


#####################
# Series
#####################

def series(**kwargs):
    """Get an economic data series."""
    if 'release' in kwargs:
        kwargs.pop('release')
        path = 'release'
    else:
        path = None
    return Fred().series(path, **kwargs)


def observations(**kwargs):
    """Get an economic data series."""
    return Fred().series('observations', **kwargs)


def search(**kwargs):
    """Get economic data series that match keywords."""
    return Fred().series('search', **kwargs)


def updates(**kwargs):
    """Get economic data series sorted in descending order."""
    return Fred().series('updates', **kwargs)


def vintage(**kwargs):
    """
    Get the dates in history when a series' data values were revised or new
    data values were released.
    """
    return Fred().series('vintagedate', **kwargs)


#####################
# Sources
#####################

def source(source_id=None, **kwargs):
    """Get a source of economic data."""
    if source_id is not None:
        kwargs['source_id'] = source_id
    elif 'id' in kwargs:
        source_id = kwargs.pop('id')
        kwargs['source_id'] = source_id
    if 'releases' in kwargs:
        kwargs.pop('releases')
        path = 'releases'
    else:
        path = None
    return Fred().source(path, **kwargs)


def sources(**kwargs):
    """Get the sources of economic data."""
    return Fred().sources(**kwargs)
