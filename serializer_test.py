import serializer_conditional as sc
import serializer_refactored as sr
import serializer_factory as sf

### Testing Conditional Class:

song1 = sc.Song("123", "Sweet home Alabama", "Lynard Skynard", "Rap", "1974")
song2 = sc.Song("234", "Jingle Bell Rock", "Bobby Helms", "Holiday", "1970")
song3 = sc.Song("345", "Till I Collapse", "Eminem", "Rap", "2002")

scs = sc.SongSerializer()
scs.serialize(song1, "JSON")
scs.serialize(song2, "JSON")
scs.serialize(song2, "XML")
scs.serialize(song3, "XML")
# serializer.serialize(song3, "HTML") #Should result in error


### Testing Refactored Class:

song1 = sr.Song("123", "Sweet home Alabama", "Lynard Skynard", "Rap", "1974")
song2 = sr.Song("234", "Jingle Bell Rock", "Bobby Helms", "Holiday", "1970")
song3 = sr.Song("345", "Till I Collapse", "Eminem", "Rap", "2002")

scf = sr.SongSerializer()
scf.serialize(song1, "JSON")
scf.serialize(song2, "XML")
scf.serialize(song3, "JSON")
