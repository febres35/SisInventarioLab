from . import models

from werkzeug.security import generate_password_hash

def init_DB():

    if not (models.User.query.filter_by(username='admin').first()):
        models.User.create_element('admin', generate_password_hash('admin'))


    if not models.Unit.query.filter_by(id=1).first():
        unit = models.Unit.create_elemet('mL')
        unit1 = models.Unit.create_elemet('piezas')

        if not models.Article.query.filter_by(id=1).first():
            articles = [['filtro', unit1],
                       ['ws2', unit],
                       ['colectores', unit1],
                       ['ependrorf05', unit1],
                       ['ependrorf02', unit1],
                       ['ependrorf2', unit1],
                       ['puntas10', unit1],
                       ['puntas1000', unit1],
                       ['amplificacion', unit],
                       ['ws1', unit],
                       ['ssb', unit],
                       ['eb', unit],
                       ['hisopos', unit1],
                        ['amplificacion24', unit1]]

            for article in articles:
                models.Article.create_elemet(name=article[0], description="", unit_id=article[1])

   #else: # encaso de un nuevo ingreso.
        #unit1 = models.Unit.query.filter_by(id=2).first()
       #articles=[['amplificacion24', unit1]]
        #for article in articles:
            #models.Article.create_elemet(name=article[0], description="", unit_id=article[1])

    if (models.Unit.query.filter_by(unitName='mL').first()):
        unit = models.Unit.query.filter_by(unitName='mL').first()
        unit1 = models.Unit.query.filter_by(unitName='piezas').first()

        if not models.Article.query.filter_by(id=1).first():
            articles = [['filtro', unit1],
                       ['ws2', unit],
                       ['colectores', unit1],
                       ['ependrorf05', unit1],
                       ['ependrorf02', unit1],
                       ['ependrorf2', unit1],
                       ['puntas10', unit1],
                       ['puntas1000', unit1],
                       ['amplificacion', unit],
                       ['ws1', unit],
                       ['ssb', unit],
                       ['eb', unit],
                       ['hisopos', unit1],
                        ['amplificacion24', unit]]

            for article in articles:
                    models.Article.create_elemet(name=article[0], description="", unit_id=article[1])


        articles = ['filtro',
                    'ws2',
                    'colectores',
                    'ependrorf05',
                    'ependrorf02',
                    'ependrorf2',
                    'puntas10',
                    'puntas1000',
                    'amplificacion',
                    'ws1',
                    'ssb',
                    'eb',
                    'hisopos',
                    'amplificacion24']
        for article in articles:
            a = models.Article.query.filter_by(name=article).first()

            if not models.Stock.query.filter_by(article_id=a.id).first():
                models.Stock.create_elemt(article_id=a, amount=0)



