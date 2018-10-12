from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'deform>=2.0a2',
    'pyramid_sqlalchemy',
    'pyramid_tm'
]

# adicionado entry_point para inicializao do bd
# script é gerado automaticamente com basenos modelos
# e eh capaz de inserir dados exemplo como no modelo ToDo desse projeto
# para inicializar o banco basta executar o script gerado apontando para o arquvo de configuracao
# $ initialize_bd development.ini
setup(name='mysite',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = mysite:main
      [console_scripts]
      initialize_db = mysite.scripts.initialize_db:main
      """
      )
