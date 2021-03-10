

reference: http://fourier.eng.hmc.edu/e161/lectures/gradient/node8.html

reference: http://fourier.eng.hmc.edu/e161/lectures/gradient/node9.html

reference: http://6.869.csail.mit.edu/fa16/lecture/lecture3linearfilters.pdf

reference: http://www.laurentnajman.org/uploads/ImageCourse/filtering_ln.pdf

### LoG (Laplacian of Gaussian)

usage: 

Since the 2nd derivative is very sensitive to noise, it is always a good idea to **remove noise** by smoothing the image before applying the Laplacian to ensure that noise  is not aggravated. 

Because of the associative property of convolution,  it can be thought of as taking the 2nd derivative (Laplacian) of the Gaussian filter and then applying the resulting (combined)  filter onto the image, hence the name LoG. 
$$
g_{\sigma}(x, y)=\frac{1}{2 \pi \sigma^{2}} \exp \left(-\frac{x^{2}+y^{2}}{2 \sigma^{2}}\right)
$$
simplicity we omitted the normalizing coefficient 
$$
L o G \triangleq \Delta g_{\sigma}(x, y)=\frac{\partial^{2}}{\partial x^{2}} g_{\sigma}(x, y)+\frac{\partial^{2}}{\partial y^{2}} g_{\sigma}(x, y)=\frac{x^{2}+y^{2}-2 \sigma^{2}}{\sigma^{4}} e^{-\left(x^{2}+y^{2}\right) / 2 \sigma^{2}}
=-\frac{1}{\pi \sigma^{4}}\left[1-\frac{x^{2}+y^{2}}{2 \sigma^{2}}\right] e^{-\frac{x^{2}+y^{2}}{2 \sigma^{2}}}
$$
note: 

Make sure that the sum (or average) of all elements of the kernel has to be zero (similar  to the Laplace kernel) so that the convolution result of a homogeneous  regions is always zero.

The kernel of any other sizes can be obtained by approximating the  continuous expression of LoG given above
$$
\left[\begin{array}{ccccc}
0 & 0 & 1 & 0 & 0 \\
0 & 1 & 2 & 1 & 0 \\
1 & 2 & -16 & 2 & 1 \\
0 & 1 & 2 & 1 & 0 \\
0 & 0 & 1 & 0 & 0
\end{array}\right]
$$
(for a Gaussian $\sigma$ = 1.4) 
$$
\begin{array}{|c|r|r|r|r|r|r|r|r|}
\hline 0 & 1 & 1 & 2 & 2 & 2 & 1 & 1 & 0 \\
\hline 1 & 2 & 4 & 5 & 5 & 5 & 4 & 2 & 1 \\
\hline 1 & 4 & 5 & 3 & 0 & 3 & 5 & 4 & 1 \\
\hline 2 & 5 & 3 & -12 & -24 & -12 & 3 & 5 & 2 \\
\hline 2 & 5 & 0 & -24 & -40 & -24 & 0 & 5 & 2 \\
\hline 2 & 5 & 3 & -12 & -24 & -12 & 3 & 5 & 2 \\
\hline 1 & 4 & 5 & 3 & 0 & 3 & 5 & 4 & 1 \\
\hline 1 & 2 & 4 & 5 & 5 & 5 & 4 & 2 & 1 \\
\hline 0 & 1 & 1 & 2 & 2 & 2 & 1 & 1 & 0 \\
\hline
\end{array}
$$
remark:

We  can  compute  its  Fourier  Transform of LoG.   We  know  that  the  Fourier  Transform  of  a  Gaussian  is  another Gaussian, and we also know that we can differentiate using a ramp function (2πiu or 2πiν) in the frequency domain. Multiply together the spectrum of the image, the Fourier Transform of a Gaussian, and two differentiating ramps in the one direction and you have a second-derivative of Gaussian in one direction. Do the same thing in the other direction,add them together, and you have the Laplacian of Gaussian of the image. 
$$
G(u, v ; \sigma)=\exp\{ -2 \pi^{2}\left(u^{2}+v^{2}\right) \sigma^{2} \}
$$

$$
\begin{aligned}
\mathcal{F}\left[\frac{\partial^{2} g_{\sigma}(x, y)}{\partial x^{2}}+\frac{\partial^{2} g_{\sigma}(x, y)}{\partial y^{2}}\right] &=(j u)^{2} G_{\sigma}(u, v)+(j v)^{2} G_{\sigma}(u, v) \\
&=-\left(u^{2}+v^{2}\right) G_{\sigma}(u, v)
\end{aligned}
$$

### DoG (Difference of Guassian)

usage: 

LoG can be efficiently  approximated using the difference of two Gaussians (DoG) with different  scales (variances)
$$
D o G \triangleq g_{\sigma_{1}}-g_{\sigma_{2}}=\frac{1}{2 \pi}\left(\frac{1}{\sigma_{1}^2} e^{-\left(x^{2}+y^{2}\right) / 2 \sigma_{1}^{2}}-\frac{1}{\sigma_{2}^2} e^{-\left(x^{2}+y^{2}\right) / 2 \sigma_{2}^{2}}\right)
$$
note:

It is necessary for the sum or average of all elements of the kernel matrix to be zero.

Comparing this plot with the previous one, we see that the DoG curve is very similar to the LoG curve.