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

build-frontend:
	docker build -t sophia-frontend ./frontend

serve-frontend: build-frontend
	docker run \
		--name sophia-frontend \
		--rm \
		--interactive \
		--tty \
		--volume=$$(pwd)/frontend:/app/ \
		--publish 3000:3000 \
		sophia-frontend

test-frontend: build-frontend
	docker run \
		--name sophia-frontend \
		--rm \
		--interactive \
		--tty \
		--volume=$$(pwd)/frontend:/app/ \
		--publish 3000:3000 \
		sophia-frontend \
		yarn test
