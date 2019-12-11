build-backend: 
	docker build -t sophia-backend ./backend

serve-backend: build-backend
	docker run \
		--name sophia-backend \
		--rm \
		--interactive \
		--tty \
		--volume=$$(pwd)/backend:/app/ \
		--publish 80:80 \
		sophia-backend

test-backend: build-backend
	docker run \
		--name sophia-backend \
		--rm \
		--interactive \
		--tty \
		--volume=$$(pwd)/backend:/app/ \
		--publish 80:80 \
		sophia-backend \
		bash -c 'pytest -v'

