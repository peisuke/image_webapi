# Image WebAPI

This sample is WebAPI for image. ```app.py``` is server side processing code and ```client.py``` is client side code. The client post an image to server and the server returns json string including base64 image to client. In the server, the image is converted to numpy array, and then, the array is converted to the json. Processing the numpy array　in the server side, the sample can be used to image translation, segmentation, recognition and so on.

# How to use

## Server side

```
python app.py
```

## Client side

```
python client.py
```

## result

The client send ```cat.jpg``` to server and the server returns the image. The client shows the shape of the returned image.

```
(194, 259, 3)
```
