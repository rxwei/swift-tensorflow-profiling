# Swift for TensorFlow profiling suite

This repository contains pairs of Python TensorFlow programs and Swift TensorFlow programs for a head-to-head performance comparison.

## Graphs with the same ops and control flow constructs

Basic operations are being tested here: matrix multiplication, convolution and loops.

- [axpy_unrolled](axpy_unrolled): Straight-line `Ax+b`
- [axpy_loop](axpy_loop): `Ax+b` in a `while` loop

|                  |  Python |   Swift |
|------------------|---------|---------|
| axpy_unrolled    | 0.7358s | 1.7969s |
| axpy_loop        | 0.3705s | 0.5781s |

## `tf.Variable` vs. functional

Graph Program Extraction currently does not generate mutable variables in the TensorFlow graph for `var` declarations. Instead, each mutation of `var` in Swift source code gets lowered to producing a new value. In Python, however, `tf.Variable` is used everywhere and may be highly optimized. Here we compare purely functional parameter updates with mutation-based parameter updates.

- [parameter_update](parameter_update): Straight-line parameter update

|                  |  Python |   Swift |
|------------------|---------|---------|
| parameter_update | 0.8749s | 1.4375s |

## Vanilla models

_Coming soon_