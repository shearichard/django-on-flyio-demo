## Some Docker Notes for Development Only

If you have updated the requirements be sure to update the contents of the `requirements.txt` file before attempting to build the image.

```
$ docker system prune -a
$ docker build --tag dj1 .
$ docker run -p 80:8000 dj1
```

