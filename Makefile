.PHONY: lint

lint:
	flake8

start:
	sh start_tunnel.sh
	sh start_bot.sh