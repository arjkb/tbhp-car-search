from flask import Flask, render_template
import tbhpscraper

app = Flask(__name__, static_url_path='')

baselink_oncr = 'https://www.team-bhp.com/forum/official-new-car-reviews/'
baselink_tdio = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/'
baselink_ltr = 'https://www.team-bhp.com/forum/long-term-ownership-reviews/'

# reviews_oncr = tbhpscraper.get_reviews(baselink_oncr)
# reviews_tdio = tbhpscraper.get_reviews(baselink_tdio)
# reviews_ltr = tbhpscraper.get_reviews(baselink_ltr)

reviews_oncr = {
    'Volkswagen Polo 1.2L GT TSI : Official Review ': 'https://www.team-bhp.com/forum/official-new-car-reviews/135550-volkswagen-polo-1-2l-gt-tsi-official-review.html',
    'Toyota Innova Crysta': 'https://www.team-bhp.com/forum/official-new-car-reviews/177320-toyota-innova-crysta-official-review.html'
}

reviews_tdio = {
    'My W222 Mercedes S-Class (S350 CDI)': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/165052-my-w222-mercedes-s-class-s350-cdi.html',
    'Driven: Volvo V90 Cross Country': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/190414-driven-volvo-v90-cross-country.html'
}

reviews_ltr = {
    'BMW 530d M-Sport (F10) : My pre-worshipped beast ': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/167550-bmw-530d-m-sport-f10-my-pre-worshipped-beast.html',
    'Hyundai Creta 1.6L CRDi SX(O) - An Ownership Log - Update: 50,000 km up': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/196858-hyundai-creta-1-6l-crdi-sx-o-ownership-log-update-50-000-km-up.html'
}

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
                                    tdio=reviews_tdio,
                                    ltr=reviews_ltr)

@app.route('/search/<word>')
def search(word):
    r_searched_oncr = tbhpscraper.search(word, reviews_oncr)
    r_searched_tdio = tbhpscraper.search(word, reviews_tdio)
    r_searched_ltr = tbhpscraper.search(word, reviews_ltr)

    return render_template('index.html', sample_text="Search", oncr=r_searched_oncr, tdio=r_searched_tdio, ltr=r_searched_ltr)
