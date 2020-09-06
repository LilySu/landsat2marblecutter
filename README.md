Micro-services architecture that allows easy access to Landsat 8 Geotiff data to be run locally.

### Instructions on running project

```
docker-compose up
```


#### Application
	- Python Flask App
	- [http://localhost/](http://localhost/) lists the Geotiffs available for loading at [https://landsat-pds.s3.amazonaws.com/](https://landsat-pds.s3.amazonaws.com/)
	- When one of the links is clicked, the user is taken to the [Marblecutter preview for the selected COG](https://github.com/mojodna/marblecutter-virtual#preview---preview).

#### Marblecutter
	- The main menu normally accessible at / using the [upstream docker-compose file](https://github.com/mojodna/marblecutter-virtual/blob/master/docker-compose.yml) is accessible at [http://localhost/mc/](http://localhost/mc/).

#### Nginx
	- Routes `/` prefixed requests to the Application container, aka. the Flask homepage with Geotiffs listed as clickable links
	- Routes `/mc` prefixed requests to the Marblecutter container
	- Uses uwsgi instead of the development http server used by the upstream Marblecutter container.
# landsat2marblecutter
