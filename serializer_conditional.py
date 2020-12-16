import json
import xml.etree.ElementTree as et
import logging
logging.basicConfig(filename='out.log', level=logging.DEBUG,format='%(asctime)s %(message)s')


class Song:
    # Constructor to create a Song object.
    def __init__(self, songId, title, artist, genre, year):
        self.songId = songId
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year
        logging.info("-- Song Conditional Object Constructed for songId: {}".format(self.songId))

class SongSerializer:
    
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                "id" : song.songId,
                "title": song.title,
                "artist": song.artist,
                "genre": song.genre,
                "year": song.year
            }
            logging.info("-- Conditional: Song Object Converted to JSON for songId: {}".format(song.songId))
            return json.dumps(song_info)
            
        elif format == "XML":
            song_info = et.Element("song", attrib={"id": song.songId})
            title = et.SubElement(song_info, "title")
            title.text = song.title

            artist = et.SubElement(song_info, "artist")
            artist.text = song.artist
            
            genre = et.SubElement(song_info, "genre")
            genre.text = song.genre
            
            year = et.SubElement(song_info, "year")
            year.text = song.year
            logging.info("-- Conditional: Song Object Converted to XML for songId: {}".format(song.songId))

            return et.tostring(song_info, encoding="unicode")
        
        else:
            logging.info("-- Error: Format '{}' not supported".format(format))
            raise ValueError(format)
