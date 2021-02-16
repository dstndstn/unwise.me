FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]
WORKDIR /app

RUN apt update && \
    apt upgrade -y && \
    apt install -y build-essential python3 python3-distutils python3-dev curl \
    git libpcre3 libpcre3-dev \
    pkg-config swig libcairo2-dev libnetpbm10-dev netpbm libpng-dev libjpeg-dev \
    zlib1g-dev libbz2-dev libcfitsio-dev wcslib-dev python3-pip && \
    apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
#    python3 get-pip.py && \
#    ln -s /usr/bin/python3 /usr/bin/python && \
#    pip install --no-cache-dir -r requirements.txt && \
#    pip install pyfits && \
#    pip install -e git+http://github.com/dstndstn/astrometry.net@23579ec66cf38547264ef058204fc36abdcb40c4#egg=astrometry --log LOG_FILE

# COPY . /app
# 
# RUN cd tractor && make && \
#     cd /app && \
#     export PYTHONPATH=$(pwd)/legacypipe/py:$PYTHONPATH && \
#     export PYTHONPATH=$(pwd)/tractor:$PYTHONPATH && \
#     export PYTHONPATH=$(pwd)/decals-web:$PYTHONPATH && \
#     cd decals-web && \
#     python3 manage.py migrate && \
#     apt-get -y clean
# 
# EXPOSE 80
# 
# ENTRYPOINT ["/app/entry.sh"]
# #CMD ["python3", "decals-web/manage.py", "runserver", "0.0.0.0:8000"]
