from setuptools import setup

# informamos outros pacotes que sao dependencias
requires = [
    'pyramid',
    'pyramid_jinja2'
]
setup(name='mysite', # damos um nome ao projeto
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = mysite:main
      """
      )

# entry_point é um lugar para esse pacote linkar ou outros pacotes plug in
# esse entry_point liga com a aplicação wsgi que fica em mysite