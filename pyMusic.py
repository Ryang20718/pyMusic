import sys
from youtube_dl import YoutubeDL
import os
from moviepy.editor import *
import csv

def mp4_to_mp3():
	path = "./"
	dirs = os.listdir( path )

	# This would print all the files and directories
	for file in dirs:
		if(file.endswith('.mp4')):
			input_file = os.path.join(os.getcwd(),file)
			base = str(file)
			base = base.replace(".mp4",".mp3")
			print(base)
			video = VideoFileClip(input_file)
			video.audio.write_audiofile(os.path.join(os.getcwd(),base))
			os.remove(file)

def read_in_from_txt():
	youtube_id_list = []
	with open('music.csv') as csv_file:
		reader = csv.reader(csv_file, delimiter=',')
		for row in reader:
			base = row[0].split("=")[1]
			youtube_id_list.append(base)
	return youtube_id_list

if __name__ == '__main__':
    if len(sys.argv) >= 0:
        ydl_opts = {}
        ydl = YoutubeDL(ydl_opts)
        ydl.download(read_in_from_txt())
        mp4_to_mp3()
    else:
        print("Enter list of urls to download")
        #mp4_to_mp3()
        read_in_from_txt()
        exit(0)



