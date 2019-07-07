# Website-Blocker
A python script that can be used to block access to certain websites during user specified working hours
## Steps to run:
### Linux or Mac
- Run crontab using the following command
```
sudo crontab -e
```
- Add the following line (without the angular brackers) at the end of the cron table file that shows up
```
@reboot python3 <path/of/this/script/website_blocker.py>
```
- Save and exit from the editor
