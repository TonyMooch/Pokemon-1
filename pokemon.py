#!/usr/bin/python
import requests, re

from sets import Set

if __name__=='__main__':

    matchups = {}
    matchups.update({'bug':[Set(['psychic', 'grass', 'dark']), Set(['fighting', 'grass', 'ground']), Set(['fighting', 'fire', 'flying', 'ghost', 'poison', 'steel', 'fairy']), Set(['fire', 'flying', 'rock'])]})

    matchups.update({'dark':[Set(['ghost', 'psychic']), Set(['dark', 'ghost', 'PSYCHIC']), Set(['dark', 'fighting', 'fairy']), Set(['bug', 'fighting', 'fairy'])]})

    matchups.update({'dragon':[Set(['dragon']), Set(['electric', 'fire', 'grass', 'water']), Set(['steel', 'FAIRY']), Set(['dragon', 'ice', 'fairy'])]})

    matchups.update({'electric':[Set(['flying','water']), Set(['electric', 'flying', 'steel']), Set(['dragon', 'electric', 'grass', 'GROUND']), Set(['ground'])]})

    matchups.update({'fire':[Set(['bug', 'grass', 'ice', 'steel']), Set(['bug', 'fairy', 'fire', 'grass', 'ice', 'steel']), Set(['dragon', 'fire', 'rock', 'water']), Set(['ground', 'rock', 'water'])]})

    matchups.update({'grass':[Set(['ground', 'rock', 'water']), Set(['electric', 'grass', 'ground', 'water']), Set(['bug', 'dragon', 'fire', 'flying', 'grass', 'poison', 'steel']), Set(['bug', 'fire', 'flying', 'ice', 'poison'])]})

    matchups.update({'normal':[Set([]), Set(['GHOST']), Set(['rock', 'steel', 'GHOST']), Set(['fighting'])]})

    matchups.update({'rock':[Set(['bug', 'fire', 'flying', 'ice']), Set(['fire', 'flying', 'normal', 'poison']), Set(['fighting', 'ground', 'steel']), Set(['fighting', 'grass', 'ground', 'steel', 'water'])]})

    matchups.update({'fairy':[Set(['dark', 'dragon', 'fighting']), Set(['bug', 'dark', 'fighting', 'DRAGON']), Set(['fire', 'poison', 'steel']), Set(['poison', 'steel'])]})

    matchups.update({'flying':[Set(['bug', 'fighting', 'grass']), Set(['bug', 'fighting', 'grass', 'GROUND']), Set(['electric', 'rock', 'steel']), Set(['electric', 'ice', 'rock'])]})

    matchups.update({'ground':[Set(['electric', 'fire', 'poison', 'rock', 'steel']), Set(['poison', 'rock', 'ELECTRIC']), Set(['bug', 'grass', 'FLYING']), Set(['grass', 'ice', 'water'])]})

    matchups.update({'poison':[Set(['grass', 'fairy']), Set(['bug', 'fairy', 'fighting', 'grass', 'poison']), Set(['ghost', 'ground', 'poison', 'rock', 'STEEL']), Set(['ground', 'psychic'])]})

    matchups.update({'steel':[Set(['fairy', 'ice', 'rock']), Set(['bug', 'dragon', 'fairy', 'flying', 'grass', 'ice', 'normal', 'psychic', 'rock', 'steel']), Set(['electric', 'fire', 'steel', 'water']), Set(['fighting', 'fire', 'ground'])]})

    matchups.update({'fighting':[Set(['dark', 'ice', 'normal', 'rock', 'steel']), Set(['bug', 'dark', 'rock']), Set(['bug', 'fairy', 'flying', 'poison', 'psychic', 'GHOST']), Set(['fairy', 'flying', 'psychic'])]})

    matchups.update({'ghost':[Set(['ghost', 'psychic']), Set(['bug', 'poison', 'NORMAL', 'FIGHTING']), Set(['dark', 'NORMAL']), Set(['ghost', 'dark'])]})

    matchups.update({'ice':[Set(['dragon', 'flying', 'grass', 'ground']), Set(['ice']), Set(['fire', 'ice', 'steel', 'water']), Set(['fighting', 'fire', 'rock', 'steel'])]})

    matchups.update({'psychic':[Set(['fighting', 'poison']), Set(['fighting', 'psychic']), Set(['psychic', 'steel', 'DARK']), Set(['bug', 'dark', 'ghost'])]})

    matchups.update({'water':[Set(['fire', 'ground', 'rock']), Set(['fire', 'ice', 'steel', 'water']), Set(['dragon', 'grass', 'water']), Set(['electric', 'grass'])]})

    
    try:
        while(True):
            # Input the pokemon name
            name = raw_input('Enter pokemon name: ')

            # Grab the bulbapedia page for this pokemon
            r = requests.get('http://bulbapedia.bulbagarden.net/wiki/%s' % name)
            
            # Each pokemon has at most 2 types, find them
            start = r.text.find('(type)')
            type_section1 = str(r.text[start:start+100])
            m = re.search('[A-za-z]+ \(type\)', type_section1)
            try:
                type1 = m.group(0).split(' ')[0].lower()
            except AttributeError:
                print 'No pokemon by that name found.'
                continue

            print 'Type: ' , type1
            list1 = matchups[type1]

            start2 = r.text.find('(type)', start+100)
            type_section2 = str(r.text[start2:start2+100])
            m2 = re.search('[A-za-z]+ \(type\)', type_section2)
            type2 = m2.group(0).split(' ')[0].lower()
            
            if type2 != 'unknown':
                list2 = matchups[type2]
                print 'Type: ' , type2
            else:
                list2 = [Set([]), Set([]), Set([]), Set([])]

            combined_list = [x.union(y) for x,y in zip(list1, list2)]

            twice_damage_to = '2x Damage To:     '
            for element in combined_list[0]:
                twice_damage_to += element
                twice_damage_to += ', '

            twice_damage_to = re.sub(', $', '', twice_damage_to)

            half_damage_from = '1/2 Damage From:  '
            for element in combined_list[1]:
                half_damage_from += element
                half_damage_from += ', '

            half_damage_from = re.sub(', $', '', half_damage_from)

            half_damage_to = '1/2 Damage To:    '
            for element in combined_list[2]:
                half_damage_to += element
                half_damage_to += ', '
            half_damage_to = re.sub(', $', '', half_damage_to)

            twice_damage_from = '2x Damage From:   '
            for element in combined_list[3]:
                twice_damage_from += element
                twice_damage_from += ', '
            twice_damage_from = re.sub(', $', '', twice_damage_from)

            lowered = Set([x.lower() for x in combined_list[1]])
            intersection = combined_list[3].intersection(lowered)
            recommended = combined_list[3]
            [recommended.remove(x) for x in intersection]

            recommend_str = 'Battle with:      '
            for element in recommended:
                recommend_str += element
                recommend_str += ', '
            recommend_str = re.sub(', $', '', recommend_str)

            print twice_damage_to
            print half_damage_from
            print '--------------------------------------------------------------------------'
            print half_damage_to
            print twice_damage_from
            print recommend_str
            print '\n'

    except KeyboardInterrupt:
        pass
