import pafy
import urllib.request
from youtube_search import YoutubeSearch


def run(command, args, voice_instance):
    if command == "play":
        search_query = " ".join(args)
        result = YoutubeSearch(search_query, max_results=10).to_dict()[0]

        video_title = result["title"]
        url_suffix = result["url_suffix"]

        url = f"https://www.youtube.com/{url_suffix}"
        video = pafy.new(url)
        best = video.getbest()
        play_url = best.url

        voice_instance.say(f"playing {video_title}")
        voice_instance.play_media(play_url)