class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

MediaPlayer.play(media1)
MediaPlayer.play(media2)
