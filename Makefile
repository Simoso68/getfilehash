build:
	python3 build.py
clean:
	rm -f getfilehash
clean-cache:
	rm -rf src/__pycache__
install:
	sudo cp getfilehash /usr/bin/getfilehash
	sudo chmod +x /usr/bin/getfilehash