## Some Docker Notes for Development Only

If you have updated the requirements be sure to update the contents of the `requirements.txt` file before attempting to build the image.

```
$ docker system prune -a
$ docker build --tag dj1 .
$ docker run -p 80:8000 dj1
```
## Some deployment notes to fly.io

The Django app is now dependent on environment variables which are defined in .env but which are not ideally deployed with the app and so .env should be in .gitignore.

If you do that however the app fails as it can't read the .env file. To get around that, at least initially, I'm doing this ...

To check the name of the app ...
```
$ fly status --all
```

... then, assuming the app name is abc-defg-1234 ...

```
$ cat .env | fly secrets import --app abc-defg-1234
```

... this will then trigger a redeploy and the app then behaves as if the .env was present in the originaly deploy.

