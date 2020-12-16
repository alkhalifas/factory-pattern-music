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
        logging.info("-- Factory: Song Object Constructed for songId: {}".format(self.songId))

class SongSerializer:
    
    def serialize(self, song, format):
        if format == 'JSON':
            return self._serialize_to_json(song)
        elif format == 'XML':
            return self._serialize_to_xml(song)
        else:
            logging.info("-- Refactored: Song Object Serialized for songId: {}".format(self.songId))
            raise ValueError(format)


    def _serialize_to_json(self, song):
            payload = {
                "id" : song.songId,
                "title": song.title,
                "artist": song.artist,
                "genre": song.genre,
                "year": song.year
            }
            logging.info("-- Refactored: Song Object Converted to JSON for songId: {}".format(song.songId))
            return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.songId})

        title = et.SubElement(song_element, 'title')
        title.text = song.title

        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist

        genre = et.SubElement(song_element, 'genre')
        genre.text = song.genre

        year = et.SubElement(song_element, 'year')
        year.text = song.year

        logging.info("-- Refactored: Song Object Converted to XML for songId: {}".format(song.songId))
        return et.tostring(song_element, encoding='unicode')