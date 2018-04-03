import dropbox

#from web.utils import variables

from cullo.utils import variables


def get_dropbox_conn():
    dbx = dropbox.Dropbox(variables.dropbox_token)
    return dbx