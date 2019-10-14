"""
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

"""

"""
    tf中有两种shape:
        static shape 和 dynamic shape
    1.static shape 用于构建图，由创建这个tensor的op推断得来。
    2.如果该tensor的static shape未定义，则可用tf.shape()获取dynamic shape
    
    http://www.jianshu.com/p/2b88256ad206
"""
import numpy as np
import tensorflow as tf


def shape_tf():

    x = tf.placeholder(tf.int32, shape=[2, 2])

    # 1.
    # static shape
    print(x.get_shape())  # 返回元组
    print(x.get_shape().as_list())  # 返回python list
    # 2.
    # dynamic shape， 运行时获取shape
    print(tf.shape(x))

    y = tf.square(x)
    print(y.get_shape())  # 返回元组
    print(y.get_shape()[0].value)  # 返回第0维上的值
    print(y.get_shape()[1].value)  # 返回第1维上的值
    print(y.get_shape().as_list())  # 返回python list
    # dynamic shape， 运行时获取shape
    print(tf.shape(y))

    # 3.
    # 更新tensor的static shape,不改变dynamic shape
    y.set_shape(shape=[2, 2])

    # 4.
    # reshape 创建一个新的具备不同dynamic shape的tensor
    y = tf.reshape(y, shape=[1, 4])

    with tf.Session() as sess:
        y_result = sess.run(y, feed_dict={x: [[1, 2], [3, 5]]})
        print(y_result)
        # 5.
        print(y_result.shape)

    pass


def shape_numpy():
    a = np.asarray([[2, 3, 4], [4, 5, 6]], dtype=np.int32)
    print(np.shape(a))
    print(a.shape)
    pass

if __name__ == '__main__':
    shape_tf()
    shape_numpy()

