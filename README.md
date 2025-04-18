# ip2tg: IP to Telegram

Send local IP address to Telegram at computer startup.

## Setting up

Rename `sample.env` to `.env`, add your telegram bot credentials.

Rename `sample_ip2tg.service` to `ip2tg.service`, modify the paths respectively.

## Using `systemd service` to send IP address to Telegram at server startup

Copy the file `ip2tg.service` to `/etc/systemd/system` using `sudo`:

`$ sudo cp ip2tg.service /etc/systemd/system`

Enable and start the service:

```
$ sudo systemctl daemon-reexec
$ sudo systemctl daemon-reload
$ sudo systemctl enable ip2tg.service
$ sudo systemctl start ip2tg.service
```

Check status and logs:

```
$ sudo systemctl status ip2tg.service
$ journalctl -u ip2tg.service
```

## Alternatively, add to crontab

`$ crontab -e`

Add this:

`@reboot /usr/bin/python3 /path/to/your_script.py`

Make the script executable:

`$ chmod +x your_script.py`
