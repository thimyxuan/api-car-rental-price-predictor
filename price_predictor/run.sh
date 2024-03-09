docker run -it\
 -p 8000:8000\
 -v "$(pwd):/home/app"\
 -e PORT=8000\
 predictor