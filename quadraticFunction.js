// TensorPlayground.com
// RGB Tensor
// INPUT TENSOR SHAPE: [622,1024,3]

(tf, aTensor) => {
  // return tensor to show
  //Declare tensors
  const a = tf.tensor([5])
  const b = tf.tensor([6])
  const c = tf.tensor([1])
  
  //Construct new tensors necesarilly
  const Mb = tf.mul(b,-1)
  const bS = (b.square())
  const aC = tf.mul(a,c)
  const ac4 = tf.mul(4,aC)
  const a2 = tf.mul(2,a)
  const bSac4 = tf.sub(bS, ac4)
  
  const bM4 = bSac4.sqrt().print()
  
  
  const x = tf.floor(bS, tf.add(Mb, bM4))
  const y = tf.floor(bS, tf.sub(Mb, bM4))
  

  return x
}
