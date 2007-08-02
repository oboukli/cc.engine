import grok
from zope.interface import implements
from zope.publisher.interfaces import NotFound
from zope.i18n import translate

import cc.license
from cc.license.exceptions import LicenseException

from cc.engine import interfaces

class BrowserLicense(grok.Model):
    implements(interfaces.ILicense)

    TARGET_NAMES = ('deed', 'rdf', 'rdf-checksum',
                    'legalcode', 'legalcode-checksum')

    def __init__(self, parent, pieces):
        self.__parent__ = parent
        self.__name__ = pieces[-1]

        self.pieces = pieces
        
    @property
    def license(self):
        """Return the cc.license.License object selected."""

        # decode the version and jurisdiction
        if len(self.pieces) > 2:
            version, jurisdiction = self.pieces[1:3]
        elif len(self.pieces) > 1:
            version, jurisdiction = self.pieces[1], None
        
        # XXX cache me!
        return cc.license.LicenseFactory().by_license_code(self.pieces[0],
                                                           version,
                                                           jurisdiction)

    @property
    def conditions(self):
        """Return a sequence of mappings defining the conditions defined by
        this license."""

        attrs = []

        for lic in self.license.code.split('-'):

            # Go through the chars and build up the HTML and such
            char_title = translate ('char.%s_title' % lic,
                                    domain='icommons')
            char_brief = translate ('char.%s_brief' % lic,
                                    domain='icommons')

            icon_name = lic
            predicate = 'cc:requires'
            object = 'http://creativecommons.org/ns#Attribution'

            if lic == 'nc':
              predicate = 'cc:prohibits'
              object = 'http://creativecommons.org/ns#CommercialUse'
              if self.license.jurisdiction == 'jp':
                 icon_name = '%s-jp' % icon_name
              elif self.license.jurisdiction in ('fr', 'es', 'nl', 'at', 'fi', 'be', 'it'):
                 icon_name = '%s-eu' % icon_name
            elif lic == 'sa':
              object = 'http://creativecommons.org/ns#ShareAlike'
              if self.license.version == 3.0 and self.license.code == 'by-sa':
                char_brief = translate ('char.sa_bysa30_brief',
                                        domain='icommons')
            elif lic == 'nd':
              predicate = ''
              object = ''

            attrs.append({'char_title':char_title,
                          'char_brief':char_brief,
                          'icon_name':icon_name,
                          'char_code':lic,
                          'predicate':predicate,
                          'object':object,
                     })

        # XXX cache me!
        return attrs
        
    def traverse(self, name):

        if len(self.pieces) > 3:
            # no cases call for more than three steps of traversal
            return None

        # XXX handle deed.de, etc
        
        if name not in self.TARGET_NAMES:
            return BrowserLicense(self, self.pieces + [name])


class LicenseDeed(grok.View):
    grok.context(BrowserLicense)
    grok.name('index')
    grok.template('deed')

    def update(self):
        """Prepare to render the deed."""

        # redirect if we don't have a trailing slash
        if self.request['PATH_INFO'][-1] != '/':
            if self.request.get('QUERY_STRING', ''):
                target = '%s/?%s' % (self.request['PATH_INFO'],
                                     self.request['QUERY_STIRNG'])
            else:
                target = '%s/' % self.request['PATH_INFO']
                
            return self.request.response.redirect(target)

        # make sure we've traversed to a valid license version
        try:
            self.context.license
        except LicenseException, e:
            raise NotFound(self.context, self.request['REQUEST_URI'],
                           self.request)


        # make sure we've extracted the locale from the request querystring
        self.request.setupLocale()

    @property
    def is_rtl(self):
        """Return 'rtl' if the request locale is represented right-to-left;
        otherwise return an empty string."""

        if self.request.locale.orientation.characters == u'right-to-left':
            return 'rtl'

        return ''

    @property
    def is_rtl_align(self):
        """Return the appropriate alignment for the request locale:
        'right' or 'left'."""

        return self.request.locale.orientation.characters.split('-')[0]

    @property
    def active_languages(self):

        # XXX
        return []

    
    @property
    def color(self):

        # XXX
        return 'green'
    

class LicenseRdf(grok.View):
    grok.context(BrowserLicense)
    grok.name('rdf')

    def render(self):
        return "rdf goes here"
                 
    
class LicenseCatalog(grok.Application, grok.Container):
    implements(interfaces.ILicenseCatalog)

    def traverse(self, code):

        return BrowserLicense(self, [code])

class Index(grok.View):
    grok.context(LicenseCatalog)
    grok.template('licenses-index')


