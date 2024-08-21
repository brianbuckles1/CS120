# Mad Lib Game
# Brian Buckles
# 8/18/2024

# variables and inputs

# create a variable vehicle and store the vehicle input from the user
vehicle = input("Name a vehicle: ")
# create a variable color and store the color input from the user
color = input("Name a color: ")
# create a variable sitting_next_to and store the person, place or thing input from the user
sitting_next_to=input("Naming a person, animal, or thing: ")
# create a variable clothing and store the clothing input from the user
clothing = input("Name a piece of clothing: ")
# create a variable footware and store the footware input from the user
footware = input("Name a footware? boots, slippers, sneakers, ...:  ")
# create a variable drink and store the drink input from the user
drink = input("Name a drink: ")
# create a variable dinner and store the dinner input from the user
dinner=input("Name a dinner: ")
# create a variable location and store the result of the location input from the user
location = input("Name a location: ")
# create a variable activity and store the result of the activity input from the user
activity = input("Name an activity: ")
# create a variable music_genre and store the result of the music genre input from the user
music_genre=input("Name a music genre: ")
# create a variable music_genre_artist and store the result of the music genre artist input from the user
music_genre_artist=input(f"Name an artist in {music_genre}: ")
# create a variable music_genre_2 and store the result of the music genre 2 input from the user
music_genre_2=input("Name a second music genre: ")
# create a variable music_genre_2_artist and store the result of the music genre 2 artist input from the user
music_genre_2_artist=input(f"Name a artist in {music_genre_2}: ")
# create a variable weather_type and store the result of the weather type input from the user
weather_type=input("Name a type of weather: ")
# create a variable river and store the result of the river name input from the user
river=input("Name a river: ")

# create a variable song_lyrics with the song lyrics with the replacements from the stored variable inputs
song_lyrics=f"""
Uh, uh
I got that real good, feel good stuff
Up under the seat of my big {color} jacked up {vehicle}
Rollin' on thirty-fives
{sitting_next_to} by my side
You got that sun tan {clothing} and {footware}
Waitin' on you to look my way and scoot
Your little hot self over here
Girl, hand me another {drink}, yeah
All them other boys wanna wine you up and take you to {location}
But you look like the kind that likes to {activity}
Out where the corn rows grow, row, row my boat
Floatin' down the {river} River
Catch us up a little {dinner} dinner
Gonna sound like a winner
When I lay you down and love you right
Yeah, that's my kind of night
(Oh)
Might sit down on my diamond plate tailgate
Put in my {music_genre} {music_genre_2} mixtape
Little {music_genre_artist}, a little {music_genre_2_artist}
Might just make it {weather_type} (make it {weather_type})
You can hang your {clothing} on a limb
Hit that bank and we can ease on in
Soak us up a little moonlight
You know I know what you like, yeah
All them other boys wanna wine you up and take you to {location}
But you look like the kind that likes to {activity}
Out where the corn rows grow, row, row my boat
Floatin' down the {river} River
Catch us up a little {dinner} dinner
Gonna sound like a winner
When I lay you down and love you right
Yeah, that's my kind of night
Yeah, that's my kind of night
(Oh)
My kind or your kind, it's this kind of night
We dance in the dark and your lips land on mine
Oh, gonna get our love on
Oh, time to get our buzz on
All them other boys wanna wine you up and take you {location}
But you look like the kind that likes to {activity}
Out where the corn rows grow, row, row my boat
Floatin' down the {river} River
Catch us up a little {dinner} dinner
Gonna sound like a winner
When I lay you down and love you right
Yeah, that's my kind of night
Yeah, that's my kind of night
(Oh)
Yeah, that's my kind of night
(Oh)
Yeah, that's my kind of night
(Oh)
(Oh) come on
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Source: LyricFind
Songwriters: Ashley Glenn Gorley / Christopher Michael De Stefano / Gerald Dallas Davidson
That's My Kind of Night lyrics © Downtown Music Publishing, Royalty Network, Sony/ATV Music Publishing LLC, Warner Chappell Music, Inc
"""

#output the final result to the user
print(song_lyrics)