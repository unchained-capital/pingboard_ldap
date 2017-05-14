from yaml import load

CONFIG = {
    # Pingboard API
    'pingboard.id':     None,
    'pingboard.secret': None,

    # LDAP Server
    'ldap.host':                   'localhost',
    'ldap.port':                   389,
    'ldap.bind_dn':                None,
    'ldap.bind_password':          None,
    'ldap.user_search_base_dn':    'ou=People,dc=example,dc=com',
    'ldap.attributes.first_name':  'givenName',
    'ldap.attributes.last_name':   'sn',
    'ldap.attributes.email':       'mail',
    'ldap.attributes.phone':       'telephoneNumber',
    'ldap.attributes.title':       'title',
    'ldap.attributes.description': 'description',
    'ldap.attributes.photo':       'jpegPhoto',
}

def load_config(path):
    CONFIG.update(load(open(path)))

def get_config(key, default=None):
    return CONFIG.get(key, default)
