.SILENT:

build:
	docker build --tag blackjack:latest .

run: build
	docker run --rm -it --name blackjack -v $(CURDIR):/usr/src/app blackjack:v0.1