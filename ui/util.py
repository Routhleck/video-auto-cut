# 将combobox中的值转换为可以用的值
def get_para(ui):
    # 视频尺寸
    video_scale_dict = {
        0: 'scale=1920:1080',
        1: 'scale=1280:720'
    }
    video_bitrate_dict = {
        0: '1000k',
        1: '2000k',
        2: '3000k',
        3: '4000k',
        4: '5000k',
        5: '6000k',
        6: '7000k',
        7: '8000k',
        8: '9000k',
        9: '10000k',
    }
    audio_bitrate_dict = {
        0: '128k',
        1: '192k',
        2: '256k',
        3: '512k'
    }
    audio_codec_dict = {
        0: 'aac',
        1: 'ogg',
        2: 'mp3'
    }
    preset_dict = {
        0: 'ultrafast',
        1: 'superfast',
        2: 'veryfast',
        3: 'faster',
        4: 'fast',
        5: 'medium',
        6: 'slow',
        7: 'slower',
        8: 'veryslow'
    }
    bitrate_encode_dict = {
        0: 'CBR4.1',
        1: 'VBR'
    }
    video_scale = video_scale_dict[ui.comboBox_scale.currentIndex()]
    video_bitrate = video_bitrate_dict[ui.comboBox_bitrate.currentIndex()]
    audio_bitrate = audio_bitrate_dict[ui.comboBox_audio_bitrate.currentIndex()]
    audio_codec = audio_codec_dict[ui.comboBox_audio_codec.currentIndex()]
    preset = preset_dict[ui.comboBox_preset.currentIndex()]
    bitrate_encode = bitrate_encode_dict[ui.comboBox_bitrate_encode.currentIndex()]
    return video_scale, video_bitrate, audio_bitrate, audio_codec, preset, bitrate_encode
