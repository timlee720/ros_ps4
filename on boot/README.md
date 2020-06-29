# Guidelines for Autorun During the Startup

* Download the **one_click.bash** to Desktop

* Create / Open rc.local file
```bash
sudo vim /etc/rc.local
```
* Copy **rc-local.txt** content then exit (':wq')

* Enable & Start the rc-local.service
```bash
chmod +x /etc/rc.local  # ensure it's executable
sudo systemctl enable rc-local.service
sudo systemctl start rc-local.service
```

* Verify the configuration
```bash
sudo reboot
systemctl status rc-local.service
rostopic list
rostopic echo <any one from the below>
```
Topics to be used
> /omni_drive_control/cmd_vel   # manual mode

> /auto_topic   # semi-auto mode

> /cross_topic  # kick stage 1

> /circle_topic # kick stage 2

> /tri_topic    # push ball

> /option_topic # reset the rebot

> /l1_topic     # enter semi-mode

> /joy          # ps4 controller

Spare topics

> /square_topic

> /share_topic

> /ps_topic

> /r1_topic
