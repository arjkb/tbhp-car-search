from flask import Flask, render_template, request
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
    'Toyota Innova Crysta': 'https://www.team-bhp.com/forum/official-new-car-reviews/177320-toyota-innova-crysta-official-review.html',
    'Mahindra Marazzo : Official Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/203475-mahindra-marazzo-official-review.html',
    'Volkswagen Vento : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/94990-volkswagen-vento-test-drive-review.html',
    'Maruti WagonR : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/80144-maruti-wagonr-test-drive-review.html',
    'Ford EcoSport S (1.0L EcoBoost) : Official Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/201440-ford-ecosport-s-1-0l-ecoboost-official-review.html',
    'Fiat Linea T-Jet : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/90735-fiat-linea-t-jet-test-drive-review.html',
    'Tata Hexa : Official Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/181903-tata-hexa-official-review.html',
}

reviews_tdio = {
    'My W222 Mercedes S-Class (S350 CDI)': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/165052-my-w222-mercedes-s-class-s350-cdi.html',
    'Driven: Volvo V90 Cross Country': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/190414-driven-volvo-v90-cross-country.html',
    'My new 2.0L CR TDi Jetta Comfortline - 30,000kms *UPDATE*': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/81190-my-new-2-0l-cr-tdi-jetta-comfortline-30-000kms-update.html', 
    'My 2018 Hyundai Grand i10 Asta Petrol': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/199954-my-2018-hyundai-grand-i10-asta-petrol.html',
    "Lexus ES300h - Owner's Review. EDIT: 20,000 km update": 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/186121-lexus-es300h-owners-review-edit-20-000-km-update.html',
    'Driven: Volvo S90': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/181447-driven-volvo-s90.html',
    'Got a new Gypsy': 'https://www.team-bhp.com/forum/showthread.php?t=204910',
    'Silver bullet - My Skoda Octavia 1.8 TSI L&K': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/197740-silver-bullet-my-skoda-octavia-1-8-tsi-l-k.html'
}

reviews_ltr = {
    'BMW 530d M-Sport (F10) : My pre-worshipped beast ': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/167550-bmw-530d-m-sport-f10-my-pre-worshipped-beast.html',
    'Hyundai Creta 1.6L CRDi SX(O) - An Ownership Log - Update: 50,000 km up': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/196858-hyundai-creta-1-6l-crdi-sx-o-ownership-log-update-50-000-km-up.html',
    'Soldier of Fortune: Wanderings with a Trusty Toyota Fortuner - 100,000 kms up!': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/89533-soldier-fortune-wanderings-trusty-toyota-fortuner-100-000-kms-up.html',
    "Ode to Goldie - My '99 Maruti 800 DX": 'https://www.team-bhp.com/forum/long-term-ownership-reviews/141986-ode-goldie-my-99-maruti-800-dx.html',
    'Tata Safari 2.2 VTT - Black Beast - 8.5 years and 100,000 kms up!': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/64167-tata-safari-2-2-vtt-black-beast-8-5-years-100-000-kms-up.html',
    'This Ford is my IKON - 89,000 km and 9 years completed': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/74132-ford-my-ikon-89-000-km-9-years-completed.html',
    'Swift Diesel, Saga continues. The DIESEL experience! Part II 72k kms Update Page 182. Now SOLD!': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/30745-swift-diesel-saga-continues-diesel-experience-part-ii-72k-kms-update-page-182-now-sold.html',
    '400,000 km on my 2006 Hyundai Elantra CRDi - And going strong!': 'https://www.team-bhp.com/forum/long-term-ownership-reviews/195266-400-000-km-my-2006-hyundai-elantra-crdi-going-strong.html'
}


@app.route('/')
def reviews():
    # r = {'Ford Fiesta (Automatic) : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/111055-ford-fiesta-automatic-test-drive-review.html', 'Fiat Avventura : Test Drive & Review': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/156762-fiat-avventura-test-drive-review.html', '2014 Skoda Yeti Facelift : A Close Look': 'https://www.team-bhp.com/forum/indian-car-scene/155485-2014-skoda-yeti-facelift-close-look.html', 'Mitsubishi Lancer EVO X : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/95116-mitsubishi-lancer-evo-x-test-drive-review.html'}
    # r = tbhpscraper.get_reviews()
    reviews = [
        { 'title': 'Official New Car Reviews', 'data': reviews_oncr},
        { 'title': 'Test Drives & Initial Ownership Reports', 'data': reviews_tdio},
        { 'title': 'Long Term Reviews', 'data': reviews_ltr}
    ]
    return render_template('reviews.html', sample_text="All Car List", reviews=reviews)

@app.route('/search', methods=["GET"])
def search():
    word = str(request.args.get("car"))
    r_searched_oncr = tbhpscraper.search(word, reviews_oncr)
    r_searched_tdio = tbhpscraper.search(word, reviews_tdio)
    r_searched_ltr = tbhpscraper.search(word, reviews_ltr)

    reviews = [
        { 'title': 'Official New Car Reviews', 'data': r_searched_oncr},
        { 'title': 'Test Drives & Initial Ownership Reports', 'data': r_searched_tdio},
        { 'title': 'Long Term Reviews', 'data': r_searched_ltr}
    ]
    return render_template('reviews.html', sample_text='Search results: "{}"'.format(word), reviews=reviews)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()