from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicyAcwb(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.acwb
        xmlconfig.file('configure.zcml',
                       policy.acwb,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.acwb:default')

POLICY_ACWB_FIXTURE = PolicyAcwb()
POLICY_ACWB_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_ACWB_FIXTURE, ),
                       name="PolicyAcwb:Integration")