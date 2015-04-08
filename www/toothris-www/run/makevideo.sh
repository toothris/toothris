#!/bin/bash

set -e

URL="www.toothris.org"
GAME_WIDTH=800
GAME_HEIGHT=600
GAME_FPS=60
START_LEN=220
START_SIZE=80
DISPLAY=:1
SILENCE=2
TMPDIR=/var/tmp/toothris-www
WWW_SSHOT=3255

CODECS_MP4="-c:a libfdk_aac -b:a 384k \
            -c:v libx264 -crf 18 -pix_fmt yuv420p"
CODECS_OGG="-c:a libvorbis -qscale:a 8 \
            -c:v libtheora -qscale:v 8"
CODECS_WEBM="-c:a libvorbis -qscale:a 8 \
             -c:v libvpx -crf 4 -b:v 5M"
VID_OPTS="[ \
{'width': 320, 'height': 240, 'ext': 'mp4', 'codecs': '$CODECS_MP4'}, \
{'width': 854, 'height': 480, 'ext': 'mp4', 'codecs': '$CODECS_MP4'}, \
{'width': 800, 'height': 600, 'ext': 'mp4', 'codecs': '$CODECS_MP4'}, \
{'width': 800, 'height': 600, 'ext': 'ogg', 'codecs': '$CODECS_OGG'}, \
{'width': 800, 'height': 600, 'ext': 'webm', 'codecs': '$CODECS_WEBM'}]"

VID_OPTLEN=$(python2 -c "print len($VID_OPTS)")

export DISPLAY

xmp -d wav -o ${TMPDIR}/music.wav -b 16 -f 48000 \
  /toothris-www/run/artificial_sweetener.xm

rm -rf ${TMPDIR}/blank.bmp
convert -size ${GAME_WIDTH}x${GAME_HEIGHT} xc:black ${TMPDIR}/blank.bmp

FRAME=0
rm -rf ${TMPDIR}/start*.bmp
while [ $FRAME -lt $START_LEN ] ; do
  if [[ $((FRAME % 10)) -eq 0 ]] ; then
    echo "start frame $FRAME / $START_LEN" ;
  fi
  SCALE=$(python2 -c "print '%.2f' % \
    ($START_SIZE+((100.0-$START_SIZE)*$FRAME/$START_LEN))")
  convert \
    '(' '(' -background black -fill white -gravity center \
            -font /usr/share/fonts/TTF/DejaVuSansMono.ttf \
            -pointsize 90 label:"$URL" \
            -resize 1600x1200 ')' \
        -resize $SCALE% \
        -gravity center \
        -extent 1600x1200 ')' \
    -resize ${GAME_WIDTH}x${GAME_HEIGHT} \
    -gravity center \
    -extent ${GAME_WIDTH}x${GAME_HEIGHT} \
    $(printf "${TMPDIR}/start%06d.bmp" $FRAME)
  ((FRAME += 1))
done

Xvfb $DISPLAY -screen 0 ${GAME_WIDTH}x${GAME_HEIGHT}x24 &
XVFB=$!

while ! xset q &>/dev/null ; do
  echo "waiting for Xfvb..."
  sleep 1
done

rm -rf ${TMPDIR}/game*.bmp
set +e
toothris --width $GAME_WIDTH --height $GAME_HEIGHT --fps $GAME_FPS --freefps \
  --replay --events /toothris-www/run/demo.events \
  --frames "${TMPDIR}/game%06d.bmp"
set -e

kill $XVFB

cp $(printf "${TMPDIR}/game%06d.bmp" $WWW_SSHOT) ${TMPDIR}/sshot.bmp

for (( VID_OPTI=0; VID_OPTI<VID_OPTLEN; VID_OPTI++)) ; do
  VID_WIDTH=$( python2 -c "print $VID_OPTS[$VID_OPTI]['width']")
  VID_HEIGHT=$(python2 -c "print $VID_OPTS[$VID_OPTI]['height']")
  VID_EXT=$(   python2 -c "print $VID_OPTS[$VID_OPTI]['ext']")
  VID_CODECS=$(python2 -c "print $VID_OPTS[$VID_OPTI]['codecs']")
  IFS=","; set $(python2 -c \
   "wheight = ($VID_WIDTH * $GAME_HEIGHT) / $GAME_WIDTH; \
    hwidth = ($VID_HEIGHT * $GAME_WIDTH) / $GAME_HEIGHT; \
    width = $VID_WIDTH if wheight <= $VID_HEIGHT else hwidth; \
    height = $VID_HEIGHT if hwidth <= $VID_WIDTH else wheight; \
    xofs = ($VID_WIDTH - width) / 2; \
    yofs = ($VID_HEIGHT - height) / 2; \
    print '%i,%i,%i,%i' % (width, height, xofs, yofs)")
  INNER_WIDTH=$1
  INNER_HEIGHT=$2
  INNER_XOFS=$3
  INNER_YOFS=$4
  rm -rf ${TMPDIR}/toothris${VID_WIDTH}x${VID_HEIGHT}.${VID_EXT}
  CMD="ffmpeg \
    -i \"${TMPDIR}/music.wav\" \
    -loop 1 -t $SILENCE -r $GAME_FPS -i \"${TMPDIR}/blank.bmp\" \
    -r $GAME_FPS -i \"${TMPDIR}/start%06d.bmp\" \
    -r $GAME_FPS -i \"${TMPDIR}/game%06d.bmp\" \
    -loop 1 -t $SILENCE -r $GAME_FPS -i \"${TMPDIR}/start000000.bmp\" \
    -filter_complex \"
      [1:0] [2:0] [3:0] [4:0] concat=n=4:v=1:a=0 [rawv];
      [rawv] scale=${INNER_WIDTH}:${INNER_HEIGHT} [innerv];
      [innerv] pad=width=${VID_WIDTH}:height=${VID_HEIGHT} \
                  :x=${INNER_XOFS}:y=${INNER_YOFS}:color=black [v];
      aevalsrc=0|0:s=48000:d=${SILENCE} [silence1];
      aevalsrc=0|0:s=48000:d=${SILENCE} [silence2];
      [silence1] [0:0] [silence2] concat=n=3:v=0:a=1 [a]\" \
    -map \"[v]\" -map \"[a]\" $VID_CODECS \
    ${TMPDIR}/toothris${VID_WIDTH}x${VID_HEIGHT}.${VID_EXT}"
  echo "Running the following command:\n$CMD"
  eval $CMD
done

rm -rf ${TMPDIR}/{blank.bmp,start*.bmp,game*.bmp,music.wav}
