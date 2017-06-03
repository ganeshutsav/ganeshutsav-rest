import flask

from ganeshutsav_rest.rest.mandal.model.mandal import Mandal

mandal_app = flask.Blueprint('mandal', __name__)


@mandal_app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def request_resolve():
    request = flask.request
    if request.method == 'GET':
        return index(request)

    elif request.method == 'PUT':
        return create(request)

    elif request.method == 'POST':
        return update(request)


def index(request):
    mandal = Mandal.init_empty_object()

    return str(mandal.list_all())


def create(request):
    assert request.method == 'PUT'
    data = request.json
    mandal = Mandal.init_using_params(data)
    result = mandal.save()
    return str(result)


def update(request):
    pass


def delete(request):
    pass
