FROM nginxinc/nginx-unprivileged

ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN apt update

RUN apt install -y --no-install-recommends \
    python3 \
    python3-pip \
    nano

RUN pip install --break-system-packages certbot certbot-nginx
RUN ln -s /opt/certbot/bin/certbot /usr/bin/certbot
RUN pip install --break-system-packages certbot-plugin-gandi

# Make /var/cache/nginx/ writable by non-root users
RUN mkdir -p /var/cache/nginx/client_temp
RUN chgrp -R nginx /var/cache/nginx/
RUN chmod -R g+w /var/cache/nginx/

USER nginx

