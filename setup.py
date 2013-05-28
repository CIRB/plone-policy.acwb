from setuptools import setup, find_packages

version = '1.2'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='policy.acwb',
      version=version,
      description="'policy of AC Watermael-boitsfort'",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.ckeditor',
          'cirb.footersitemap',
          'collective.quickupload',
          'Products.PloneFormGen',
          'qi.portlet.TagClouds',
          'collective.easyslider',
          'Solgema.fullcalendar',
          'collective.gallery',
          'quintagroup.analytics',
          'collective.recaptcha',
          'collective.anysurfer',
          'collective.portlet.videoanysurfer',
          'collective.videoanysurfer',
          'collective.linguafaq',
          'plonetheme.acwb',
          'collective.languagemovefolders',
          'cirb.zopemonitoring',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
