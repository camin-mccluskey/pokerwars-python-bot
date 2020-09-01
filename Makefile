.PHONY: lint start

lint:
	flake8

start:
	sh start_tunnel.sh &
	echo "Tunnel Open"
	# sleeping to give ngrok time to open the tunnel
	sleep 3
	sh start_bot.sh
	echo "Bot started"