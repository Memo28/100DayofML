(tf, aTensor) => {
  // return tensor to show
  console.log(aTensor.shape[1]/2)

  const left = (aTensor.slice([0, 0], [aTensor.shape[0], aTensor.shape[1]/2]))
  const newLeft = (aTensor.slice([0, 0], [aTensor.shape[0], aTensor.shape[1]/2])).reverse(1)
  //const right = (aTensor.slice([0, aTensor.shape[1]/2], [aTensor.shape[0],aTensor.shape[1]/2])).reverse(1)
  
  const mirror = tf.concat([left, newLeft] , 1)

  return mirror
}
