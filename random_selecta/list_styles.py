#%%
import pandas as pd
import pandas_gbq

#%%
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Electro
electronic_style = [
    "House", "Experimental", "Synth-pop", "Techno", "Ambient", "Electro", "Trance", "Downtempo", "Disco", "Tech House", 
    "Noise", "Deep House", "Drum n Bass", "Progressive House", "Industrial", "Euro House", "Abstract", "Hardcore", "Minimal", 
    "Pop Rock", "Breakbeat", "Drone", "Progressive Trance", "IDM", "New Wave", "Breaks", "Dark Ambient", "Dance-pop", 
    "Hard Trance", "Electro House", "Acid", "Alternative Rock", "Europop", "Leftfield", "Dubstep", "Psy-Trance", "Dub", 
    "Indie Rock", "Hard House", "Hip Hop", "Funk", "New Age", "Modern Classical", "Ballad", "EBM", "Italo-Disco", "Trip Hop", 
    "Jungle", "Soundtrack", "Hardstyle", "Soul", "Synthwave", "Garage House", "Darkwave", "Vaporwave", "Happy Hardcore", 
    "Eurodance", "UK Garage", "Tribal", "Italodance", "Vocal", "Future Jazz", "RnB/Swing", "Glitch", "Harsh Noise Wall", 
    "Indie Pop", "Pop Rap", "Latin", "Dub Techno", "Gabber", "Avantgarde", "Breakcore", "Hi NRG", "Power Electronics", 
    "Acid House", "Dungeon Synth", "Psychedelic Rock", "Punk", "Musique Concrète", "Minimal Techno", "Field Recording", 
    "Chiptune", "Freestyle", "Nu-Disco", "Post-Punk", "Tribal House", "Contemporary R&B", "Big Beat", "Acid Jazz", "Berlin-School", 
    "Lo-Fi", "Folk", "Soft Rock", "Post Rock", "Broken Beat", "Art Rock", "Prog Rock", "Instrumental", "Chanson", "Chillwave", 
    "Goth Rock", "Goa Trance", "Black Metal", "Hip-House", "Euro-Disco", "Krautrock", "Deep Techno", "Trap", "Score", "Bass Music", 
    "Acoustic", "Rhythmic Noise", "Contemporary", "Folk Rock", "Grime", "Tech Trance", "Free Improvisation", "Hard Techno", 
    "J-pop", "Shoegaze", "Speedcore", "Eurobeat", "Easy Listening", "Boogie", "Sound Collage", "Neofolk", "Makina", "Spoken Word", 
    "Freetekno", "Witch House", "Fusion", "Rhythm & Blues", "Schlager", "Hands Up", "Jazzdance", "Reggae-Pop", "Ethereal", 
    "Contemporary Jazz", "Jazz-Funk", "Hard Rock", "Theme", "Heavy Metal", "Reggae", "Space Rock", "Neo-Classical", "New Beat", 
    "Electroacoustic", "Video Game Music", "Italo House", "Classic Rock", "Jumpstyle", "Rock & Roll", "Speed Garage", "Grindcore", 
    "African", "Illbient", "Conscious", "Bassline", "Smooth Jazz", "Dancehall", "Doom Metal", "Neo Soul", "Donk", "Coldwave", 
    "Soul-Jazz", "Free Jazz", "Cut-up/DJ", "Classical", "Juke", "Avant-garde Jazz", "Blues Rock", "Lounge", "Holiday", "Jazzy Hip-Hop", 
    "Parody", "Dream Pop", "Glam", "Afrobeat", "Psychedelic", "Kayōkyoku", "Power Pop", "Disco Polo", "Sound Art", "Garage Rock", 
    "New Jack Swing", "Jazz-Rock", "Electroclash", "Tropical House", "Symphonic Rock", "Ska", "Ghetto", "Country Rock", "Ragga HipHop", 
    "Ragga", "Death Metal", "K-pop", "Progressive Breaks", "Country", "Halftime", "City Pop", "Britpop", "Novelty", "Nu Metal", 
    "Comedy", "Footwork", "Gangsta", "Poetry", "Therapy", "Modern", "Industrial Metal", "Balearic", "J-Core", "Mandopop", "Latin Jazz", 
    "Reggaeton", "Gospel", "Doomcore", "Schranz", "AOR", "Ghetto House", "Glitch Hop", "Bubblegum", "Dark Electro", "Bleep", "Boom Bap", 
    "Samba", "Interview", "Roots Reggae", "Cumbia", "No Wave", "Noisecore", "Bossa Nova", "Arena Rock", "Swing", "Hyperpop", "Medieval", 
    "Salsa", "Pop Punk", "Emo", "Space-Age", "Atmospheric Black Metal", "Celtic", "Bossanova", "Plunderphonics", "Goregrind", "Thrash", 
    "Religious", "Hardcore Hip-Hop", "Cloud Rap", "Math Rock", "Flamenco", "Cantopop", "Special Effects", "Alt-Pop", "Future House", 
    "Anison", "Big Band", "Metalcore", "Neo Trance", "Rumba", "Thug Rap", "Post-Modern", "Ghettotech", "Merengue", "Grunge", "Beatdown", 
    "Surf", "P.Funk", "Swingbeat", "Future Bass", "Stoner Rock", "MPB", "Kwaito", "Screw", "Dialogue", "DJ Battle Tool", "Canzone Napoletana", 
    "Romantic", "UK Funky", "Cool Jazz", "Military", "Baroque", "Radioplay", "Rockabilly", "Funk Metal", "NDW", "Bhangra", "Afro-Cuban", 
    "Post-Hardcore", "Speech", "Baltimore Club", "Miami Bass", "Musical", "Electro Swing", "Sound Poetry", "Indian Classical", "Tango", 
    "Ambient House", "Gothic Metal", "Hindustani", "Sludge Metal", "Turntablism", "Free Funk", "Lento Violento", "Nordic", "Ethno-pop", 
    "Deconstructed Club", "Bollywood", "Progressive Metal", "Beat", "Cha-Cha", "Crunk", "Health-Fitness", "Latin Pop", "Aboriginal", 
    "Mod", "Zouk", "French House", "Afro-Cuban Jazz", "Acid Rock", "Hard Beat", "Comfy Synth", "Favela Funk", "Opera"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Rock
rock_style = [
    "Pop Rock", "Punk", "Alternative Rock", "Indie Rock", "Hard Rock", "Rock & Roll", "Hardcore", "Heavy Metal", 
    "Psychedelic Rock", "Folk Rock", "Prog Rock", "Classic Rock", "Black Metal", "Blues Rock", "Experimental", 
    "Death Metal", "New Wave", "Soft Rock", "Garage Rock", "Synth-pop", "Thrash", "Acoustic", "Country Rock", 
    "Ballad", "Vocal", "Art Rock", "Post-Punk", "Noise", "Doom Metal", "Beat", "Avantgarde", "Rockabilly", "Grindcore", 
    "Folk", "Lo-Fi", "Post Rock", "Rhythm & Blues", "Power Pop", "Glam", "Industrial", "Goth Rock", "Soul", "Indie Pop", 
    "Ambient", "Emo", "Soundtrack", "Stoner Rock", "Disco", "Shoegaze", "Surf", "Electro", "Pop Punk", "Chanson", "Oi", 
    "Country", "Ska", "Doo Wop", "Jazz-Rock", "Funk", "Metalcore", "Grunge", "Progressive Metal", "Arena Rock", "AOR", 
    "Southern Rock", "Nu Metal", "Symphonic Rock", "Downtempo", "Power Metal", "Space Rock", "Speed Metal", "House", 
    "Fusion", "Krautrock", "Post-Hardcore", "Europop", "Sludge Metal", "Mod", "Abstract", "Schlager", "Math Rock", "Drone", 
    "Crust", "Darkwave", "Easy Listening", "Leftfield", "Britpop", "Ethereal", "Melodic Death Metal", "Gothic Metal", 
    "Goregrind", "Psychobilly", "Symphonic Metal", "Parody", "Atmospheric Black Metal", "Dark Ambient", "Holiday", 
    "Pop Rap", "J-pop", "Lounge", "Dream Pop", "Melodic Hardcore", "Funk Metal", "Dub", "Neofolk", "Modern Classical", 
    "Instrumental", "Deathcore", "Euro House", "Gospel", "Acid Rock", "Techno", "Dance-pop", "Folk Metal", "Minimal", 
    "RnB/Swing", "Twist", "Free Improvisation", "J-Rock", "Noisecore", "Hip Hop", "Trip Hop", "Post-Metal", "Novelty", 
    "Electric Blues", "Psychedelic", "Theme", "Reggae", "Jazz-Funk", "Spoken Word", "Coldwave", "Interview", "Score", 
    "Viking Metal", "Trance", "No Wave", "Religious", "Breakbeat", "Pub Rock", "EBM", "Synthwave", "Contemporary R&B", 
    "Industrial Metal", "Contemporary Jazz", "Alternative Metal", "Depressive Black Metal", "Comedy", "Yé-Yé", "Drum n Bass", 
    "IDM", "Reggae-Pop", "Country Blues", "Power Violence", "MPB", "Noise Rock", "Technical Death Metal", "Groove Metal", 
    "Celtic", "Swing", "Soul-Jazz", "Free Jazz", "New Age", "Deathrock", "Bluegrass", "Contemporary", "Kayōkyoku", 
    "Horror Rock", "Neo-Classical", "Big Band", "Breaks", "Latin", "Eurodance", "Big Beat", "Musical", "Avant-garde Jazz", 
    "Bubblegum", "Dungeon Synth", "Public Broadcast", "Jangle Pop", "Funeral Doom Metal", "Classical", "Smooth Jazz", 
    "African", "Latin Jazz", "City Pop", "Pornogrind", "Italo-Disco", "Chiptune", "Modern Electric Blues", "Progressive House", 
    "Tribal", "Cumbia", "Dubstep", "Chicago Blues", "Hardcore Hip-Hop", "Conscious", "Samba", "Electro House", "Musique Concrète", 
    "Field Recording", "Swamp Pop", "Poetry", "Power Electronics", "Breakcore", "Texas Blues", "Afrobeat", "Glitch", "Alt-Pop", 
    "Bossa Nova", "Flamenco", "Skiffle", "Dialogue", "Video Game Music", "Cha-Cha", "Tech House", "Honky Tonk", "Unblack Metal", 
    "Future Jazz", "Bossanova", "Neo Soul", "Anison", "Gangsta", "Acid Jazz", "Hi NRG", "Berlin-School", "Bolero", "Harmonica Blues", 
    "Mandopop", "Blackgaze", "Deep House", "NDW", "Group Sounds", "Rock Opera", "Boogie", "Rhythmic Noise", "Baroque Pop", 
    "Crossover thrash", "Salsa", "K-Rock", "Rumba", "Tango", "Freestyle", "Trap", "Acid", "Harsh Noise Wall", "Modern", 
    "Louisiana Blues", "Acid House", "Afro-Cuban", "Cajun", "Rocksteady", "Piano Blues", "Minneapolis Sound", "Light Music", 
    "Sound Collage", "Space-Age", "Jump Blues", "Boogie Woogie", "Promotional", "Calypso", "Hillbilly", "Cool Jazz", "Happy Hardcore", 
    "Éntekhno", "Cut-up/DJ", "Ragga HipHop", "Sunshine Pop", "Chillwave", "Delta Blues", "Slowcore", "Italodance", "UK Garage", 
    "Progressive Trance", "Medieval", "Euro-Disco", "Political", "Speech", "Mambo", "Garage House", "Hip-House", "Opera", 
    "Electroclash", "Romantic", "Free Funk", "Radioplay", "Vaporwave", "Dancehall", "Polka", "Gabber", "P.Funk", "Nordic", 
    "Mathcore", "Speedcore", "Roots Reggae", "Dixieland", "K-pop", "Afro-Cuban Jazz", "New Jack Swing", "Music Hall", "Jungle"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Pop
pop_style = [
"Vocal", "Pop Rock", "Ballad", "Chanson", "Schlager", "Synth-pop", "Europop", "Easy Listening",
"Indie Pop", "Disco", "Soft Rock", "Rock & Roll", "Indie Rock", "Soul", "Soundtrack",
"Alternative Rock", "Folk", "House", "Dance-pop", "J-pop", "Holiday", "Folk Rock", "New Wave",
"Electro", "Country", "Euro House", "Rhythm & Blues", "Beat", "Downtempo", "Funk", "Novelty",
"Acoustic", "Psychedelic Rock", "Classic Rock", "Kayōkyoku", "Experimental", "Pop Rap", "Big Band",
"RnB/Swing", "Swing", "Theme", "Contemporary R&B", "Bollywood", "Power Pop", "Parody", "Gospel",
"Country Rock", "Light Music", "Mandopop", "Garage Rock", "Religious", "Comedy", "Prog Rock",
"Ambient", "Blues Rock", "Instrumental", "Punk", "Eurodance", "Doo Wop", "Hard Rock", "Hindustani",
"Art Rock", "Trance", "Surf", "K-pop", "Musical", "Lo-Fi", "Glam", "Italo-Disco", "Hip Hop",
"Music Hall", "Reggae-Pop", "AOR", "City Pop", "Tango", "MPB", "Techno", "Latin", "Rockabilly",
"Score", "Canzone Napoletana", "Electro House", "Leftfield", "Bubblegum", "Soul-Jazz", "Progressive House",
"Bolero", "Volksmusik", "Smooth Jazz", "Enka", "Romantic", "Classical", "Pop Punk", "Trip Hop",
"Ska", "Shoegaze", "Mod", "Contemporary Jazz", "Lounge", "Spoken Word", "Contemporary", "Samba",
"Hi NRG", "African", "Euro-Disco", "Jazz-Funk", "Dream Pop", "Abstract", "Latin Jazz", "Laïkó",
"Post-Punk", "Rumba", "Avantgarde", "Twist", "Karaoke", "Flamenco", "Reggae", "Bossa Nova", "Alt-Pop",
"Cha-Cha", "Anison", "Yé-Yé", "Arena Rock", "Cantopop", "New Age", "Fusion", "Jazz-Rock", "Britpop",
"Space-Age", "Russian Pop", "Deep House", "Modern Classical", "Bossanova", "Breakbeat", "Polka",
"Hokkien Pop", "Symphonic Rock", "Boogie", "Dub", "Italodance", "Salsa", "Drum n Bass", "Neo Soul",
"Romani", "Choral", "Levenslied", "Psychedelic", "Trap", "Latin Pop", "Post Rock", "Promotional",
"Heavy Metal", "Industrial", "Synthwave", "Cumbia", "Freestyle", "Minimal", "Noise", "Interview",
"Ethno-pop", "Celtic", "IDM", "J-Rock", "Pacific", "Tech House", "Cool Jazz", "Neo-Classical",
"Ragtime", "Story", "Ethereal", "Hip-House", "New Jack Swing", "Indo-Pop", "Darkwave", "Poetry",
"Mambo", "Jangle Pop", "Opera", "Calypso", "Modern", "Reggaeton", "Breaks", "Dixieland", "Marches",
"Garage House", "UK Garage", "Nursery Rhymes", "Acid Jazz", "Public Broadcast", "Dubstep", "Dialogue",
"Emo", "Hawaiian", "Éntekhno", "Nu-Disco", "Goth Rock", "Minneapolis Sound", "Operetta", "Educational",
"Hardcore", "Chillwave", "Merengue", "Big Beat", "Happy Hardcore", "Dancehall", "Ryūkōka", "Bhangra",
"Ranchera", "Southern Rock", "Musette", "Barbershop", "Nordic", "Eurobeat", "Mariachi", "Conscious",
"Political", "Krautrock", "Afrobeat", "Tropical House", "Tribal House", "Progressive Trance", "Chiptune",
"Video Game Music", "Space Rock", "Future Jazz", "Hard Trance", "Neofolk", "Beguine", "Afro-Cuban", "Monolog",
"Grunge", "Radioplay", "Brass Band", "Country Blues", "Sunshine Pop", "Bluegrass", "Gangsta", "Tribal",
"Vaporwave", "EBM", "Glitch", "Baroque Pop", "Ragga HipHop", "Piano Blues", "Dark Ambient", "Acid House",
"Baroque", "Bop", "Bass Music", "Hard House", "Hyperpop", "Exotica", "Neo-Romantic", "Fado", "Jazzdance",
"Nhạc Vàng", "Nu Metal", "Acid Rock", "Drone", "Pub Rock", "Catalan Music", "Military", "Speech",
"Jazzy Hip-Hop", "NDW", "Swingbeat", "Field Recording", "Cubano", "Group Sounds", "Ragga", "Electroclash",
"Bachata", "Mizrahi", "Raï", "Education", "Electric Blues", "Skiffle", "Séga", "Cabaret", "Broken Beat",
"Cut-up/DJ", "Acid", "Free Improvisation", "Honky Tonk", "Thug Rap", "Nueva Cancion", "Lambada",
"Boogie Woogie", "Disco Polo", "Min'yō", "Sea Shanties", "Tejano", "Shidaiqu", "Hands Up", "Math Rock",
"Gypsy Jazz", "Villancicos", "Indian Classical", "Pachanga", "Zouk"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Funk Soul
funk_soul_style = [
    "Soul", "Disco", "Funk", "Rhythm & Blues", "Contemporary R&B", "Pop Rock", "Gospel", "Ballad",
    "Synth-pop", "Vocal", "Jazz-Funk", "House", "Soul-Jazz", "RnB/Swing", "Rock & Roll", "Boogie", 
    "Downtempo", "Soundtrack", "Electro", "Neo Soul", "Soft Rock", "Easy Listening", "Pop Rap", "Doo Wop", 
    "Psychedelic", "Afrobeat", "Fusion", "Alternative Rock", "Psychedelic Rock", "Blues Rock", "New Jack Swing",
    "African", "Europop", "Classic Rock", "Dance-pop", "Hip Hop", "Folk Rock", "Smooth Jazz", "Chanson",
    "New Wave", "Jazz-Rock", "Experimental", "Reggae", "Indie Rock", "Acid Jazz", "Folk", "Contemporary Jazz", 
    "Holiday", "MPB", "City Pop", "Latin Jazz", "P.Funk", "Country", "Garage Rock", "Theme", "Euro House", 
    "Jazzy Hip-Hop", "Prog Rock", "Deep House", "Beat", "Hard Rock", "Instrumental", "Schlager", "Dub", 
    "Kayōkyoku", "Country Rock", "AOR", "Reggae-Pop", "Garage House", "Samba", "Breakbeat", "Conscious", 
    "Indie Pop", "Big Band", "Trip Hop", "Breaks", "Ska", "Future Jazz", "Mod", "Acoustic", "Latin", "Trap", 
    "Salsa", "Punk", "Italo-Disco", "Score", "Ambient", "Swing", "Minneapolis Sound", "Leftfield", "Bossa Nova", 
    "Swingbeat", "Bayou Funk", "Religious", "Free Funk", "Afro-Cuban", "Gangsta", "Hi NRG", "Surf", "J-pop", 
    "Nu-Disco", "Techno", "Freestyle", "Abstract", "Broken Beat", "Glam", "Lounge", "Electric Blues", "Art Rock", 
    "Drum n Bass", "Trance", "Cumbia", "Boogaloo", "Calypso", "Rockabilly", "Bossanova", "Eurodance", "Novelty", 
    "Cut-up/DJ", "Jazzdance", "Highlife", "Spoken Word", "UK Garage", "Cool Jazz", "Southern Rock", "Progressive House", 
    "Dancehall", "UK Street Soul", "Hip-House", "Piano Blues", "Go-Go", "Electro House", "Funk Metal", "Vaporwave", 
    "Afro-Cuban Jazz", "Chicago Blues", "Big Beat", "Power Pop", "Avantgarde", "Ragga HipHop", "Bubblegum", "Bolero", 
    "Twist", "Musical", "Cha-Cha", "Rumba", "Roots Reggae", "Soca", "G-Funk", "Boom Bap", "Bass Music", "Comedy", 
    "Heavy Metal", "Free Jazz", "Country Blues", "Post-Punk", "Tech House", "Rocksteady", "Lo-Fi", "Lovers Rock", 
    "Space-Age", "Parody", "Modern Electric Blues", "Mambo", "Louisiana Blues", "Industrial", "Arena Rock", 
    "Thug Rap", "Britpop", "Dubstep", "Acid House", "Zouk", "Jump Blues", "Euro-Disco", "K-pop", "Hardcore Hip-Hop", 
    "Guaguancó", "Bollywood", "Avant-garde Jazz", "Interview", "Tribal", "Mandopop", "Dialogue", "New Age", 
    "Contemporary", "Flamenco", "Tribal House", "Light Music", "Krautrock", "Acid Rock", "Free Improvisation", 
    "Synthwave", "Classical", "Yé-Yé", "Modern Classical", "Descarga", "IDM", "Space Rock", "Symphonic Rock", 
    "Modal", "Merengue", "Hard Bop", "Bop", "Pop Punk", "Sermon", "Italodance", "Hardcore", "Hindustani", "Post Bop",
    "Choral"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Jazz
jazz_style = [
"Easy Listening", "Swing", "Big Band", "Contemporary Jazz", "Vocal", "Fusion", "Jazz-Funk",
"Soul-Jazz", "Bop", "Jazz-Rock", "Latin Jazz", "Free Improvisation", "Hard Bop", "Free Jazz",
"Cool Jazz", "Post Bop", "Smooth Jazz", "Experimental", "Dixieland", "Soundtrack", "Soul", "Funk",
"Bossa Nova", "Ballad", "Avant-garde Jazz", "Pop Rock", "Rhythm & Blues", "Modal", "Prog Rock",
"Disco", "Downtempo", "Chanson", "Ragtime", "Ambient", "Folk", "Theme", "Avantgarde", "Holiday",
"Space-Age", "Psychedelic Rock", "Instrumental", "Afro-Cuban Jazz", "Future Jazz", "Schlager", "Score",
"Synth-pop", "Abstract", "Samba", "Rock & Roll", "Blues Rock", "Contemporary", "Folk Rock",
"Alternative Rock", "Soft Rock", "Acid Jazz", "Gypsy Jazz", "Lounge", "House", "Mambo", "Cha-Cha", "Noise",
"New Age", "MPB", "Acoustic", "Bossanova", "Art Rock", "Afrobeat", "Tango", "African", "Country", "Gospel",
"Musical", "Electro", "Afro-Cuban", "Classic Rock", "Salsa", "Indie Rock", "Spoken Word", "Bolero", "Classical",
"Light Music", "Modern Classical", "Jazzy Hip-Hop", "Piano Blues", "Trip Hop", "Psychedelic", "Rumba",
"Modern", "Novelty", "Jazzdance", "Dub", "Deep House", "Leftfield", "Hip Hop", "Contemporary R&B", "Neo Soul",
"Punk", "New Wave", "Romantic", "Pacific", "Broken Beat", "Hard Rock", "Comedy", "Boogie Woogie", "Jump Blues",
"Beat", "Krautrock", "Neo-Classical", "Drone", "Country Rock", "Post Rock", "Flamenco", "Latin", "Ska", "Minimal",
"Poetry", "Europop", "Religious", "RnB/Swing", "Drum n Bass", "Music Hall", "Parody", "Breakbeat", "Indie Pop",
"Industrial", "Surf", "Techno", "Reggae", "Country Blues", "Calypso", "Rockabilly", "Descarga", "Field Recording",
"Guaguancó", "Breaks", "Doo Wop", "Baroque", "Musique Concrète", "Lo-Fi", "Mod", "Brass Band", "Conscious",
"IDM", "Twist", "Cubano", "Pop Rap", "Boogie", "AOR", "Boogaloo", "Merengue", "Garage Rock", "Electric Blues",
"Promotional", "City Pop", "J-pop", "Exotica", "Space Rock", "Math Rock", "Dark Ambient", "Dance-pop",
"Heavy Metal", "Son", "Bluegrass", "Free Funk", "Dark Jazz", "Cape Jazz", "Beguine", "Polka", "Hawaiian", "Tribal",
"Marches", "Post-Punk", "Kayōkyoku", "Chicago Blues", "Dialogue", "Education", "Louisiana Blues", "Symphonic Rock",
"Klezmer", "Vaporwave", "Interview", "Guaracha", "Euro House", "Nordic", "Cumbia", "Trance", "Hardcore", "Celtic",
"Boom Bap", "Indian Classical", "No Wave", "Neo-Romantic", "Honky Tonk", "Opera", "Electroacoustic", "Delta Blues",
"Cut-up/DJ", "Shidaiqu", "Choral", "Stride", "Progressive Metal", "Big Beat", "Canzone Napoletana", "Neofolk",
"Video Game Music", "Guajira", "Mariachi", "Modern Electric Blues", "Reggae-Pop", "Post-Modern", "Bayou Funk",
"Hindustani", "Southern Rock", "Ethereal", "Glitch", "Technical", "Chillwave", "Freestyle", "Western Swing", "Choro",
"Special Effects", "Grindcore", "Anison", "Pachanga", "Batucada", "Son Montuno", "Public Broadcast", "Radioplay",
"Sound Collage", "Sound Art", "Rocksteady", "Bollywood", "Chiptune", "Political", "Romani", "Acid Rock", "Glam",
"Garage House", "Highlife", "Black Metal"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Folk
world_style = [
"Folk", "Country", "Folk Rock", "African", "Vocal", "Gospel", "Volksmusik", "Ballad", "Country Rock",
"Celtic", "Bluegrass", "Laïkó", "Pop Rock", "Soundtrack", "Chanson", "Acoustic", "Polka", "Religious",
"Holiday", "Schlager", "Hindustani", "Experimental", "Easy Listening", "Indie Rock", "Flamenco", "Bollywood",
"Alternative Rock", "Ambient", "Psychedelic Rock", "Indian Classical", "Rock & Roll", "Éntekhno", "Rumba",
"Canzone Napoletana", "Soft Rock", "New Age", "Rockabilly", "Pacific", "Blues Rock", "Nordic", "Soul",
"Honky Tonk", "Indie Pop", "Fado", "Choral", "Soukous", "Highlife", "Hawaiian", "Funk", "Disco", "Zouk",
"Tango", "Downtempo", "Bolero", "Punk", "Country Blues", "Prog Rock", "Comedy", "Cumbia", "Europop", "Luk Thung",
"Fusion", "Romani", "MPB", "Classic Rock", "Classical", "Synth-pop", "Afrobeat", "Calypso", "Rhythm & Blues",
"Spoken Word", "Neofolk", "Samba", "Contemporary", "Contemporary Jazz", "Field Recording", "Cajun", "Bhangra",
"Lo-Fi", "Instrumental", "Novelty", "Avantgarde", "Tribal", "Hillbilly", "Andean Music", "House", "Rebetiko",
"Abstract", "Romantic", "Electro", "Swing", "Raï", "Poetry", "Afro-Cuban", "Marches", "Brass Band", "Chinese Classical",
"Séga", "Min'yō", "Parody", "Theme", "Western Swing", "Art Rock", "Reggae", "Ranchera", "Klezmer", "Free Improvisation",
"Latin Jazz", "Aboriginal", "Modern Classical", "Cha-Cha", "Salsa", "Dub", "Drone", "Psychedelic", "Political",
"Nueva Cancion", "Carnatic", "Garage Rock", "Pasodoble", "Score", "Catalan Music", "Southern Rock", "Merengue",
"Appalachian Music", "Népzene", "Musical", "Modern", "Hard Rock", "Big Band", "Dance-pop", "Compas", "Medieval",
"Bossanova", "Sea Shanties", "Copla", "Zydeco", "Soca", "Jazz-Rock", "Noise", "Bakersfield Sound", "Mariachi",
"Jazz-Funk", "Beguine", "Opera", "Neo-Classical", "Huayno", "Beat", "Liscio", "Light Music", "Ethereal", "Bossa Nova",
"Quechua", "Cretan", "Ska", "Mambo", "New Wave", "Forró", "Kayōkyoku", "Leftfield", "Gypsy Jazz", "Son",
"Nursery Rhymes", "Ghazal", "Baroque", "Guaracha", "Gamelan", "Dark Ambient", "Latin", "Space-Age", "Military",
"Kolo", "Mizrahi", "Surf", "Ottoman Classical", "Persian Classical", "Techno", "Post Rock", "Euro House",
"Industrial", "Soul-Jazz", "Chamamé", "Zamba", "Pop Rap", "Hip Hop", "Musette", "Minimal", "Enka", "Story",
"Trip Hop", "Bengali Music", "Corrido", "Education", "Smooth Jazz", "Avant-garde Jazz", "Chacarera", "Lounge",
"Ethno-pop", "Basque Music", "Mo Lam", "Educational", "Sertanejo", "AOR", "Free Jazz", "Cubano", "Ragtime",
"Reggae-Pop", "Dangdut", "Música Criolla", "Chutney", "Dixieland", "Dialogue", "Power Pop", "Krautrock", "Spirituals",
"Qawwali", "Trance", "Tamil Film Music", "Delta Blues", "Luk Krung", "Black Metal", "Promotional", "Contemporary R&B",
"Renaissance", "Afro-Cuban Jazz", "RnB/Swing", "Nhạc Vàng", "Vallenato", "Heavy Metal", "Gusle", "Electric Blues",
"Breakbeat", "Mandopop", "Doo Wop", "Kaseko", "Deep House", "Karaoke", "Occitan", "Drum n Bass", "Music Hall",
"Keroncong", "Boogie", "Interview", "Porro", "Eurodance", "Post-Punk", "Andalusian Classical", "Guarania", "Steel Band",
"Morna", "Folk Metal", "Baião", "Shoegaze", "Italo-Disco", "Pachanga", "Acid Rock", "Exotica", "Batucada", "IDM",
"J-pop", "Norteño", "Maloya", "Nueva Trova", "Darkwave", "Cool Jazz", "Jota", "Operetta", "Conscious", "Sephardic",
"Dancehall", "Izvorna", "Speech", "Tejano", "Overtone Singing", "Salegy", "Future Jazz", "Galician Traditional",
"Monolog", "Skiffle", "Texas Blues", "Griot", "Louisiana Blues", "Caipira", "Milonga", "Goth Rock", "Hardcore",
"Villancicos", "Dungeon Synth", "Public Broadcast", "Phleng Phuea Chiwit", "Dream Pop", "Symphonic Rock", "Breaks",
"Conjunto", "Musique Concrète", "Roots Reggae", "Twist", "Joropo", "Mbalax", "Therapy", "Bubblegum", "Zemer Ivri",
"Swamp Pop", "Pipe & Drum", "Space Rock", "Emo", "Glam", "Guajira", "Pop Punk", "Radioplay", "Thai Classical",
"Acid Jazz", "Mugham", "Trova", "Kwaito", "Dubstep", "Sermon", "Guaguancó", "Gagaku", "Funaná", "Neo-Romantic",
"Early", "Choro", "Neo Soul", "Ragga", "Charanga", "Cantorial", "Levenslied", "Shaabi", "Tribal House"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Classical
classical_style = [
"Romantic", "Classical", "Baroque", "Modern", "Opera", "Contemporary", "Choral", "Renaissance", "Neo-Classical",
"Soundtrack", "Religious", "Vocal", "Holiday", "Experimental", "Impressionist", "Easy Listening", "Operetta",
"Modern Classical", "Ambient", "Folk", "Score", "Neo-Romantic", "Medieval", "Organ", "Ballad", "Oratorio",
"Post-Modern", "Theme", "New Age", "Abstract", "Musical", "Minimal", "Contemporary Jazz", "Chanson", "Gospel",
"Instrumental", "Avantgarde", "Pop Rock", "Spoken Word", "Light Music", "Schlager", "Free Improvisation",
"Marches", "Drone", "Downtempo", "Acoustic", "Musique Concrète", "Prog Rock", "Dark Ambient", "Big Band", "Early",
"Synth-pop", "Zarzuela", "Field Recording", "Poetry", "Symphonic Rock", "Tango", "Alternative Rock", "Celtic",
"Story", "Video Game Music", "Ballet", "Electro", "Brass Band", "Noise", "Education", "Industrial", "Disco", "Swing",
"Indian Classical", "Avant-garde Jazz", "Volksmusik", "Fusion", "Folk Rock", "Twelve-tone", "Educational", "Art Rock",
"Military", "Classic Rock", "Canzone Napoletana", "Polka", "Comedy", "Post Rock", "Flamenco", "Indie Rock", "Electroacoustic",
"Speech", "Techno", "IDM", "Soft Rock", "Neofolk", "House", "Promotional", "Free Jazz", "Darkwave", "Psychedelic Rock",
"Nordic", "Country", "Soul", "Chinese Classical", "Novelty", "Smooth Jazz", "Political", "Rock & Roll", "Cool Jazz",
"Leftfield", "Ethereal", "Music Hall", "Public Broadcast", "Serial", "Interview", "Dungeon Synth", "Heavy Metal",
"Hard Rock", "Dialogue", "Europop", "Jazz-Rock", "Indie Pop", "Anison", "Latin Jazz", "New Wave", "Ragtime", "Technical",
"Jazz-Funk", "Trance", "Radioplay", "Audiobook", "Funk", "J-pop", "Hindustani", "African", "Parody", "Goth Rock",
"Sound Art", "Glitch", "Space-Age", "Blues Rock", "Samba", "Monolog", "Soul-Jazz", "Special Effects", "Trip Hop",
"Drum n Bass", "Rhythm & Blues", "Nursery Rhymes", "Black Metal", "MPB", "Éntekhno", "Bossa Nova", "Bolero",
"Persian Classical", "Sound Collage", "Therapy", "Punk", "Breakbeat", "Tribal", "Romani", "Lo-Fi", "Dance-pop", "Dixieland",
"Lounge", "Dubstep", "Chiptune", "Rumba", "Hip Hop", "Andalusian Classical", "Dub", "Hardcore", "Breaks", "Sermon",
"Pop Rap", "Doom Metal", "Cha-Cha", "Breakcore", "Gagaku", "Occitan", "Country Rock", "Future Jazz", "Gypsy Jazz",
"Catalan Music", "Post Bop", "Modal", "Synthwave", "Bop", "Symphonic Metal", "Beat", "Klezmer", "RnB/Swing",
"Rhythmic Noise", "Euro House", "Sephardic", "Krautrock", "Ottoman Classical", "Bossanova", "Choro", "Spirituals",
"Bluegrass", "Contemporary R&B", "Népzene", "Chillwave", "Sound Poetry", "Shoegaze", "Deep House", "Progressive House",
"Gamelan", "Mambo", "Carnatic", "Progressive Metal", "Psychedelic", "Death Metal", "Latin", "Electro House",
"Post-Punk", "EBM", "Pacific", "Movie Effects", "Thrash", "Arena Rock", "Power Electronics", "Broken Beat", "Fado",
"Big Beat", "Acid", "Aboriginal", "Reggae", "Surf", "Bollywood", "Tech House", "Acid Jazz", "Gothic Metal", "Min'yō",
"Illbient", "Afro-Cuban", "Pasodoble", "Berlin-School", "Happy Hardcore", "Piano Blues", "Mariachi", "Pipe & Drum",
"Space Rock"
]


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Hip hop
hip_hop_style = [
"Gangsta", "Pop Rap", "RnB/Swing", "Conscious", "Hip Hop", "Instrumental", "House", "Electro", "Hardcore Hip-Hop",
"Trap", "Contemporary R&B", "Boom Bap", "Jazzy Hip-Hop", "Thug Rap", "Downtempo", "Experimental", "Pop Rock",
"Synth-pop", "Alternative Rock", "G-Funk", "Soul", "Bass Music", "Euro House", "Funk", "Trip Hop", "Cut-up/DJ",
"Abstract", "Disco", "Europop", "Ragga HipHop", "Ballad", "Breakbeat", "Horrorcore", "Dance-pop", "Indie Rock",
"Breaks", "Soundtrack", "Hip-House", "Dancehall", "Drum n Bass", "Ambient", "Techno", "Dub", "Vocal", "Cloud Rap",
"Trance", "Grime", "Neo Soul", "Punk", "New Jack Swing", "Leftfield", "Dubstep", "Rhythm & Blues", "Screw", "UK Garage",
"Nu Metal", "Crunk", "Electro House", "Eurodance", "Reggae", "Hardcore", "Acid Jazz", "Reggaeton", "Industrial",
"DJ Battle Tool", "Soft Rock", "IDM", "Deep House", "Indie Pop", "Latin", "Big Beat", "Turntablism", "Bounce",
"Garage House", "Hard Rock", "Reggae-Pop", "Future Jazz", "Freestyle", "Broken Beat", "Lo-Fi", "Progressive House",
"Noise", "J-pop", "Glitch", "Folk Rock", "Acoustic", "Heavy Metal", "Miami Bass", "Jazz-Funk", "Chanson", "New Wave",
"Vaporwave", "Funk Metal", "African", "Ragga", "K-pop", "Folk", "Gospel", "Britcore", "Tech House", "Soul-Jazz",
"Ska", "Kwaito", "Rock & Roll", "Blues Rock", "Jungle", "Phonk", "Spoken Word", "Contemporary Jazz", "Classic Rock",
"Comedy", "Go-Go", "Chillwave", "Country Rock", "Fusion", "Emo", "Boogie", "Afrobeat", "Country", "Acid House", "Hyphy",
"Parody", "Drill", "Favela Funk", "Holiday", "Britpop", "Hiplife", "Psychedelic Rock", "Ghetto", "P.Funk", "Italodance",
"Witch House", "Avantgarde", "Breakcore", "Happy Hardcore", "Psychedelic", "Tribal", "Acid", "Minimal", "Novelty",
"Chiptune", "Jazzdance", "Pop Punk", "Hi NRG", "Dark Ambient", "Schlager", "Juke", "Art Rock", "Theme", "Garage Rock",
"Grunge", "Hard Trance", "Swingbeat", "Easy Listening", "Synthwave", "Illbient", "Sound Collage", "Beatbox", "Hard House",
"Post-Punk", "Post Rock", "Smooth Jazz", "Power Pop", "Italo-Disco", "Tribal House", "Score", "Thrash", "Progressive Trance",
"Salsa", "Modern Classical", "Arena Rock", "Drone", "Bhangra", "Nu-Disco", "Roots Reggae", "Swing", "Prog Rock", "Glitch Hop",
"Merengue", "Cumbia", "Interview", "Samba", "Shoegaze", "Poetry", "Darkwave", "Video Game Music", "Tropical House",
"Bassline", "EBM", "Euro-Disco", "Afro-Cuban", "Rhythmic Noise", "Avant-garde Jazz", "New Age", "Free Jazz", "Metalcore",
"MPB", "Jazz-Rock", "Glam", "Lounge", "Big Band", "Latin Jazz", "Hyperpop", "Death Metal", "Cool Jazz", "Alt-Pop",
"Bubblegum", "Grindcore", "Baltimore Club", "Religious", "AOR", "Mandopop", "Black Metal", "Goth Rock", "Hardstyle",
"Free Improvisation", "New Beat", "Dialogue", "Bossa Nova", "Gabber", "Musique Concrète", "Contemporary", "Surf",
"Eurobeat", "Beat", "Flamenco", "Footwork", "Free Funk", "Rockabilly", "Zouk", "Soca", "UK Street Soul", "Field Recording",
"Dub Techno", "Raï", "Ethereal", "Cubano", "Speed Garage", "Ghettotech", "Southern Rock", "Latin Pop", "Stoner Rock",
"Rumba", "Bossanova", "Low Bap", "Beatdown", "Classical", "Electric Blues", "Electroclash", "Italo House", "Political",
"Speedcore", "Afro-Cuban Jazz", "Brass Band", "Power Electronics", "Space-Age", "Space Rock", "Celtic", "Ghetto House",
"Krautrock", "Symphonic Rock", "Jersey Club", "Ethno-pop", "Skweee", "Alternative Metal", "Post-Hardcore", "Musical",
"Neofolk", "Anison", "Special Effects", "Dream Pop", "Pacific", "Speech", "Math Rock", "Promotional", "Rocksteady",
"Bluegrass", "Laïkó", "Halftime", "Doom Metal", "Future Bass", "Hands Up", "Plunderphonics", "Mambo", "Bachata", "Batucada",
"Dungeon Synth", "Doo Wop", "Modern", "Industrial Metal", "Psy-Trance", "Radioplay", "Moombahton", "Speed Metal",
"Tango", "Bongo Flava", "Jumpstyle", "No Wave", "Educational", "Minimal Techno", "Lovers Rock", "Bop", "Country Blues",
"Deep Techno", "Karaoke", "Post Bop", "Bollywood", "Deconstructed Club", "Electroacoustic", "Calypso", "Public Broadcast",
"Hard Techno", "Minneapolis Sound", "Sound Art", "Highlife", "Romani", "Cha-Cha", "Electro Swing", "Neo-Classical", "Acid Rock",
"City Pop", "UK Funky", "Gypsy Jazz", "Harsh Noise Wall", "Mod", "Hard Bop", "Aboriginal", "Cantopop", "Hindustani",
"Post-Modern"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Stage&screen
stage_style = [
"Soundtrack", "Score", "Theme", "Musical", "Vocal", "Easy Listening",
"Pop Rock", "Bollywood", "Ballad", "Hindustani", "Video Game Music",
"Ambient", "Synth-pop", "Chanson", "Experimental", "Rock & Roll", "Disco",
"Modern Classical", "Contemporary", "Comedy", "Anison", "Big Band", "Folk",
"Soul", "Funk", "Alternative Rock", "Classical", "Swing", "Downtempo",
"Opera", "Schlager", "Psychedelic Rock", "Romantic", "Spoken Word", "Soft Rock",
"Modern", "Story", "Jazz-Funk", "Electro", "Dialogue", "Classic Rock",
"Folk Rock", "J-pop", "Country", "Abstract", "Rhythm & Blues", "Hard Rock",
"Soul-Jazz", "Prog Rock", "House", "Instrumental", "Neo-Classical",
"Contemporary Jazz", "Indie Rock", "Holiday", "Novelty", "Operetta", "Lounge",
"Blues Rock", "Beat", "Country Rock", "Industrial", "Music Hall", "Techno",
"Indian Classical", "Chiptune", "Kayōkyoku", "Light Music", "Acoustic",
"Radioplay", "Cool Jazz", "New Wave", "Pop Rap", "Dark Ambient", "Smooth Jazz",
"Parody", "Contemporary R&B", "Europop", "New Age", "Punk", "Neo-Romantic",
"Heavy Metal", "Surf", "Promotional", "RnB/Swing", "Cabaret", "Avantgarde",
"Latin Jazz", "Religious", "Bossa Nova", "Space-Age", "Dance-pop", "Monolog",
"Breakbeat", "Minimal", "Poetry", "Synthwave", "Jazz-Rock", "Gospel", "Art Rock",
"Leftfield", "Carnatic", "Tamil Film Music", "Tango", "Fusion", "Baroque",
"Psychedelic", "Hip Hop", "Interview", "Gangsta", "Symphonic Rock", "Trance",
"Audiobook", "Trip Hop", "Drum n Bass", "Samba", "Marches", "Ragtime",
"Special Effects", "Dixieland", "Breaks", "Choral", "Field Recording",
"Arena Rock", "Glam", "Movie Effects", "MPB", "Rockabilly", "Zarzuela", "Educational",
"Drone", "Éntekhno", "Garage Rock", "Bossanova", "Bhangra", "Indie Pop", "Euro House",
"Nursery Rhymes", "Vaudeville", "Noise", "J-Rock", "Political", "Doo Wop", "Laïkó",
"African", "Bop", "Ballet", "Musique Concrète", "Big Beat", "Mandopop", "Tribal",
"Post Rock", "Reggae-Pop", "Karaoke", "Celtic", "IDM", "Cha-Cha", "Speech",
"Italo-Disco", "Free Improvisation", "Power Pop", "Flamenco", "Reggae", "Nu Metal",
"Bolero", "Latin", "Post-Modern", "Avant-garde Jazz", "Darkwave", "Mambo", "Military",
"Hi NRG", "Brass Band", "Education", "Conscious", "Dub", "Ska", "Free Jazz", "Mod",
"Ghazal", "Rumba", "Hard Bop", "Future Jazz", "Chinese Classical", "Hardcore",
"Krautrock", "Berlin-School", "Bluegrass", "Lo-Fi", "Public Broadcast", "Progressive House",
"Thug Rap", "Pop Punk", "AOR", "New Jack Swing", "Minneapolis Sound", "Britpop",
"Grunge", "Twist", "Sound Collage", "Medieval", "Post-Punk", "Canzone Napoletana",
"Salsa", "Shidaiqu", "Copla", "Acid Rock", "Acid Jazz", "Calypso", "Bengali Music",
"Impressionist", "Goth Rock", "Modal", "Polka", "Rock Opera", "Volksmusik",
"Country Blues", "Eurodance", "Post Bop", "Qawwali", "City Pop", "Boogie",
"Ethereal", "Dubstep", "Bubblegum", "Electro House", "Sound Art", "Afro-Cuban Jazz",
"Technical", "Electric Blues", "Roots Reggae", "Space Rock", "Southern Rock",
"Afrobeat", "Mariachi", "Pacific", "Thrash", "Neo Soul", "Acid", "Chillwave",
"Freestyle", "Happy Hardcore", "Shoegaze", "Progressive Trance", "Tech House",
"Cantopop", "Funk Metal", "African", "Ragga", "K-pop", "Folk", "Gospel", "Britcore",
"Tech House", "Soul-Jazz", "Ska", "Jungle", "Phonk", "Spoken Word", "Classical",
"Metalcore", "Ghetto", "P.Funk", "Italodance", "Witch House", "Avantgarde",
"Breakcore", "Happy Hardcore", "Psychedelic", "Tribal", "Acid", "Minimal", "Novelty",
"Chiptune", "Jazzdance", "Pop Punk", "Hi NRG", "Dark Ambient", "Schlager", "Juke",
"Art Rock", "Theme", "Garage Rock", "Grunge", "Hard Trance", "Swingbeat", "Easy Listening",
"Synthwave", "Illbient", "Sound Collage", "Beatbox", "Hard House", "Post-Punk",
"Post Rock", "Smooth Jazz", "Power Pop", "Italo-Disco", "Tribal House", "Score",
"Thrash", "Progressive Trance", "Salsa", "Modern Classical", "Arena Rock", "Drone",
"Bhangra", "Nu-Disco", "Roots Reggae", "Swing", "Prog Rock", "Glitch Hop", "Merengue",
"Cumbia", "Interview", "Samba", "Shoegaze", "Poetry", "Darkwave", "Video Game Music",
"Tropical House", "Bassline", "EBM", "Euro-Disco", "Afro-Cuban", "Rhythmic Noise",
"Avant-garde Jazz", "New Age", "Free Jazz", "Metalcore", "MPB", "Jazz-Rock", "Glam",
"Lounge", "Big Band", "Latin Jazz", "Hyperpop", "Death Metal", "Cool Jazz",
"Alt-Pop", "Bubblegum", "Grindcore", "Baltimore Club", "Religious", "AOR",
"Mandopop", "Black Metal", "Goth Rock", "Hardstyle", "Free Improvisation", "New Beat",
"Dialogue", "Bossa Nova", "Gabber", "Musique Concrète", "Contemporary", "Surf",
"Eurobeat", "Beat", "Flamenco", "Footwork", "Free Funk", "Rockabilly", "Zouk", "Soca",
"UK Street Soul", "Field Recording", "Dub Techno", "Raï", "Ethereal", "Cubano",
"Speed Garage", "Ghettotech", "Southern Rock", "Latin Pop", "Stoner Rock", "Rumba",
"Bossanova", "Low Bap", "Beatdown", "Classical", "Electric Blues", "Electroclash",
"Italo House", "Political", "Speedcore", "Afro-Cuban Jazz", "Brass Band", "Power Electronics",
"Space-Age", "Space Rock", "Celtic", "Ghetto House", "Krautrock", "Symphonic Rock",
"Jersey Club", "Ethno-pop", "Skweee", "Alternative Metal", "Post-Hardcore", "Musical",
"Neofolk", "Anison", "Special Effects", "Dream Pop", "Pacific", "Speech", "Math Rock",
"Promotional", "Rocksteady", "Bluegrass", "Low Bap", "Beatdown", "Swing", "Grunge",
"Big Beat", "Ambient", "Trance", "Vaporwave"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Latin
latin_style = [
"Bolero", "Salsa", "Cumbia", "Ballad", "MPB", "Samba", "Tango", "Latin Jazz",
"Cha-Cha", "Merengue", "Vocal", "Rumba", "Flamenco", "Ranchera", "Easy Listening",
"Mambo", "Pop Rock", "Folk", "Bossanova", "Guaracha", "Afro-Cuban", "Son",
"Bossa Nova", "Disco", "Funk", "Guaguancó", "Latin", "Chanson", "Mariachi",
"House", "Soul", "African", "Reggaeton", "Vallenato", "Cubano", "Norteño",
"Rock & Roll", "Forró", "Corrido", "Europop", "Porro", "Boogaloo", "Soundtrack",
"Tejano", "Synth-pop", "Fusion", "Pachanga", "Descarga", "Psychedelic Rock", "Guajira",
"Alternative Rock", "Son Montuno", "Beat", "Afro-Cuban Jazz", "Big Band", "Euro House",
"Downtempo", "Schlager", "Charanga", "Soft Rock", "Beguine", "Jazz-Funk", "Dance-pop",
"Nueva Cancion", "Polka", "Swing", "Calypso", "Andean Music", "Gospel", "Electro",
"Bachata", "Folk Rock", "Danzon", "Compas", "Conjunto", "Música Criolla", "Holiday",
"Batucada", "Contemporary Jazz", "Experimental", "Latin Pop", "Pop Rap", "Reggae",
"Soul-Jazz", "Ska", "Acoustic", "Garage Rock", "Quechua", "Copla", "Psychedelic",
"Pasodoble", "Blues Rock", "Classic Rock", "Lambada", "Rhythm & Blues", "Instrumental",
"Country", "RnB/Swing", "Baião", "Axé", "Choro", "Plena", "Religious", "Gangsta",
"Huayno", "Afrobeat", "Samba-Canção", "Soukous", "Prog Rock", "Theme", "Nueva Trova",
"Hip Hop", "Jazz-Rock", "Trova", "Indie Rock", "Eurodance", "Smooth Jazz", "Romantic",
"Techno", "Gaita", "Classical", "Reggae-Pop", "Musette", "Dub", "Surf", "Ambient",
"Punk", "Zouk", "Chamamé", "Space-Age", "Twist", "Joropo", "Hard Rock", "Deep House",
"Zamba", "New Wave", "Future Jazz", "Contemporary R&B", "Trance", "Chacarera", "Score",
"Contemporary", "Dancehall", "Marimba", "Indie Pop", "Timba", "Freestyle", "Sertanejo",
"Cool Jazz", "Banda", "Electro House", "Trip Hop", "Comedy", "Lounge", "Boogie", "Jibaro",
"Tribal", "Soca", "Acid Jazz", "Light Music", "Fado", "Italodance", "Country Rock",
"Guarania", "Breakbeat", "Trap", "Marcha Carnavalesca", "Milonga", "Hip-House",
"Drum n Bass", "Bomba", "Italo-Disco", "Tribal House", "Canzone Napoletana", "Modern",
"Progressive House", "Rockabilly", "Parody", "Candombe", "Avantgarde", "Jazzdance",
"Marches", "Breaks", "Musical", "Conscious", "Poetry", "Aguinaldo", "Favela Funk",
"Kayōkyoku", "Novelty", "Art Rock", "Broken Beat", "Leftfield", "Spoken Word", "New Age",
"Abstract", "Bambuco", "Champeta", "Highlife", "Thug Rap", "Ragga", "Cuatro", "Carimbó",
"Doo Wop", "Gypsy Jazz", "Ragga HipHop", "Bass Music", "Seresta", "Dixieland", "Caipira",
"Neo Soul", "G-Funk", "Tech House", "Sonero", "AOR", "Educational", "Bop", "Opera",
"City Pop", "Roots Reggae", "Liscio", "Heavy Metal", "Pacific", "Hardcore", "Brass Band",
"Free Jazz", "Avant-garde Jazz", "Steel Band", "Morna", "Yé-Yé", "Tropical House",
"Jazzy Hip-Hop", "Garage House", "Hardcore Hip-Hop", "Frevo", "Free Improvisation",
"Field Recording", "Big Beat", "Promotional", "Villancicos", "Political", "Euro-Disco",
"Hi NRG", "Kaseko", "J-pop", "Baroque", "Laïkó", "Bubblegum", "Modal", "Modern Classical",
"Celtic", "Exotica", "Romani", "Music Hall", "Catalan Music", "Post-Punk", "Zarzuela",
"Aboriginal", "Choral", "Lo-Fi", "Ragtime", "Go-Go", "Neo-Classical", "Mod", "Dubstep",
"Interview", "Post Bop", "Cut-up/DJ", "Arena Rock", "Operetta", "Symphonic Rock",
"Rocksteady", "Hard Bop", "UK Garage", "Pop Punk", "Story", "Glam", "Education", "Power Pop",
"Hard House", "Klezmer", "Hawaiian", "Jota", "Free Funk", "Industrial", "Ethno-pop",
"Monolog", "Nu Metal", "Acid Rock", "Nu-Disco"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Reagge
reggae_style = [
"Dancehall", "Reggae", "Roots Reggae", "Dub", "Ska", "Reggae-Pop", "Rocksteady",
"Lovers Rock", "Calypso", "Ragga", "Pop Rock", "Soca", "Disco", "Soul", "Punk",
"House", "Funk", "Synth-pop", "Ragga HipHop", "Alternative Rock", "Downtempo",
"Euro House", "New Wave", "Ballad", "Electro", "African", "Pop Rap", "RnB/Swing",
"Hip Hop", "Europop", "Rhythm & Blues", "Indie Rock", "Vocal", "Experimental",
"Dubstep", "Reggaeton", "Drum n Bass", "Folk Rock", "Rock & Roll", "Folk", "Soft Rock",
"Dance-pop", "Steel Band", "Jungle", "Contemporary R&B", "Soundtrack", "Chanson",
"Classic Rock", "Afrobeat", "Blues Rock", "Hardcore", "Acoustic", "Reggae Gospel",
"Eurodance", "Breakbeat", "Latin", "Conscious", "Holiday", "Trip Hop", "Techno",
"Ambient", "Dub Poetry", "Gospel", "Hard Rock", "Trance", "Psychedelic Rock", "Toasting",
"Cumbia", "Leftfield", "Breaks", "Salsa", "Mento", "Zouk", "Samba", "Indie Pop", "Abstract",
"Post-Punk", "Deep House", "Tribal", "Instrumental", "Country", "Easy Listening",
"Jazz-Funk", "Acid Jazz", "Gangsta", "MPB", "Country Rock", "Afro-Cuban", "Prog Rock",
"Fusion", "Neo Soul", "Highlife", "Boogie", "Soul-Jazz", "Electro House", "Merengue",
"UK Garage", "Power Pop", "Hip-House", "Cut-up/DJ", "Chutney", "Heavy Metal", "Progressive House",
"Grime", "Industrial", "Italodance", "Trap", "Art Rock", "Big Beat", "Latin Jazz", "Schlager",
"Bass Music", "Avantgarde", "Garage House", "Dub Techno", "Italo-Disco", "Garage Rock",
"Jazzy Hip-Hop", "Rockabilly", "Surf", "J-pop", "Contemporary Jazz", "Glam", "Psychedelic",
"Parody", "Future Jazz", "Rumba", "Cha-Cha", "Séga", "Beat", "Swing", "Pop Punk", "Theme",
"Novelty", "Smooth Jazz", "Axé", "Nu Metal", "Jazz-Rock", "Minimal", "Broken Beat", "Pacific",
"Funk Metal", "Hardcore Hip-Hop", "Hi NRG", "IDM", "Thug Rap", "Bolero", "Compas", "Freestyle",
"Bossanova", "Mod", "Post Rock", "Hindustani", "Oi", "Britpop", "Tech House", "Arena Rock",
"Noise", "Afro-Cuban Jazz", "Big Band", "Bossa Nova", "Lo-Fi", "Pachanga", "Boom Bap", "Mambo",
"Acid", "Spoken Word", "Breakcore", "Acid House", "Happy Hardcore", "Flamenco", "Doo Wop",
"Comedy", "Soukous", "New Jack Swing", "Jazzdance", "Euro-Disco", "Tribal House", "New Age",
"Junkanoo", "Rapso", "Batucada", "Beguine", "Raï", "AOR", "Bubbling", "Interview", "Contemporary",
"Chiptune", "Modern Classical", "Tropical House", "Score", "Aboriginal", "Space Rock", "Bhangra",
"Grunge", "Thrash", "Hawaiian", "UK Street Soul", "Lounge", "Cool Jazz", "Stoner Rock", "Tango",
"Lambada", "Glitch", "Celtic", "Religious", "Son", "Bounce", "Boogaloo"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Blues
blues_style = [
"Blues Rock", "Rhythm & Blues", "Rock & Roll", "Electric Blues", "Country Blues",
"Chicago Blues", "Soul", "Pop Rock", "Classic Rock", "Folk", "Vocal", "Psychedelic Rock",
"Folk Rock", "Piano Blues", "Delta Blues", "Modern Electric Blues", "Ballad", "Country",
"Country Rock", "Acoustic", "Gospel", "Swing", "Hard Rock", "Harmonica Blues",
"Alternative Rock", "Texas Blues", "Jump Blues", "Garage Rock", "Funk", "Doo Wop",
"Louisiana Blues", "Boogie Woogie", "Soul-Jazz", "Southern Rock", "Rockabilly", "Experimental",
"Easy Listening", "Big Band", "Indie Rock", "Soft Rock", "Soundtrack", "Prog Rock", "Jazz-Rock",
"Chanson", "Beat", "Punk", "Dixieland", "Bluegrass", "Avantgarde", "Contemporary Jazz",
"Ragtime", "Fusion", "Holiday", "Synth-pop", "Disco", "Jazz-Funk", "Memphis Blues", "Lo-Fi",
"East Coast Blues", "Art Rock", "Downtempo", "Cool Jazz", "Smooth Jazz", "Bop", "African",
"Stoner Rock", "Surf", "Piedmont Blues", "Mod", "New Wave", "Ambient", "Zydeco", "Ska",
"Heavy Metal", "Instrumental", "Cajun", "Free Improvisation", "Electro", "Abstract", "Contemporary R&B",
"Acid Rock", "House", "Indie Pop", "Bayou Funk", "Europop", "Schlager", "Pub Rock", "Arena Rock",
"Psychedelic", "Latin Jazz", "Noise", "Neo Soul", "Spoken Word", "Theme", "Score", "Reggae",
"Pop Rap", "Glam", "Honky Tonk", "Power Pop", "Twist", "AOR", "Hard Bop", "Novelty", "RnB/Swing",
"Comedy", "Parody", "Hip Hop", "Field Recording", "Free Jazz", "Lounge", "Classical", "Swamp Pop",
"Religious", "Bossa Nova", "Public Broadcast", "Trip Hop", "Interview", "Post-Punk", "Space Rock",
"Post Bop", "Post Rock", "Industrial", "Calypso", "Dance-pop", "Musical", "Celtic", "Avant-garde Jazz",
"Western Swing", "Tango", "Contemporary", "Jug Band", "Afrobeat", "Hillbilly", "Grunge", "Poetry",
"Samba", "Symphonic Rock", "Psychobilly", "Hill Country Blues", "Krautrock", "Skiffle", "MPB",
"Techno", "Reggae-Pop", "Doom Metal", "Boogie", "Neofolk", "Mambo", "Appalachian Music", "Bolero",
"Conscious", "Cha-Cha", "Flamenco", "Romantic", "Leftfield", "Afro-Cuban Jazz", "Gypsy Jazz", "Hardcore",
"Breakbeat", "Euro House", "Drone", "Acid Jazz", "Rumba", "New Age", "Minimal", "Latin", "Goth Rock",
"Bossanova", "Modern Classical", "Modern", "Future Jazz", "J-pop", "Afro-Cuban", "Modal", "Drum n Bass",
"Jazzy Hip-Hop", "Dialogue", "Kayōkyoku", "Education", "Light Music", "Thrash", "Brass Band", "Shoegaze",
"Free Funk", "Polka", "Space-Age", "Trance", "Stride", "Ethereal", "Funk Metal", "Deep House", "Music Hall",
"Spirituals", "Neo-Classical", "Black Metal", "Britpop", "Pop Punk", "Dark Ambient", "Salsa", "Rocksteady",
"Cumbia", "IDM", "Political", "Breaks", "Gangsta", "Pacific", "Big Beat", "Eurodance", "Opera", "Éntekhno",
"Nordic", "Roots Reggae", "Speech", "Death Metal", "Volksmusik", "Swingbeat", "Cut-up/DJ", "Erotic",
"Darkwave", "Hawaiian", "Highlife", "Freestyle", "Emo", "Baroque", "Electro House", "Sermon", "Boom Bap",
"Conjunto", "New Jack Swing", "P.Funk", "Yé-Yé", "Indian Classical", "Tejano", "Acid", "Cantopop",
"Griot", "Musique Concrète", "Thug Rap"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Non music
non_music_style = [
"Comedy", "Spoken Word", "Radioplay", "Field Recording", "Experimental", "Audiobook", "Poetry",
"Religious", "Interview", "Noise", "Education", "Story", "Ambient", "Dialogue", "Abstract",
"Promotional", "Monolog", "Speech", "Folk", "Political", "Drone", "Special Effects", "Soundtrack",
"Public Broadcast", "Sound Art", "Therapy", "Vocal", "Pop Rock", "Industrial", "Musique Concrète",
"Parody", "Chanson", "Sermon", "Avantgarde", "Dark Ambient", "New Age", "Alternative Rock", "Technical",
"Novelty", "Gospel", "Punk", "Synth-pop", "Minimal", "Ballad", "Health-Fitness", "Country", "Rock & Roll",
"Classical", "Free Improvisation", "Psychedelic Rock", "Holiday", "Acoustic", "Movie Effects", "Sound Collage",
"Educational", "Easy Listening", "Schlager", "Lo-Fi", "Sound Poetry", "Contemporary", "Harsh Noise Wall",
"Classic Rock", "Folk Rock", "Electro", "Indie Rock", "Power Electronics", "Soul", "Public Service Announcement",
"Disco", "Hard Rock", "Downtempo", "Techno", "Musical", "Prog Rock", "Modern Classical", "Art Rock", "Theme",
"New Wave", "Erotic", "Funk", "Score", "Leftfield", "Romantic", "Blues Rock", "Hardcore", "Grindcore",
"Nursery Rhymes", "Heavy Metal", "House", "Modern", "Choral", "Rhythmic Noise", "Soft Rock", "Glitch",
"Medical", "Free Jazz", "Big Band", "Avant-garde Jazz", "IDM", "Marches", "Contemporary Jazz", "Military",
"Electroacoustic", "Volksmusik", "African", "Swing", "Baroque", "Rhythm & Blues", "Garage Rock", "Hip Hop",
"Country Rock", "Black Metal", "Europop", "Post-Punk", "Opera", "Beat", "Pop Rap", "Post Rock", "Dub",
"Goregrind", "Trip Hop", "Noisecore", "Music Hall", "Tribal", "Breakbeat", "Breakcore", "Vaporwave", "Surf",
"Jazz-Funk", "Neo-Classical", "Darkwave", "Krautrock", "Acid", "Thrash", "Fusion", "Neofolk", "Indie Pop",
"Jazz-Rock", "Conscious", "Trance", "Drum n Bass", "Instrumental", "Chiptune", "Cabaret", "Rockabilly",
"Freestyle", "Dance-pop", "Celtic", "Medieval", "Cut-up/DJ", "Doom Metal", "J-pop", "Death Metal", "No Wave",
"Cool Jazz", "Ethereal", "Goth Rock", "Occult", "Bluegrass", "Glam", "Light Music", "Anison", "Illbient",
"Dixieland", "Arena Rock", "Post-Modern", "Euro House", "EBM", "Space Rock", "Brass Band", "Country Blues",
"Broken Beat", "Indian Classical", "Psychedelic", "Grunge", "RnB/Swing", "Breaks", "Video Game Music", "Shoegaze",
"Power Pop", "Hindustani", "Smooth Jazz", "Soul-Jazz", "Gangsta", "Contemporary R&B", "Polka", "Synthwave",
"Lounge", "Aboriginal", "Space-Age", "Tango", "Nordic", "Future Jazz", "Ska", "Gabber", "Bop", "Reggae",
"Vaudeville", "Tech House", "Deep House", "DJ Battle Tool", "Doo Wop", "Symphonic Rock", "Renaissance", "Dubstep",
"Speedcore", "Ragtime", "Samba", "Pacific", "MPB", "Flamenco", "Acid Jazz", "Dungeon Synth", "Kayōkyoku", "Emo",
"Acid Rock", "Stoner Rock", "Jungle", "Electric Blues", "Berlin-School", "Britpop", "Latin Jazz", "Jazzy Hip-Hop",
"Big Beat", "Trap", "Nu Metal", "Southern Rock", "Neo-Romantic", "Dub Techno", "Chillwave", "Post Bop", "Thug Rap",
"AOR", "Sludge Metal", "Eurodance", "Impressionist", "Break-In", "Pop Punk", "Witch House", "Acid House",
"Latin", "Operetta", "Batucada", "Early", "Bass Music", "Delta Blues", "Hardcore Hip-Hop", "Plunderphonics",
"Salsa", "Bossa Nova", "Progressive House", "Roots Reggae", "Crust", "Reggae-Pop", "Happy Hardcore", "Karaoke",
"Math Rock", "Rumba", "Cha-Cha", "Minimal Techno", "Népzene", "Afrobeat", "Psy-Trance", "Turntablism",
"Italo-Disco", "Nueva Cancion", "Calypso", "Modal", "Éntekhno", "Boom Bap"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>children
children_style = [
"Story", "Radioplay", "Nursery Rhymes", "Educational", "Holiday", "Soundtrack", "Vocal", "Audiobook",
"Folk", "Spoken Word", "Chanson", "Theme", "Religious", "Novelty", "Musical", "Ballad", "Choral", "Pop Rock",
"Comedy", "Schlager", "Europop", "Classical", "Education", "Score", "Poetry", "Gospel", "Synth-pop", "Disco",
"Country", "Experimental", "Romantic", "Dialogue", "Modern", "Easy Listening", "Parody", "Dance-pop", "Rock & Roll",
"Contemporary", "Euro House", "Folk Rock", "Pop Rap", "Promotional", "Acoustic", "Funk", "Special Effects",
"Alternative Rock", "Villancicos", "Volksmusik", "Bubblegum", "Ambient", "Soft Rock", "MPB", "Marches", "Anison",
"Opera", "Soul", "Abstract", "Field Recording", "Electro", "Karaoke", "Punk", "Indie Rock", "Speech", "Big Band",
"House", "African", "Népzene", "Indie Pop", "Baroque", "Monolog", "Health-Fitness", "Mandopop", "Catalan Music",
"Instrumental", "Prog Rock", "Eurodance", "Celtic", "Psychedelic Rock", "Avantgarde", "Kayōkyoku", "Lo-Fi", "Light Music",
"Swing", "New Age", "Political", "J-pop", "Therapy", "Interview", "RnB/Swing", "Music Hall", "Contemporary Jazz",
"New Wave", "Polka", "Blues Rock", "Techno", "Beat", "Country Rock", "Rhythm & Blues", "Garage Rock", "Neo-Classical",
"Classic Rock", "Italo-Disco", "Nordic", "Reggae", "Samba", "Downtempo", "Art Rock", "Ska", "Hard Rock", "Hip Hop",
"Latin", "Minimal", "Surf", "Movie Effects", "Noise", "Bluegrass", "Power Pop", "Cool Jazz", "Contemporary R&B",
"Heavy Metal", "Leftfield", "Brass Band", "Tango", "Pop Punk", "Video Game Music", "Éntekhno", "Dixieland", "Reggae-Pop",
"Modern Classical", "Calypso", "Cumbia", "Free Improvisation", "Happy Hardcore", "Psychedelic", "Impressionist",
"Military", "Lambada", "Italodance", "Jazz-Funk", "Trance", "Freestyle", "Jazz-Rock", "Twist", "Neo-Romantic",
"Sea Shanties", "Breakbeat", "Horror Rock", "Musique Concrète", "Sound Poetry", "Technical"
]



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Brass
military_style = [
"Marches", "Brass Band", "Military", "Folk", "Polka", "Volksmusik", "Pipe & Drum", "Vocal", "Political", "Schlager",
"Classical", "Instrumental", "Religious", "Romantic", "Big Band", "Easy Listening", "Soundtrack", "Modern", "Contemporary",
"Choral", "Holiday", "Industrial", "Spoken Word", "Theme", "Ballad", "Experimental", "Speech", "Score", "Dark Ambient",
"Baroque", "Chanson", "Celtic", "Swing", "Neofolk", "Dixieland", "Ragtime", "Neo-Classical", "Pasodoble", "Field Recording",
"Pop Rock", "Novelty", "Ambient", "Opera", "Gospel", "Musical", "Comedy", "Country", "Tango", "Guggenmusik", "Light Music",
"Romani", "Noise", "Disco", "Kolo", "Promotional", "Jazz-Funk", "Funk", "Modern Classical", "Education", "Abstract",
"Samba", "Music Hall", "Operetta", "Parody", "Folk Rock", "Synth-pop", "Rock & Roll", "Dialogue", "Electro", "Soul",
"Punk", "Renaissance", "Alternative Rock", "Flamenco", "Educational", "Poetry", "Acoustic", "Contemporary Jazz", "African",
"Neo-Romantic", "Sea Shanties", "House", "Bolero", "Monolog", "Techno", "Rumba", "Rhythm & Blues", "Gypsy Jazz", "Drone",
"Avantgarde"
]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Disct

#%%
genres_styles = {
    "Rock" : rock_style,
    "Electronic" : electronic_style,
    "Pop" : pop_style,
    "Folk_World_&_Country" : world_style,
    "Jazz" : jazz_style,
    "Funk_Soul" : funk_soul_style,
    "Classical" : classical_style,
    "Hip_Hop" : hip_hop_style,
    "Latin" : latin_style,
    "Stage_&_Screen" : stage_style,
    "Reggae" : reggae_style,
    "Blues" : blues_style,
    "Non_Music" : non_music_style,
    "Children's" : children_style,
    "Brass_&_Military " : military_style
    }

     

print("list_styles.py loaded successfully")

#%%
#Création tableau
tableau_genre = pd.DataFrame.from_dict(genres_styles, orient='index').transpose()

tableau_genre.to_csv("tableau_genre.csv")

print("tableau créé")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>> TO bigquery
project_id = "discogs-random-selecta"
table_id = "discogs-random-selecta.my_data.tableau_genre"

pandas_gbq.to_gbq(tableau_genre, table_id, project_id)

print("tableau exporté")

#%%
tableau_genre

#%%
genres_styles.values()

#%%
genres_styles["Electronic"]

#%%

# %%

