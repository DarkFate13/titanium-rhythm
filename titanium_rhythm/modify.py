import eyed3

class Song:
	def __init__(self, filepath):
		self.filepath = filepath
		self.audiofile = eyed3.load(filepath)
	
	def modify(self, title = None, artist = None, album = None, genre = None, lyrics = None):
		
		if(title is not None):
			self.audiofile.tag.title = title
		if(artist is not None):
			self.audiofile.tag.artist = artist
		if(album is not None):
			self.audiofile.tag.album = album
		if(genre is not None):
			self.audiofile.tag.genre = genre
		if(lyrics is not None):
			self.audiofile.tag.lyrics.set(lyrics)
		
		self.audiofile.tag.save()
		
	def get_tag(self):
		tag_info = dict()
		tag_info['title'] = self.audiofile.tag.title
		tag_info['artist'] = self.audiofile.tag.artist 
		tag_info['album'] = self.audiofile.tag.album 
		tag_info['genre'] = self.audiofile.tag.genre
		tag_info['lyrics'] = self.audiofile.tag.lyrics[0].text
		
		return tag_info
		