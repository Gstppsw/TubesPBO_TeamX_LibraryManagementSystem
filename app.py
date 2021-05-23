from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__, template_folder='template')
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tempat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def __init__ (self, name):
        self.name = name

@app.route('/')
def Index():
    all_data = Tempat.query.all()
    data = Item.query.all()
    dat = Subscriber.query.all()
    da = Borrow.query.all()
    return render_template("index.html", library = all_data, item = data, subscriber = dat, borrow = da)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']

        my_data = Tempat(name)
        db.session.add(my_data)
        db.session.commit()

        flash("Library Added")

        return redirect(url_for('Index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Tempat.query.get(request.form.get('id'))

        my_data.name = request.form['name']

        db.session.commit()

        flash("Library Updated")

        return redirect(url_for('Index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Tempat.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Library Deleted")

    return redirect(url_for('Index'))


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(100))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    production = db.Column(db.String(100))
    copies = db.Column(db.String(100))

    def __init__ (self, category, title, author, publisher, production, copies):
        self.category = category
        self.title = title
        self.author = author
        self.publisher = publisher
        self.production = production
        self.copies = copies

@app.route('/insertitem', methods = ['POST', 'GET'])
def insertitem():
    if request.method == 'POST':

        category = request.form['category']
        title = request.form['title']
        author = request.form['author']
        publisher = request.form['publisher']
        production = request.form['production']
        copies = request.form['copies']

        my_data = Item(category, title, author, publisher, production, copies)
        db.session.add(my_data)
        db.session.commit()

        flash("Item Added")

        return redirect(url_for('Index'))

@app.route('/updateitem', methods = ['GET', 'POST'])
def updateitem():
    if request.method == 'POST':
        my_data = Item.query.get(request.form.get('item_id'))

        my_data.category = request.form['category']
        my_data.title = request.form['title']
        my_data.author = request.form['author']
        my_data.publisher = request.form['publisher']
        my_data.production = request.form['production']
        my_data.copies = request.form['copies']


        db.session.commit()

        flash("Item Updated")

        return redirect(url_for('Index'))


@app.route('/deleteitem/<item_id>/', methods=['GET', 'POST'])
def deleteitem(item_id):
    my_data = Item.query.get(item_id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Item Deleted")

    return redirect(url_for('Index'))

class Subscriber(db.Model):
    subscriber_id = db.Column(db.Integer, primary_key = True)
    typ = db.Column(db.String(100))
    name_subscriber = db.Column(db.String(100))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__ (self, typ, name_subscriber, address, phone, email):
        self.typ = typ
        self.name_subscriber = name_subscriber
        self.address = address
        self.phone = phone
        self.email = email

@app.route('/insertsubscriber', methods = ['POST', 'GET'])
def insertsubscriber():
    if request.method == 'POST':

        typ = request.form['typ']
        name_subscriber = request.form['name_subscriber']
        address = request.form['address']
        phone = request.form['phone']
        email = request.form['email']

        my_data = Subscriber(typ, name_subscriber, address, phone, email)
        db.session.add(my_data)
        db.session.commit()

        flash("Subscriber Added")

        return redirect(url_for('Index'))

@app.route('/updatesubscriber', methods = ['GET', 'POST'])
def updatesubscriber():
    if request.method == 'POST':
        my_data = Subscriber.query.get(request.form.get('subscriber_id'))

        my_data.typ = request.form['typ']
        my_data.name_subscriber = request.form['name_subscriber']
        my_data.address = request.form['address']
        my_data.phone = request.form['phone']
        my_data.email = request.form['email']

        db.session.commit()

        flash("Subscriber Updated")

        return redirect(url_for('Index'))

@app.route('/deletesubscriber/<subscriber_id>/', methods=['GET', 'POST'])
def deletesubscriber(subscriber_id):
    my_data = Subscriber.query.get(subscriber_id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Subscriber Deleted")

    return redirect(url_for('Index'))

class Borrow(db.Model):
    sub_id = db.Column(db.Integer, primary_key = True)
    borrowdate = db.Column(db.String(100))
    itemid = db.Column(db.String(100))
    returndate = db.Column(db.String(100))
    fee = db.Column(db.String(100))

    def __init__ (self, borrowdate, itemid, returndate, fee):
        self.borrowdate =borrowdate
        self.itemid = itemid
        self.returndate = returndate
        self.fee = fee

@app.route('/insertborrow', methods = ['POST', 'GET'])
def insertborrow():
    if request.method == 'POST':

        borrowdate = request.form['borrowdate']
        itemid = request.form['itemid']
        returndate = request.form['returndate']
        fee = request.form['fee']

        my_data = Borrow(borrowdate, itemid, returndate, fee)
        db.session.add(my_data)
        db.session.commit()

        flash("Borrow Added")

        return redirect(url_for('Index'))

@app.route('/updateborrow', methods = ['GET', 'POST'])
def updateborrow():
    if request.method == 'POST':
        my_data = Borrow.query.get(request.form.get('sub_id'))

        my_data.borrowdate = request.form['borrowdate']
        my_data.itemid = request.form['itemid']
        my_data.returndate = request.form['returndate']
        my_data.fee = request.form['fee']

        db.session.commit()

        flash("Borrow Updated")

        return redirect(url_for('Index'))

@app.route('/deleteborrow/<sub_id>/', methods=['GET', 'POST'])
def deleteborrow(sub_id):
    my_data = Borrow.query.get(sub_id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Borrow Deleted")

    return redirect(url_for('Index'))



if __name__ == "__main__" :
    app.run(debug=True)
