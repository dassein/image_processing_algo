## Euclidean distance tansform
the codes are from the lab at Princetion https://github.com/seung-lab/euclidean-distance-transform-3d
### 1-d code
in the `./edt_cpp/edt.hpp` file, see link http://cs.brown.edu/people/pfelzens/papers/dt-final.pdf
```c++
/**
 * Essentially, the distance function can be 
 * modeled as the lower envelope of parabolas
 * that spring mainly from edges of the shape
 * you want to transform. The array is scanned
 * to find the parabolas, then a second scan
 * writes the correct values.
 *
 * O(N) time complexity.
 *
 * I (wms) make a few modifications for our use case
 * of executing a euclidean distance transform on
 * a 3D anisotropic image that contains many segments
 * (many binary images). This way we do it correctly
 * without running EDT > 100x in a 512^3 chunk.
 *
 * The first modification is to apply an envelope 
 * over the entire volume by defining two additional
 * vertices just off the ends at x=-1 and x=n. This
 * avoids needing to create a black border around the
 * volume (and saves 6s^2 additional memory).
 *
 * The second, which at first appeared to be important for
 * optimization, but after reusing memory appeared less important,
 * is to avoid the division operation in computing the intersection
 * point. I describe this manipulation in the code below.
 *
 * I make a third modification in squared_edt_1d_parabolic_multi_seg
 * to enable multiple segments.
 *
 * Parameters:
 *   *f: the image ("sampled function" in the paper)
 *    *d: write destination, same size in voxels as *f
 *    n: number of voxels in *f
 *    stride: 1, sx, or sx*sy to handle multidimensional arrays
 *    anisotropy: e.g. (4nm, 4nm, 40nm)
 * 
 * Returns: writes distance transform of f to d
 */
void squared_edt_1d_parabolic(
    float* f, 
    float *d, 
    const int n, 
    const long int stride, 
    const float anisotropy, 
    const bool black_border_left,
    const bool black_border_right
  ) {

  if (n == 0) {
    return;
  }

  const float w2 = anisotropy * anisotropy;

  int k = 0;
  int* v = new int[n]();
  float* ff = new float[n]();
  for (long int i = 0; i < n; i++) {
    ff[i] = f[i * stride];
  }
  
  float* ranges = new float[n + 1]();

  ranges[0] = -INFINITY;
  ranges[1] = +INFINITY;

  /* Unclear if this adds much but I certainly find it easier to get the parens right.
   *
   * Eqn: s = ( f(r) + r^2 ) - ( f(p) + p^2 ) / ( 2r - 2p )
   * 1: s = (f(r) - f(p) + (r^2 - p^2)) / 2(r-p)
   * 2: s = (f(r) - r(p) + (r+p)(r-p)) / 2(r-p) <-- can reuse r-p, replace mult w/ add
   */
  float s;
  float factor1, factor2;
  for (long int i = 1; i < n; i++) {
    factor1 = (i - v[k]) * w2;
    factor2 =  i + v[k];
    s = (ff[i] - ff[v[k]] + factor1 * factor2) / (2.0 * factor1);

    while (s <= ranges[k]) {
      k--;
      factor1 = (i - v[k]) * w2;
      factor2 =  i + v[k];
      s = (ff[i] - ff[v[k]] + factor1 * factor2) / (2.0 * factor1);
    }

    k++;
    v[k] = i;
    ranges[k] = s;
    ranges[k + 1] = +INFINITY;
  }

  k = 0;
  float envelope;
  for (long int i = 0; i < n; i++) {
    while (ranges[k + 1] < i) { 
      k++;
    }

    d[i * stride] = w2 * sq(i - v[k]) + ff[v[k]];
    // Two lines below only about 3% of perf cost, thought it would be more
    // They are unnecessary if you add a black border around the image.
    if (black_border_left && black_border_right) {
      envelope = std::fminf(w2 * sq(i + 1), w2 * sq(n - i));
      d[i * stride] = std::fminf(envelope, d[i * stride]);
    }
    else if (black_border_left) {
      d[i * stride] = std::fminf(w2 * sq(i + 1), d[i * stride]);
    }
    else if (black_border_right) {
      d[i * stride] = std::fminf(w2 * sq(n - i), d[i * stride]);      
    }
  }

  delete [] v;
  delete [] ff;
  delete [] ranges;
}

// about 5% faster
void squared_edt_1d_parabolic(
    float* f, 
    float *d, 
    const int n, 
    const long int stride, 
    const float anisotropy
  ) {

  if (n == 0) {
    return;
  }

  const float w2 = anisotropy * anisotropy;

  int k = 0;
  int* v = new int[n]();
  float* ff = new float[n]();
  for (long int i = 0; i < n; i++) {
    ff[i] = f[i * stride];
  }

  float* ranges = new float[n + 1]();

  ranges[0] = -INFINITY;
  ranges[1] = +INFINITY;

  /* Unclear if this adds much but I certainly find it easier to get the parens right.
   *
   * Eqn: s = ( f(r) + r^2 ) - ( f(p) + p^2 ) / ( 2r - 2p )
   * 1: s = (f(r) - f(p) + (r^2 - p^2)) / 2(r-p)
   * 2: s = (f(r) - r(p) + (r+p)(r-p)) / 2(r-p) <-- can reuse r-p, replace mult w/ add
   */
  float s;
  float factor1, factor2;
  for (long int i = 1; i < n; i++) {
    factor1 = (i - v[k]) * w2;
    factor2 = i + v[k];
    s = (ff[i] - ff[v[k]] + factor1 * factor2) / (2.0 * factor1);

    while (s <= ranges[k]) {
      k--;
      factor1 = (i - v[k]) * w2;
      factor2 = i + v[k];
      s = (ff[i] - ff[v[k]] + factor1 * factor2) / (2.0 * factor1);
    }

    k++;
    v[k] = i;
    ranges[k] = s;
    ranges[k + 1] = +INFINITY;
  }

  k = 0;
  float envelope;
  for (long int i = 0; i < n; i++) {
    while (ranges[k + 1] < i) { 
      k++;
    }

    d[i * stride] = w2 * sq(i - v[k]) + ff[v[k]];
    // Two lines below only about 3% of perf cost, thought it would be more
    // They are unnecessary if you add a black border around the image.
    envelope = std::fminf(w2 * sq(i + 1), w2 * sq(n - i));
    d[i * stride] = std::fminf(envelope, d[i * stride]);
  }

  delete [] v;
  delete [] ff;
  delete [] ranges;
}

void _squared_edt_1d_parabolic(
    float* f, 
    float *d, 
    const int n, 
    const long int stride, 
    const float anisotropy, 
    const bool black_border_left,
    const bool black_border_right
  ) {

  if (black_border_left && black_border_right) {
    squared_edt_1d_parabolic(f, d, n, stride, anisotropy);
  }
  else {
    squared_edt_1d_parabolic(f, d, n, stride, anisotropy, black_border_left, black_border_right); 
  }
}
```
