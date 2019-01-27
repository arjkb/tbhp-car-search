from flask import Flask, render_template
import tbhpscraper

app = Flask(__name__, static_url_path='')

baselink_oncr = 'https://www.team-bhp.com/forum/official-new-car-reviews/'
baselink_tdio = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/'

reviews_oncr = tbhpscraper.get_reviews(baselink_oncr)
reviews_tdio = tbhpscraper.get_reviews(baselink_tdio)

@app.route('/')
def root():
    # return 'at root'
    return render_template('index.html', sample_text="")

@app.route('/results/')
def results():
    # r = {'Ford Fiesta (Automatic) : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/111055-ford-fiesta-automatic-test-drive-review.html', 'Fiat Avventura : Test Drive & Review': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/156762-fiat-avventura-test-drive-review.html', '2014 Skoda Yeti Facelift : A Close Look': 'https://www.team-bhp.com/forum/indian-car-scene/155485-2014-skoda-yeti-facelift-close-look.html', 'Mitsubishi Lancer EVO X : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/95116-mitsubishi-lancer-evo-x-test-drive-review.html'}
    # r = tbhpscraper.get_reviews()
    return render_template('index.html', sample_text="Foo", 
                                    oncr=reviews_oncr,
                                    tdio=reviews_tdio)

@app.route('/search/<word>')
def search(word):
    r_searched_oncr = tbhpscraper.search(word, reviews_oncr)
    r_searched_tdio = tbhpscraper.search(word, reviews_tdio)

    return render_template('index.html', sample_text="Search", oncr=r_searched_oncr, tdio=r_searched_tdio)
