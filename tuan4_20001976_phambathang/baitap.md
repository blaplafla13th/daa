---
documentclass: article
fontsize: 14pt
title: Bài tập tuần 4
author: Phạm Thị Thương - 20001981
---

# Bài 1

a. $T(n) = nlogn + 3n + 2$  
$nlogn + 3n + 2 \leq 2*n*log(n) \rightarrow nlogn-3n-2 \geq 0$  
$\Rightarrow T(n) = O(nlogn), c = 2, n_0 = 1004.594$

b. $T(n) = nlog(n!) + 5n^2+ 7$  
Ta có $nlog(n!) = nlog(1*2*3*...*n) = n * (log(1)+log(2)+...+log(n)) \leq n(log(n)+...+log(n)) = n^2*log(n)$  
$\rightarrow nlog(n!) + 5n^2+ 7 \leq 2n^2logn$  
$\Rightarrow T(n) = O(n^2logn), c = 2, n_0 = 100001$

c. $1000n+ 0.01n^2$  
Ta có $1000n+0.01n^2 \leq n^2$  
$\Rightarrow T(n) = O(n^2), c = 1, n_0 = 11112$

d. $100nlogn+n^3+100n$  
Ta có $100nlogn+n^3+100n \leq 2n^3$  
$\Rightarrow T(n) = O(n^3), c = 2, n_0 = 15$

e. $0.01nlogn+n(logn)^2$
Ta có $0.01nlogn+n(logn)^2 \leq 2n(logn)^2$  
$\Rightarrow T(n) = O(n(logn)^2), c = 2, n_0 = 1.02$

# Bài 2

a.

Chạy for từ i = 0 đến n - 1. Thực hiện phép cộng trong vòng lặp là $O(1)$ $\rightarrow T(n) = O(n)*O(1)= O(n)$

b.

Chạy for từ i = 0 đến n - 1 với bước nhảy là 2, số lần lặp thực hiện là $\frac{n}{2}$. Thực hiện phép cộng trong vòng
lặp là $O(1)$ $\rightarrow T(n) = O(\frac{n}{2})*O(1)= O(n)$

c.

Vòng lặp bên ngoài chạy từ 0 đến n - 1, vòng lặp bên trong chạy từ 0 đến j. Vậy số lần lặp là $\sum_{i=0}^{n-1}i =
\frac{n(n-1)}{2}$. Thực hiện phép cộng trong vòng lặp là $O(1)$ $\rightarrow T(n) = O(\frac{n(n-1)}{2})*O(1)= O(n^2)$

d.

Vòng lặp chạy từ 0 đến n - 1. Trong vòng lặp thực hiện 2 phép cộng nên độ phức tạp là $O(max(O(1),O(1))) = O(1)$.
$\rightarrow T(n) = O(n)*O(1)= O(n)$

e.

Vòng lặp thứ 2 chạy từ 0 đến n - 1, vòng lặp vòng lặp thứ ba chạy từ 0 đến j. $\rightarrow$ số lần lặp là $\sum_
{i=0}^{n-1}i = \frac{n(n-1)}{2}$. Thực hiện phép cộng trong vòng lặp thứ ba là $O(1)$ $\rightarrow$ độ phức tạp của vòng
lặp thứ 2 là $O(\frac{n(n-1)}{2})*O(1)= O(n^2)$. Trong vòng lặp đầu tiên còn có phép so sánh độ phức tạp là $O(1)
\rightarrow$ độ phức tạp trong vòng lặp là $O(max(O(n^2),O(1))) = O(n^2)$, vòng lặp chạy từ 0 đến n - 1. $\rightarrow$
độ phức tạp của vòng lặp đầu tiên là $O(n)*O(n^2) = O(n^3)$