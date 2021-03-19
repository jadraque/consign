from . import sessions


def consign(method, data, url, **kwargs):
    '''Constructs and sends a :class:`Request <Request>`.
    :param method: method for the new :class:`Consign` object: ``CSV``, etc.
    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    :param delimiter: delimiter used to separate elements in a CSV row.
    '''
    # By using the 'with' statement we are sure the session is closed, thus we
    # avoid leaving sockets open which can trigger a ResourceWarning in some
    # cases, and look like a memory leak in others.
    with sessions.Session() as session:
        return session.consign(method=method, data=data, url=url, **kwargs)


def csv(data, url, **kwargs):
    r'''Stores a CSV file locally.

    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    '''
    return consign('csv', data, url, **kwargs)


def json(data, url, **kwargs):
    r'''Stores a JSON file locally.

    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    '''
    return consign('json', data, url, **kwargs)


def txt(data, url, **kwargs):
    r'''Stores a TXT file locally.

    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    '''
    return consign('txt', data, url, **kwargs)


def html(data, url, **kwargs):
    r'''Stores a HTML file locally.

    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    '''
    return consign('html', data, url, **kwargs)


def pdf(data, url, **kwargs):
    r'''Stores a PDF file locally.

    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    '''
    return consign('pdf', data, url, **kwargs)


def img(data, url, **kwargs):
    r'''Stores an image locally.

    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    '''
    return consign('img', data, url, **kwargs)


def blob(data, url, **kwargs):
    r'''Stores a PDF file locally.

    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    '''
    return consign('blob', data, url, **kwargs)


def table(data, url, **kwargs):
    r'''Stores an image locally.

    :param data: data for the new :class:`Consign` object.
    :param url: path for the new :class:`Consign` object.
    '''
    return consign('table', data, url, **kwargs)
