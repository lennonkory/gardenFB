"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('/', controller='index', action='index')

    # USER ACCESSIBLE:
    # Admin / Coord
    map.connect('/dashboard', controller='tools', action='index') #adminDash or coordDash, depending on cookie
    map.connect('/hostsites', controller='tools', action='manageHS')
    map.connect('/accounts', controller='tools', action='manageAccounts')
    map.connect('/login', controller='users', action='login')
    map.connect('/cashsales', controller='sales', action='index')

    map.connect('/user/me', controller='users', action='me')

    # Not logged in user
    map.connect('/shop', controller='shop', action='home')
    map.connect('/shop/buy', controller='shop', action='newOrder')
    map.connect('/info', controller='index', action='info')
    map.connect('/donate', controller='sales', action='donate')
    map.connect('/contact', controller='index', action='contact')

    # DATA ACCESSIBLE
    map.connect('/order', controller='orders', action='orders')
    map.connect('/order/distribution', controller='data', action='distribution')
    map.connect('/sales/customers', controller='sales', action='customers')
    map.connect('/sales/donors', controller='sales', action='donors')
    map.connect('/sales/cashsales', controller='sales', action='sales')
    map.connect('/user/auth', controller='users', action='auth')
    map.connect('/user/logout', controller='users', action='logout')
    map.connect('/user', controller='users', action='user')
    map.connect('/hs', controller='hostsites', action='host_site')

    return map
