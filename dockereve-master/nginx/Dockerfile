FROM nginx
COPY .ssl/mriqcep.crt /etc/ssl/certs/mriqcep-selfsigned.crt
COPY .ssl/mriqcep.key /etc/ssl/private/mriqcep-selfsigned.key
#COPY .ssl/mriqcep_pass /etc/ssl/mriqcep_pass
#RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
