sudo cp ./lcddisplay.service /lib/systemd/system/lcddisplay.service
sudo chmod 644 /lib/systemd/system/lcddisplay.service
sudo systemctl daemon-reload
sudo systemctl enable lcddisplay.service
sudo systemctl start lcddisplay.service
sudo systemctl status lcddisplay.service
