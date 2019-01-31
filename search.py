from flask import Flask, render_template, request
import tbhpscraper

app = Flask(__name__, static_url_path='')

baselink_oncr = 'https://www.team-bhp.com/forum/official-new-car-reviews/'
baselink_tdio = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/'
baselink_ltr = 'https://www.team-bhp.com/forum/long-term-ownership-reviews/'

reviews_oncr = tbhpscraper.get_reviews(baselink_oncr)
reviews_tdio = tbhpscraper.get_reviews(baselink_tdio)
reviews_ltr = tbhpscraper.get_reviews(baselink_ltr)

@app.route('/')
def root():
    # return 'at root'
    return render_template('index.html', sample_text="")

@app.route('/reviews/')
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
