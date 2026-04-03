

def convert_numbers(playlist):
    total_seconds = 0
    
    for song in playlist:
        song["duration"] = [int(time) for time in song["duration"].split(":")]
        total_seconds += song["duration"][0] * 60 + song["duration"][1]
     
    minutes = total_seconds // 60
    seconds = total_seconds % 60 
    
    print(f"Duración total: {minutes}m  {seconds}s")
    return playlist

def largest_song(playlist):
    max_song = playlist[0]
    max_time_song = max_song["duration"][0] * 60 + max_song["duration"][1]
    
    for song in playlist:
        actual_song_duration = song["duration"][0] * 60 + song["duration"][1]
        if actual_song_duration > max_time_song:
            max_song = song
            max_time_song = max_song["duration"][0] * 60 + max_song["duration"][1]

    print(f"Cancion mas larga: {max_song["title"]} ({max_song["duration"][0]}m {max_song["duration"][1]}s)")
    
def shortest_song(playlist):
    min_song = playlist[0]
    min_time_song = min_song["duration"][0] * 60 + min_song["duration"][1]
    
    for song in playlist:
        actual_song_duration = song["duration"][0] * 60 + song["duration"][1]
        if actual_song_duration < min_time_song:
            min_song = song
            min_time_song = min_song["duration"][0] * 60 + min_song["duration"][1]
            
    print(f"Cancion mas corta: {min_song["title"]} ({min_song["duration"][0]}m {min_song["duration"][1]}s)")


def duration(playlist):
    convert_numbers(playlist)
    print()
    shortest_song(playlist)
    print()
    largest_song(playlist)