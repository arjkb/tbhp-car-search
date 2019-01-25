from flask import Flask, render_template
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    # return 'at root'
    return render_template('index.html', sample_text="")

@app.route('/results/')
def results():
    r = {'Ford Fiesta (Automatic) : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/111055-ford-fiesta-automatic-test-drive-review.html', 'Fiat Avventura : Test Drive & Review': 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/156762-fiat-avventura-test-drive-review.html', '2014 Skoda Yeti Facelift : A Close Look': 'https://www.team-bhp.com/forum/indian-car-scene/155485-2014-skoda-yeti-facelift-close-look.html', 'Mitsubishi Lancer EVO X : Test Drive & Review': 'https://www.team-bhp.com/forum/official-new-car-reviews/95116-mitsubishi-lancer-evo-x-test-drive-review.html'}
    # r = {'a': 'apple', 'b':'ball'}
    return render_template('index.html', sample_text="Foo", reviews=r)

# if __name__ == "__main__":
#     app.debug = True
#     app.run()