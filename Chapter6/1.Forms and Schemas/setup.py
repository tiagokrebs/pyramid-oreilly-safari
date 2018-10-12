from setuptools import setup

# adicionei dform com versao >= etc
# dform 2 tem uma integracao com bootstrap
requires = [
    'pyramid',
    'pyramid_jinja2',
    'deform>=2.0a2'
]
setup(name='mysite',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = mysite:main
      """
      )
