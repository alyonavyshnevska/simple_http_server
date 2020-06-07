
##### A simple http server in python that runs locally and returns valid status codes

Python comes with a simple builtin HTTP server. With the help of this little HTTP server you can turn any directory in your system into your web server directory. The only thing you need to have installed is Python.  
If the directory has a file named index.html, that file will be served as the initial file. If there is no index.html, then the files in the directory will be listed.

`python -m http.server 8000`

Specifying port is optional. 

By default, server uses the current directory. The option -d/--directory specifies a directory to which it should serve the files.

`python -m http.server --directory /tmp/`


-------- 

My tiny utility lets you customize error messages, e.g. the 404 page not found messages when running a simple http server built-in in python standard library. To see an example of that run: 

`python simple_python_http_server.py`

then go to the `localhost:port/whatever_nonexisting_page` in your browser and see my example customizable error message.

Edit the message to your desired one in the `simple_python_http_server.py`

