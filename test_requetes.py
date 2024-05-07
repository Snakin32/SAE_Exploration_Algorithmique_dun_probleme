import requetes as req

#Voici le ficiher test pour les fonctions nécessitant des vérifications (avec le fichier créé réduit pour accélérer le temps des tests -> "data_2.json"):

# tests collaborateurs_communs

def test_collaborateurs_communs():
    assert req.collaborateurs_communs(req.json_vers_nx("./data_2.json"), "Robert Downey Jr.", "Tom Holland") is None
    assert req.collaborateurs_communs(req.json_vers_nx("./data_2.json"), "Rutger Hauer", "Sean Young") == {'Harrison Ford', 'Joe Turkel', 'Brion James', 'James Hong', 'Edward James Olmos', 'Daryl Hannah', 'William Sanderson', 'Morgan Paull', 'Joanna Cassidy', 'Hy Pyke', 'M. Emmet Walsh'}
    assert req.collaborateurs_communs(req.json_vers_nx("./data_2.json"), "Daryl Hannah", "Hy Pyke") == {'Sean Young', 'William Sanderson', 'Joe Turkel', 'Edward James Olmos', 'Brion James', 'Rutger Hauer','M. Emmet Walsh', 'Joanna Cassidy', 'James Hong', 'Morgan Paull', 'Harrison Ford'}
    assert req.collaborateurs_communs(req.json_vers_nx("./data_2.json"), "Jack Palance", "Jerry Hall") == {'Michael Keaton', 'Jack Nicholson', 'Tracey Walter', 'Adrian Meyers', 'David Baxt', 'William Hootkins', 'Billy Dee Williams', 'Sharon Holm', 'Hugo Blick', 'Pat Hingle', 'Garrick Hagon', 'Robert Wuhl', 'Kim Basinger', 'Lee Wallace', 'Liza Ross', 'Charles Roskilly', 'Michael Gough'}
    assert req.collaborateurs_communs(req.json_vers_nx("./data_2.json"), "Eric Lloyd", "Nicole Kidman") == {'Pat Hingle', 'Michael Gough', "Chris O'Donnell", 'Elizabeth Sanders'}

# tests collaborateurs_communs

def test_collaborateurs_proches():
    assert req.collaborateurs_proches(req.json_vers_nx("data_2.json"), "Rutger Hauer", 3) == {'Kimberly Scott', 'Michael Gough', 'René Auberjonois', 'Christopher Walken', 'Vincent Schiavelli', 'Alicia Silverstone', 'Christian Boeving', 'Seth Green', 'Billy Dee Williams', 'Vendela Kirsebom', 'Luke Perry', 'Elizabeth Sanders', 'Anna Katarina', 'Hugo Blick', 'Uma Thurman', 'Robert Swenson', 'David Baxt', 'Debi Mazar', 'William Hootkins', 'Liza Ross', 'Armand Assante', 'Ed Begley Jr.', 'Ofer Samra', 'M. Emmet Walsh', 'Daryl Hannah', 'Hy Pyke', 'David Arquette', 'Hilary Swank', 'Rick Zumwalt', 'Doug Jones', 'Glory Fioramonti', 'Joanna Cassidy', 'Adrian Meyers', 'Elle Macpherson', 'Sasha Jenson', 'George Wallace', 'Val Kilmer', 'Kristy Swanson', 'Arnold Schwarzenegger', 'Pat Hingle', 'Tommy Lee Jones', 'En Vogue', 'James Hong', 'Jerry Hall', 'Thomas Jane', "Chris O'Donnell", 'Tracey Walter', 'Jim Carrey', 'Stephen Root', 'Charles Roskilly', 'Joe Grifasi', 'Harrison Ford', 'Candy Clark', 'Morgan Paull', 'Jon Favreau', 'Randall Batinkoff', 'Garrick Hagon', 'Vivica A. Fox', 'Joe Turkel', 'Paris Vaughan', 'Michelle Pfeiffer', 'Kim Basinger', 'Ricki Lake', 'John Glover', 'Marisa Brown', 'Robert Wuhl', 'Danny DeVito', 'Michele Abrams', 'Sarah Sebastiana', 'Sean Young', 'Nicole Kidman', 'Eric Lloyd', 'Brion James', 'Cristi Conaway', 'Robert Arquette', 'Rutger Hauer', 'Kresh Novakovic', 'Jon Simmons', 'Paul Reubens', 'Jack Palance', 'William Sanderson', 'Donald Sutherland', 'Lee Wallace', 'Drew Barrymore', 'Edward James Olmos', 'Michael Paul Chan', 'Ben Affleck', 'Natasha Gregson Wagner', 'Michael Murphy', 'Larry A. Lee', 'Sharon Holm', 'Jack Nicholson', 'Andrew Bryniarski', 'George Clooney', 'Federico Castelluccio', 'Michael Keaton', 'Diane Salinger', 'Eric Roberts'}
    assert req.collaborateurs_proches(req.json_vers_nx("data_2.json"), "Paul Marco", 2) == {'Bud Osborne', 'Bela Lugosi', 'Tor Johnson', 'Loretta King Hadler', 'Ben Frommer', 'Don Nagel', 'Tony McCoy', 'John Warren', 'Paul Marco', 'Ann Wilner', 'Harvey B. Dunn', 'George Becwar', 'William "Billy" Benedict', 'Dolores Fuller'}
    assert req.collaborateurs_proches(req.json_vers_nx("data_2.json"), "George Coulouris", 0) == {"George Coulouris"}
    assert req.collaborateurs_proches(req.json_vers_nx("data_2.json"), "Warren Hymer", 1) == {'Brian Donlevy', 'James Stewart', 'Billy Gilbert', 'Tom Fadden', 'Marlene Dietrich', 'Mischa Auer', 'Ann E. Todd', 'Irene Hervey', 'Samuel S. Hinds', 'Una Merkel', 'Lillian Yarbo', 'Warren Hymer', 'Charles Winninger', 'Jack Carson', 'Edmund MacDonald', 'Virginia Brissac', 'Allen Jenkins', 'Dick Jones', 'Joe King'}
    assert req.collaborateurs_proches(req.json_vers_nx("data_2.json"), "Ken Baker", 4) == {'David Margulies', 'Anthony Boyd Scriven', 'Brandon Maggart', 'Angie Dickinson', 'Frederick Sanders', 'Ken Baker', 'Dennis Franz', 'Robert McDuffie', 'Keith Gordon', 'Susanna Clemm', 'Anneka Di Lorenzo', 'William Finley', 'Nancy Allen', 'Robert Lee Rush', 'Michael Caine'}
   
# tests est_proche

def test_est_proche():
    assert req.est_proche(req.json_vers_nx("./data_2.json"), "Rutger Hauer", "Sean Young") is True
    assert req.est_proche(req.json_vers_nx("./data_2.json"), "Rutger Hauer", "Jerry Hall") is False
    assert req.est_proche(req.json_vers_nx("./data_2.json"), "Slim Pickens", "Shane Rimmer") is True
    assert req.est_proche(req.json_vers_nx("./data_2.json"), "Lutz Schnell", "Betsy Baker") is False
    assert req.est_proche(req.json_vers_nx("./data_2.json"), "Bill Shine", "John Miller") is True