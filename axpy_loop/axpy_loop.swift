import TensorFlow
import Dispatch

func time(_ body: () -> Void) {
  let divisor: Float = 1_000_000_000
  let start = Float(DispatchTime.now().uptimeNanoseconds) / divisor
  print("Start: \(start)s")
  body()
  let end = Float(DispatchTime.now().uptimeNanoseconds) / divisor
  print("End: \(end)s")
  let elapsed = end - start
  print("Elapsed: \(elapsed)s")
}

@inline(never)
func main() {
  var x = Tensor<Float>(shape: [64, 512], repeating: 0.2)
  let w = Tensor<Float>(shape: [512, 512], repeating: 0.2)
  let b = Tensor<Float>(shape: [512], repeating: 0.2)
  var i: Int32 = 0
  repeat {
    x = matmul(x, w) + b
    i += 1
  } while i < 1000
}

time(main)