from flask import Flask, request, render_template, redirect, url_for
from model import db, Contact


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dheeraj_kb@localhost/contacts_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/')
    def index():
        contacts = Contact.query.all()
        return render_template('list_contacts.html', contacts=contacts)

    @app.route('/contact', methods=['GET', 'POST'])
    @app.route('/contact/<int:id>', methods=['GET', 'POST'])
    def contact(id=None):
        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']
            address = request.form['address']
            phone_number = request.form['phone_number']
            if id:
                contact = Contact.query.filter_by(id=id).first()
                contact.name = name
                contact.age = age
                contact.address = address
                contact.phone_number = phone_number
            else:
                contact = Contact(name=name, age=age, address=address, phone_number=phone_number)
                db.session.add(contact)
            db.session.commit()
            return redirect(url_for('index'))
        contact = Contact.query.filter_by(id=id).first() if id else None
        return render_template('contact_form.html', contact=contact)

    @app.route('/delete/<int:id>')
    def delete_contact(id):
        contact = Contact.query.filter_by(id=id).first()
        db.session.delete(contact)
        db.session.commit()
        return redirect(url_for('index'))

    return app

