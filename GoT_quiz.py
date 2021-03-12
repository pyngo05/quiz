quiz = {
  'The drummer for which famous band made a cameo appearance during the Red Wedding?': 'Coldplay',
  'How many episodes of Game of Thrones are there in total?': '73',
  'Which character appears in more episodes than any other?': 'Tyrion Lannister',
  'What is the name of Jon Snow’s direwolf?': 'Ghost',
  'Who is king of Westeros at the very start of the show?': 'Robert Baratheon',
  'Which British actress was originally cast as Daenerys in the unaired pilot episode?': 'Tamzin Merchant',
  '\'All men must die\' translates as what term in High Valyrian?': 'Valar morghulis',
  'Fill in the blanks for Emilia Clarke’s original title: \'Daenerys Stormborn of the House Targaryen, First of Her Name, the Unburnt, Queen of the ____ and the ____, Khaleesi of the Great Grass Sea, ____ of Chains, and ____ of Dragons\'': 'Andals, First Men, Breaker, Mother',
  'The largest skull in the dungeons beneath King’s Landing belonged to which dragon?': 'Balerion',
  'Which animal does Tywin Lannister skin during his first appearance in the show?': 'Deer',
  'Which actress plays the role of Margaery Tyrell?': 'Natalie Dormer',
  'Name the ancestral home of House Lannister?': 'Casterly Rock',
  'How does Viserys Targaryen die in season 1?': 'Khal Drogo pours liquid gold over his head',
  'Which character says the line: \'Say it. Say her name. Say it!\'': 'Oberyn Martell',
  'Name the orphan baker boy who befriends Arya Stark?': 'Hot Pie',
  'What do the initials stand for in the infamous – and ultimately correct – Game of Thrones fan theory \‘R+L=J\’?': 'Rhaegar, Lyanna, Jon',
  'What is the name of the huge mercenary army commanded by Daenerys?': 'The Unsullied',
  'Which character is often referred to with ‘Giantsbane’ in their name?': 'Tormund',
  'Which vegetable-related nickname is Stannis Baratheon’s right-hand man Davos Seaworth known by?': 'The Onion Knight',
  'Which character ends up being crowned King of the Six Kingdoms in the final episode?': 'Bran Stark ',
}

points = 0
for q, a in quiz.items():
  print(q + '\n')
  answer = input()
  if answer == a: 
    print(answer + ' is the right answer! \n')
    points +=1
  else:
    print('Wrong! ' + a + ' is the correct answer. \n')

print('You got ' + str(points) + ' out of 20')
