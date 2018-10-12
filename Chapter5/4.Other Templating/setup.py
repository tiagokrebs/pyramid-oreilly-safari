from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_chameleon'
]
setup(name='mysite',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = mysite:main
      """
      )
