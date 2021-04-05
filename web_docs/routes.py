from web_docs.views import index, docs_post, docs_update, docs_delete


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/post', docs_post)
    app.router.add_get('/update', docs_update)
    app.router.add_get('/delete', docs_delete)
