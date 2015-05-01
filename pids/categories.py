lithum_categories = {
			"fall": 
			{
				"Greek Tragedy": ["The Medea", "Oresteia", "Oedipus the King"],
		  		"Play": ["The Medea", "Oresteia", "Oedipus the King", "King Lear"],
		  		"Epic": ["Aeneid", "Odyssey", "Iliad"],
		  		"History" : ["The Histories", "History of the Peloponnesian War"],
		  		"Bible" : ["Luke", "John", "Job", "Exodus", "Genesis"], 
		  		"Roman" : ["The Golden Ass", "Metamorphoses", "Aeneid", "Confessions"], 
		  		"Novel" : ["Don Quixote", "Pride and Prejudice", "To the Lighthouse", "The Golden Ass"]
			},
			"spring":
		    {
		    	"Ancient": ["The Aeneid", "Metamorphoses"],
				"Existential": ["Faust", "Crime and Punishment"],
				"Medieval": ["Confessions", "Don Quixote", "King Lear", "The Divine Comedy"],
				"Novel": ["Essays", "Pride and Prejudice", "To the Lighthouse" ],
			}
		 }

lithum_titles = { "fall": [ ("The Iliad", "The Iliad"),
							("The Odyssey", "The Odyssey"),
							("Oresteia", "Oresteia"),
							("Oedipus Rex", "Oedipus Rex"),
							("The Medea", "The Medea"),
							("The Histories", "The Histories"),
							("History of the Peloponnesian War", "History of the Peloponnesian War"),
							("Lysistrata", "Lysistrata"),
							("The Symposium", "The Syposium"),
							("Genesis", "Genesis"),
							("Job", "Job"),
							("Luke/John", "Luke/John") ],
				  "spring": [("The Aeneid", "The Aeneid"),
				  			 ("Metamorphoses", "Metamorphoses"),
				  			 ("Confessions", "Confessions"),
				  			 ("The Divine Comedy", "The Divine Comedy"),
				  			 ("Essays", "Essays"),
				  			 ("King Lear", "King Lear"),
				  			 ("Don Quixote", "Don Quixote"),
				  			 ("Faust", "Faust"),
				  			 ("Pride and Prejudice", "Pride and Prejudice"),
				  			 ("Crime and Punishment", "Crime and Punishment")
				  			]		
				}

lithum_authors_categories = {
					"The Iliad": {"author": "Homer", "category": "Epic"},
					"The Odyssey": {"author": "Homer", "category": "Epic"},
					"Oresteia": {"author": "Aeschylus", "category": "Greek Tragedy"},
					"Oedipus Rex": {"author": "Sophocles", "category": "Greek Tragedy"},
					"The Medea": {"author": "Euripides", "category": "Greek Tragedy"},
					"The Histories": {"author": "Herodotus", "category": ""},
					"History of the Peloponnesian War": {"author": "Thucydides", "category": ""},
					"Lysistrata": {"author": "Aristophanes", "category": ""},
					"The Symposium": {"author": "Plato", "category": ""},
					"Genesis": {"author": "Unknown", "category": ""},
					"Job": {"author": "Unknown", "category": ""},
					"Luke/John": {"author": "Unknown", "category": ""},
					"The Aeneid": {"author": "Virgil", "category": "Epic"},
					"Metamorphoses": {"author": "Ovid", "category": ""},
				  	"Confessions": {"author": "St. Augustine", "category": ""},
				  	"The Divine Comedy": {"author": "Dante Alighieri", "category": ""},
				  	"Essays": {"author": "Michel de Montaigne", "category": ""},
				  	"King Lear": {"author": "William Shakespeare", "category": ""},
				  	"Don Quixote": {"author": "Miguel de Cervantes", "category": ""},
				  	"Faust": {"author": "Goethe", "category": ""},
				  	"Pride and Prejudice": {"author": "Jane Austen", "category": "Novel"},
				  	"Crime and Punishment": {"author": "Fyodor Dostoyevsky", "category": "Novel"}
				  }

cc_titles = { "spring": [ ("The Writings of David Hume", "The Writings of David Hume"),
						("Discourse on Inequality and Social Contract", "Discourse on Inequality and Social Contract"),
						("Wealth of Nations", "Wealth of Nations"),
						("Groundwork for the Metaphysics of Morals", "Groundwork for the Metaphysics of Morals"),
						("American Revolution and Founding Texts", "American Revolution and Founding Texts"),
						("Reflections on the Revolutions in France", "Reflections on the Revolutions in France"),
						("The French Revolution", "The French Revolution"),
						("A Vindication of the Rights of Woman", "A Vindication of the Rights of Woman"),
						("Democracy in America", "Democracy in America"),
						("On Liberty and Other Essays", "On Liberty and Other Essays"),
						("Selections from the Marx-Engels Reader", "Selections from the Marx-Engels Reader"),
						("On the Genealogy of Morals", "On the Genealogy of Morals"),
						("The Writings of Charles Darwin", "The Writings of Charles Darwin"),
						("The Souls of Black Folk", "The Souls of Black Folk"),
						("The Writings of Sigmund Freud", "The Writings of Sigund Freud"),
						("Three Guineas", "Three Guineas")
			  		    ],
			  "fall": [ ("Republic", "Republic"),
			  			("Nicomachean Ethics", "Nicomachean Ethics"),
			  			("Politics", "Politics"),
			  			("The Hebrew Bible", "The Hebrew Bible"),
			  			("Roman & Hellenistic Thought", "Roman & Hellenistic Thought"),
			  			("New Testament", "New Testament"),
			  			("City of God", "City of God"),
			  			("The Qur'an", "The Qur'an"),
			  			("Medieval Philosophy"),
			  			("The Discourses", "The Discourses"),
			  			("The Prince", "The Prince"),
			  			("The Protestant Reformation", "The Protestant Reformation"),
			  			("The Scientific Revolution", "The Scientific Revolution"),
			  			("Discourse on Method and Meditations on First Philosophy", "Discourse on Method and Meditations on First Philosophy"),
			  			("New World Writings", "New World Writings"),
			  			("Leviathan", "Leviathan"),
			  			("Second Treatise", "Second Treatise")
			  		  ]
			}

lithum = { "fall": 
			{
				"Ancient" : ["Republic", "Nicomachean Ethics", "Politics", "Roman & Hellenistic Thought", "The Writings of David Hume" ],
				"Medieval" : ["Medieval Philosophy", "City of God"],
				"Biblical" : ["New Testament", "The Qur'an", "The Hebrew Bible"],
				"Philosophical": ["Second Treatise", "Leviathan", "New World Writings", "Discourse on Method and Meditations on First Philosophy"],
				"Renaissance": ["The Prince", "The Scientific Revolution", "The Discourses", "The Protestant Reformation"],
			}
		   "spring":
		    {
		    	"Enlightenment": ["Discourse on Inequality and Social Contract", "Wealth of Nations", "Groundwork for the Metaphysics of Morals" ],
		    	"Freedom": ["Democracy in America", "On Liberty and Other Essays"],
		    	"Revolution": ["Selections from the Marx-Engels Reader", "The French Revolution", "Reflections on the Revolutions in France", "American Revolution and Founding Texts"],
		    	"Morality": ["The Writings of Sigmund Freud", "On the Genealogy of Morals", "The Writings of Charles Darwin"],
		    	"Oppression": ["Three Guineas", "A Vindication of the Rights of Woman", "The Souls of Black Folk"],
		    }
		  }
