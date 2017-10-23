.PHONY: all clean build test mount_shell shell upload check-env

MUJOCO_LICENSE_PATH ?= ~/.mujoco/mjkey.txt

all: test

clean:
	rm -rf cyberglove.egg-info
	rm -rf */__pycache__
	rm -rf */*/__pycache__
	rm -rf dist
	rm -rf build

upload:
	rm -rf dist
	python setup.py sdist
	twine upload dist/*
