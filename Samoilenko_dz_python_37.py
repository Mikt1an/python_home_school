# 1

class AudioFileMixin:
    """
        Mixin that adds audio playback functionality.
    """
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError(f"Audio track audio_tracks does not exist")
        print(f"Playing audio {self.__class__.__name__}")
        for tracks in self.audio_tracks:
            print(tracks)

class VideoFileMixin:
    """
       Mixin that adds video playback functionality.
    """
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError(f"Video file video_files does not exist")
        print(f"Playing video {self.__class__.__name__}")
        for video in self.video_files:
            print(video)

class MediaPlayer(AudioFileMixin):
    """
        Media player with audio support.
    """
    def __init__(self, audio_files):
        self.audio_tracks = audio_files

class Laptop(AudioFileMixin, VideoFileMixin):
    """
        Laptop class with audio and video support.
    """
    def __init__(self, audio_files, video_files):
        self.audio_tracks = audio_files
        self.video_files = video_files

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]


M = MediaPlayer(tracks)
M.play_audio()
print()
L = Laptop(tracks, movies)
L.play_audio()
L.play_video()