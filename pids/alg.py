#determining a system for an intelligent algorith
#then add to app.py 
#this file exists to prevent merge conflicts with app.py


@app.route("/form", methods = ['GET', 'POST'])
def form():
	form = QuoteForm()
	if request.method == 'POST':
		quote = Passage(content = form.content, title = form.title, author = form.author)
		db.session.add(quote)
		db.session.commit()
		return render_template('form.html', form = form)
	elif request.method == 'GET':
		return render_template('form.html', form = form)