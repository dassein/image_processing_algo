

input:

* I: (M, N)
* p: (M, N)
* size = 2 * r + 1

output:

* q: (M, N)

$$
\bar{I}(i, j)= E[I](i, j) = \frac{\sum\limits_{\Delta x=-r\to r\\
\Delta y=-r\to r} I(i+\Delta x, j+\Delta y) }{[2r+1]^2}\\

\bar{p}(i, j) = E[p](i, j)= \frac{\sum\limits_{\Delta x=-r\to r\\
\Delta y=-r\to r} p(i+\Delta x, j+\Delta y) }{[2r+1]^2}
$$

and


$$
E[I^2](i, j) = \frac{\sum\limits_{\Delta x=-r\to r\\
\Delta y=-r\to r} I^2(i+\Delta x, j+\Delta y) }{[2r+1]^2}\\

E[I\cdot p](i, j) = \frac{\sum\limits_{\Delta x=-r\to r\\
\Delta y=-r\to r} I\cdot p(i+\Delta x, j+\Delta y) }{[2r+1]^2}\\
$$
then **goal 1**:
$$
\sigma^2[I](i, j) = E[I^2](i, j)-E^2[I](i, j)\\
\text{cov}[Ip](i, j) = 
 E[Ip](i, j) - E[I](i, j)E[p](i, j)
$$
Define 
$$
a(i, j) \equiv \frac{\text{cov}[Ip](i, j)}{\sigma^2[I](i, j) + \epsilon}\\
b(i, j) \equiv E[p](i, j) - \frac{\text{cov}[Ip](i, j)}{\sigma^2[I](i, j)+\epsilon} E[I](i, j)
$$
calc
$$
\bar{a}(i, j)= E[a](i, j) = \frac{\sum\limits_{\Delta x=-r\to r\\
\Delta y=-r\to r} a(i+\Delta x, j+\Delta y) }{[2r+1]^2}\\

\bar{b}(i, j) = E[b](i, j)= \frac{\sum\limits_{\Delta x=-r\to r\\
\Delta y=-r\to r} b(i+\Delta x, j+\Delta y) }{[2r+1]^2}
$$
In the end **goal 2**:
$$
q(i, j) = E[a](i, j) \times I(i, j) + E[b](i, j)
$$


