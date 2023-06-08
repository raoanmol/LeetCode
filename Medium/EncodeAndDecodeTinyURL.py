class Codec:

    def __init__(self):
        self.encMap = {}
        self.decMap = {}
        self.baseUrl = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encMap:
            shortUrl = self.baseUrl + str(len(self.encMap))
            self.encMap[longUrl] = shortUrl
            self.decMap[shortUrl] = longUrl

        return self.encMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        if shortUrl not in self.decMap:
            return "Invalid Value"
        
        return self.decMap[shortUrl]
