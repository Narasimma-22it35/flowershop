from flask import Flask, render_template

app = Flask(__name__)

flowers = [
    {"name":"Rose Bouquet","price":"₹499","image":"https://images.unsplash.com/photo-1518709268805-4e9042af2176"},
    {"name":"Sunflower","price":"₹399","image":"https://images.unsplash.com/photo-1470509037663-253afd7f0f51"},
    {"name":"Lily","price":"₹599","image":"https://images.unsplash.com/photo-1468327768560-75b778cbb551"},
    {"name":"Tulip","price":"₹699","image":"https://images.unsplash.com/photo-1526045612212-70caf35c14df"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flowers')
def flowers_page():
    return render_template('flowers.html', flowers=flowers)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)