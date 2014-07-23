from twisted.application.service import IServiceMaker
from twisted.application.strports import service
from twisted.plugin import IPlugin
from twisted.python.usage import Options
from zope.interface import implements


class ProxyOptions(Options):

    optParameters = [
        ["control", "c", "tcp:5500", "Endpoint for the control socket"],
    ]


class ProxyServiceMaker(object):

    implements(IPlugin, IServiceMaker)

    tapname = "vncap"
    description = "Specialized VNC proxy with authentication"
    options = ProxyOptions

    def makeService(self, options):
        from vncap.control import ControlFactory
        return service(options["control"], ControlFactory())


servicemaker = ProxyServiceMaker()
