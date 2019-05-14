FROM sd2e/reactors:python3
# FROM sd2e/reactors:python3-edge

# reactor.py, config.yml, and message.jsonschema will be automatically
# added to the container when you run docker build or abaco deploy

RUN pip uninstall --yes agavepy

# Install from Repo
#RUN pip install --upgrade git+https://github.com/TACC/agavepy.git@aloe
RUN pip install --upgrade agavepy

#RUN export _abaco_access_token=94dcee9c76113147e183a2123b435e0
