import os

# Video formats supported: H.264 video up to 1080p, 60 frames per second, 
# High Profile level 5.0 with AAC-LC audio up to 160 Kbps, 48kHz, stereo audio 
# in .m4v, .mp4, and .mov file formats; MPEG-4 video up to 2.5 Mbps, 640 by 480 pixels, 
# 30 frames per second, Simple Proﬁle with AAC-LC audio up to 160 Kbps per channel, 48kHz, 
# stereo audio in .m4v, .mp4, and .mov ﬁle formats; Motion JPEG (M-JPEG) up to 35 Mbps, 
# 1280 by 720 pixels, 30 frames per second, audio in ulaw, PCM stereo audio in .avi ﬁle format


file_path = raw_input('input the file path : ')
save_output_path = file_path.replace('.ts', '.mp4')

command = './HandBrakeCLI -i %s -o %s ' \
           '-e x264  -q 20.0 -r 30 --pfr  -a 1 -E faac -B 160 -6 dpl2 ' \
	   '-R Auto -D 0.0 --audio-copy-mask aac,ac3,dtshd,dts,mp3 ' \
	   '--audio-fallback ffac3 -f mp4 -4 -X 1280 -Y 720 --loose-anamorphic ' \
	   '--modulus 2 -m --x264-preset medium --h264-profile high --h264-level 3.1 '\
	   %(file_path, save_output_path)
os.system(command)
