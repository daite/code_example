#!/bin/bash
url="$1"
user=$(echo $url | cut -d / -f5)
num=$(echo $url | cut -d / -f6)
down_url="http://jp.channel.pandora.tv/channel/video.ptv?ch_userid=$user&prgid=$num"
echo $down_url
youtube-dl $down_url -v
