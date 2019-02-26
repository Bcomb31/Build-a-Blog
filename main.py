from flask import Flask, request, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:get-it-done@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def is_valid(self):
        '''
        self check
        '''
        if self.title and self.body and self.created:
            return True
        else:
            return False




@app.route('/')
def index():
   
   return redirect("/blog")

@app.route('/blog')
def display_blog_entries():

    if (entry_id):
        entry = Blog.query.get(entry_id)
        return render_template('single_blog.html', title="Add a Blog Entry", entry=entry)

    if (sort=="newest"):
        all_entries = Blog.query.order_by(Blog.created.desc()).all()
    else:
        all_entries = Blog.query.all()   
    return render_template('blog.html', title="All Entries", all_entries=all_entries)

@app.route('/newpost', methods=['GET', 'POST'])
def new_post():
    
    if request.method == 'POST':
        new_title = request.form['title']
        new_body = request.form['body']
        new_post = Blog(title, body)

        if post.is_valid():
            db.session.add(new_post)
            db.session.commit()
            url = "/blog?id=" + str(new_post.id)
            return redirect(url)
        else:
            flash("Please check your entry for errors. Both a title and a body are required.")
            return render_template('newpost.html',
                title="Add new blog entry",
                new_title=new_title,
                new_body=new_body)    

    else: # GET request
        return render_template('newpost.html', title="Create new blog entry")

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

if __name__ == '__main__':
    app.run()