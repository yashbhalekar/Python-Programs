def build_person(first_name,last_name,age=' ') :
    person ={'first':first_name ,'last':last_name} #DICTIONARY
    if age:
        person['age']=age
    return person
musician = build_person('jimi','hendrix')
print(musician)


def make_album(title,artist,tracks=' ') :
    album = {'Title' : title , 'Artist' : artist}
    if tracks:
        album['track']=tracks
    return album

artist_group = make_album('t-series' , 'guru randhawa', tracks=20)
print(artist_group)


def city_country(city_name,country_name) :
    info = city_name +" "+","+country_name
    return info.title()

var =city_country('california','usa')
print(var)