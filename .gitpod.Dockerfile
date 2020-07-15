FROM gitpod/workspace-full
RUN pip install Flask robin_stocks
RUN cd Python/
RUN python rh.py
# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/
