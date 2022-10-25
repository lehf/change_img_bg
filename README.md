# change_img_bg
change image's background use ai


### install rembg & pillow
```shell
python --verson # > 3.7
pip isntall rembg pillow 
```
### download model
All models are downloaded and saved in the user home folder in the ```.u2net``` directory
You can download [u2net](https://github.com/lehf/change_img_bg/releases/tag/u2net)

### usage
#### change background to color; default ```'#fff'```
```shell
python3 change_bg.py -i input_path -o output_path -b "#7bb8f1"
```
#### change background to image
```shell
python3 change_bg.py -i input_path -o output_path -b image_path
```
#### quietly
```shell
nohup python3 -u change_bg.py -i input_path -o output_path -b "#7bb8f1" > nohup.log 2>&1 &
```

