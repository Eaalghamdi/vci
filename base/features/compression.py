import ffmpeg
import os
import provider as Provider

DIRECTORY = str(os.path.dirname(os.path.abspath(__file__)))
DATABASE_ROOT = DIRECTORY.replace('features', 'src')


def video_comp(videoPath, videoDir, widthD, heightD, fps, fileFormat):
    input = ffmpeg.input(
        videoPath)
    audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
    video = input.video.filter('scale', width=widthD, height=heightD)
    video = input.video.filter("fps", fps)
    out = ffmpeg.output(
        audio, video, (videoDir + '/test.' + fileFormat))
    out.run(
        cmd=(DATABASE_ROOT + '/ffmpeg/ffmpeg'))

    return 1


def add_to_db(videoPath, videoDir, fileFormat):
    head, tail = os.path.split(videoPath)
    # in bytes
    prevSize = os.path.getsize(videoPath)
    newSize = os.path.getsize((videoDir + '/test.' + fileFormat))

    Provider.insert_compression(
        [tail, fileFormat, prevSize, newSize])

    return 1


def compression(videoPath, videoDir, widthD, heightD, fps, fileFormat):

    if video_comp(videoPath, videoDir, widthD, heightD, fps, fileFormat) == 1:
        if add_to_db(videoPath, videoDir, fileFormat) == 1:
            os.remove((videoDir + '/test.' + fileFormat))
            return "completed"
