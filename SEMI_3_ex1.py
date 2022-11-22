import os


# ref: https://stackoverflow.com/questions/11552565/vertically-or-horizontally-stack-mosaic-several-videos-using-ffmpeg
def compare(first, second, third, fourth, output):
    com = 'ffmpeg -i ' + first + ' -i ' + second + ' -i ' + third + ' -i ' + fourth + \
          ' -filter_complex ' \
          '"[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" ' \
          '-map "[v]" ' \
          + output
    os.system(com)


# per poder executar aquest codi hem de tenir primer els videos generats per l'ex 2
if __name__ == '__main__':
    # compare("BBB_720p_vp8.mkv", "BBB_720p_vp9.mp4", "BBB_720p_h265.mp4", "BBB_720p_av1.mp4", "compare_720p.mp4")
    # compare("BBB_480p_vp8.mkv", "BBB_480p_vp9.mp4", "BBB_480p_h265.mp4", "BBB_480p_av1.mp4", "compare_480p.mp4")
    # compare("BBB_360x240_vp8.mkv", "BBB_360x240_vp9.mp4", "BBB_360x240_h265.mp4", "BBB_360x240_av1.mp4",
    #         "compare_360x240.mp4")
    compare("BBB_160x120_vp8.mkv", "BBB_160x120_vp9.mp4", "BBB_160x120_h265.mp4", "BBB_160x120_av1.mkv",
            "compare_160x120.mp4")
