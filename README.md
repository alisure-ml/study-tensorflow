# confuse:shape

### tf:static shape
> x is a tensor
- x.get_shape()
- x.get_shape()[0].value
- x.get_shape().as_list()

### tf:dynamic shape
> x is a tensor
- tf.shape(x)

### tf:set_shape
> x is a tensor
- x.set_shape(shape=[2, 2])

### numpy:np.shape
> x is a numpy list
- np.shape(x)
- x.shape
