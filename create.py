from pids.__init__ import app, db, Passage
import random

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eu quam eu erat feugiat luctus nec vel ligula. Aenean sagittis metus ut urna facilisis vulputate. Fusce tempus condimentum aliquet. Nulla ante enim, pharetra quis consequat non, dapibus fermentum arcu. Proin eget turpis vel neque fermentum sodales. Morbi egestas arcu non erat molestie, a volutpat risus facilisis. Nulla enim turpis, mattis blandit maximus eget, ultricies vel arcu. Nunc id interdum turpis. Vestibulum rhoncus nibh non consequat pellentesque. Mauris cursus arcu eget lectus tempus laoreet. Sed ac rutrum lorem. Integer in tellus dapibus, venenatis nibh eget, facilisis libero. Fusce eget porta orci, id maximus mauris. Aenean placerat scelerisque sapien in cursus. Fusce et dolor posuere, laoreet est ut, laoreet odio. Aenean vehicula nulla lacus, ac lobortis nisl varius ut. Aliquam fermentum a elit sit amet ullamcorper. Nunc tellus lacus, pharetra vel nibh quis, rhoncus semper orci. Ut rhoncus viverra ipsum quis mattis. Maecenas vulputate dui ante, eu elementum tellus commodo sit amet. Phasellus nec dignissim mauris, vitae iaculis elit. Mauris volutpat lacinia diam blandit volutpat. Donec bibendum imperdiet nulla id placerat. Sed sapien turpis, venenatis nec vestibulum quis, elementum sit amet nunc. Duis mollis placerat sollicitudin. Suspendisse eget erat in eros tincidunt imperdiet in id nisl. Mauris a risus nec massa mattis consectetur. Praesent pretium tempus nibh eget rhoncus. Morbi porttitor dolor sit amet urna lobortis luctus. Donec blandit diam ante, sit amet ultricies quam tincidunt placerat. Cras venenatis hendrerit sapien non dapibus. Cras faucibus lectus non justo porta luctus. Curabitur vel nulla eget purus elementum bibendum at eu ex. In in pulvinar risus. Fusce mi metus, mattis vel consequat ultricies, commodo vel massa. Suspendisse non neque id lorem semper suscipit non sed lacus. Aenean vestibulum ex sit amet sagittis rutrum. Aenean porttitor scelerisque laoreet. Cras at placerat tellus. Sed dictum accumsan justo facilisis auctor. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum sit amet lectus vitae ipsum condimentum accumsan nec sit amet magna. Proin eros quam, congue et aliquam at, suscipit non ipsum. Aliquam erat volutpat. Duis lorem dolor, placerat a justo in, gravida egestas magna. Phasellus auctor ante ipsum, ut scelerisque purus vestibulum nec. In hac habitasse platea dictumst. Proin sit amet turpis felis. Fusce id sem pulvinar, porttitor mauris et, efficitur ligula. Aliquam posuere, magna eget egestas scelerisque, dui tellus suscipit neque, ut dignissim nisi orci quis nunc. Sed vehicula tellus justo, sed interdum velit dignissim a. Donec sed metus sed orci fringilla euismod. Aliquam sem arcu, accumsan ac semper ut, porttitor in diam. Phasellus neque lectus, imperdiet non sagittis ac, luctus ut velit. Fusce varius ultricies tempor. Ut quis fringilla ipsum. Maecenas at mauris id odio mattis consectetur."

authors = [ "Homer", "Virgil", "Dante", "Virginia Woolf", "Herodotus", "Thucydides", "Shakespeare", "Sophocles", "Ovid", "Augustine", "Michel de Montaigne", "Dostoevsky"]

titles = [ "The Iliad", "The Odyssey", "Oresteia", "Oedipus Rex", "The Medea", "Genesis", "Lysistrata", "The Histories", "The Symposium", "Job", "Luke/John", "The Aeneid", "Confessions", "The Divine Comedy", "Pride and Prejudice", "Crime and Punishment"]

categories = [ "Greek Tragedy", "Play", "Epic", "History", "Roman", "Novel", "Bible" ]

def split(text):
	words = text.split()
	return words

def generator(text):
	author = authors[random.randint(0, len(authors) - 1)]
	content = ""
	count = random.randint(0, len(text))
	for i in range(count):
		content = content + " " + text[i]
	title = titles[random.randint(0, len(titles)  - 1)]
	class_type = random.randint(1,2)
	category = categories[random.randint(0, len(categories) - 1)]
	return Passage(quote=content, title=title, author=author, submitter="auto-create", class_type=class_type, category=category)

def generatePassages():
		for i in range(100):
			passage = generator(split(lorem))
			db.session.add(passage)
		db.session.commit()

with app.app_context():
    db.create_all()
    generatePassages()