---
documentclass: article
fontsize: 14pt
title: Bài tập tuần 7
author: Phạm Bá Thắng - 20001976
---
# Bài tập tại lớp
1. Let us consider an algorithm A which solves problems by dividing them into five subproblems of half the size, recursively solving each subproblem, and then combining the solutions in linear time. What is the complexity of this algorithm?
$$
\begin{array}{ll}
T(n)=5T(\frac{n}{2})+n\\
a = 5, b = 2, d = 1, p = 0, a > b^d\\
\Rightarrow T(n)=\Theta(n^{\log_b {a}})=\Theta(n^{\log_2 {5}})\\
\end{array}
$$
2. Similar to Problem-1, an algorithm B solves problems of size n by recursively solving two subproblems of size $n - 1$ and then combining the solutions in constant time. What is the complexity of this algorithm?
$$
\begin{array}{ll}
T(n)=2T(n-1)+1\\
\Rightarrow T(n)=2*(2*T(n-2)+1)+1\\
...\\
\Rightarrow T(n)=2^{n}(T(0))+n\\
\Rightarrow T(n)=\Theta(2^n)\\
\end{array}
$$
3. Againt similar to Problem-1, another algorithm C solves problems of size n by
dividing them into nine subproblems of size $\frac{n}{3}$, recursively solving each subproblem and then combining the solution in $O(n^2)$ time. What is the complexity of this algorithm?
$$
\begin{array}{ll}
T(n)=9T(\frac{n}{3})+n^2\\
a = 9, b = 3, d = 2, p = 0, a = b^d\\
\Rightarrow T(n)=\Theta(n^{\log_b {a}}\log n)=\Theta(n^2\log n)\\
\end{array}
$$
4. Write a recurrence and solve it
```java
public void function ( int n ) {
    if (n > 1) {
        System.out.println("*");
        function(n/2);
        function(n/2);
    }
}
```
$$
\begin{array}{ll}
T(n)=2T(\frac{n}{2})+1\\
a = 2, b = 2, d = 0, p = 0, a > b^d\\
\Rightarrow T(n)=\Theta(n^{\log_b {a}})=\Theta(n^{\log_2 {2}})=\Theta(n)\\
\end{array}
$$
# Bài tập vận dụng
1. $T(n)=3T(\frac{n}{2})+n^2$
$$
\begin{array}{ll}
a = 3, b = 2, d = 2, p = 0, a < b^d\\
\Rightarrow T(n)=\Theta(n^d)=\Theta(n^2)\\
\end{array}
$$
2. $T(n)=4T(\frac{n}{2})+n^2$
$$
\begin{array}{ll}
a = 4, b = 2, d = 2, p = 0, a = b^d\\
\Rightarrow T(n)=\Theta(n^{\log_b {a}}\log n)=\Theta(n^2\log n)\\
\end{array}
$$
3. $T(n)=16T(\frac{n}{4})+n$
$$
\begin{array}{ll}
a = 16, b = 4, d = 1, p = 0, a > b^d\\
\Rightarrow T(n)=\Theta(n^{\log_b a})=\Theta(n^2)\\
\end{array}
$$
4. $T(n)=2T(\frac{n}{2})+\frac{n}{\log n}$
$$
\begin{array}{ll}
a = 2, b = 2, d = 1, p = -1, a = b^d\\
\Rightarrow T(n)=\Theta(n^{\log_b {a}}\log\log n)=\Theta(n\log\log n)\\
\end{array}
$$
5. $\sqrt{2}T(\frac{n}{2})+log n$
$$
\begin{array}{ll}
a = \sqrt{2}, b = 2, d = 0, p = 1, a > b^d\\
\Rightarrow T(n)=\Theta(n^{\log_b {a}})=\Theta(\sqrt{n})\\
\end{array}
$$
6. $T(n)=3T(\frac{n}{3})+\sqrt{n}$
$$
\begin{array}{ll}
a = 3, b = 3, d = \frac{1}{2}, p = 0, a > b^d\\
\Rightarrow T(n)=\Theta(n^{\log_b {a}})=\Theta(n)\\
\end{array}
$$
7. Write a recursion formula for the running time T(n) of the function f, whose code is given below. What is the running time of fuction, as a function of n?
```java
public void function ( int n ) {
    if( n <= 1) return ;
        for (int i = 1; i < n ; i ++)
            System.out.println("*");
    function (0.6*n) ;
}
```
$$
\begin{array}{ll}
T(n)=T(0.6n)+n-1\\
\Rightarrow T(n)=3\Theta(\frac{n}{5})+n\\
a = 3, b = 5, d = 1, p = 0, a < b^d\\
\Rightarrow T(n)=\Theta(n^d)=\Theta(n)\\
\end{array}
$$
8. $T(n)=2T(\sqrt{n})+\log n$

Đặt $n = 2^m \rightarrow \log n = m$
$$
\begin{array}{ll}
    \left\{
        \begin{array}{ll}
            T(n)=T(2^m)=2T(2^{\frac{m}{2}})+m\\
            T(n)=S(m) \Rightarrow S(\frac{m}{2})=T(2^\frac{m}{2})
        \end{array}
    \right.\\
    \Rightarrow 
    S(m) = 2 S(\frac{m}{2}) + m\\
    a = 2, b = 2, d = 1, a = b^d\\
    \Rightarrow S(m) = \Theta(m\log m) \\
    \Rightarrow T(n)=\Theta(\log n \log \log n)
\end{array}
$$
9. $T(n)=T(\sqrt{n})+1$

Đặt $n = 2^m \rightarrow \log n = m$
$$
\begin{array}{ll}
    \left\{
        \begin{array}{ll}
            T(n)=T(2^m)=T(2^{\frac{m}{2}})+1\\
            T(n)=S(m) \Rightarrow S(\frac{m}{2})=T(2^\frac{m}{2})
        \end{array}
    \right.\\
    \Rightarrow 
    S(m) = S(\frac{m}{2}) + 1\\
    a = 2, b = 2, d = 0, a > b^d\\
    \Rightarrow S(m) = \Theta(m) \\
    \Rightarrow T(n)=\Theta(\log n)
\end{array}
$$
10. Phân tích thời gian chạy của mã giả đệ quy sau:
```java
public void function(int n) {
    if (n < 2) return ;
    else counter = 0;
    for i = 1 to 8 do
        function(n / 2) ;
    for i = 1 to n^3 do
        counter = counter + 1;
}
```
$$
\begin{array}{ll}
    \left\{
        \begin{array}{ll}
            T(n) = 1 & n < 2 \\
            T(n) = 8 T(\frac{n}{2}) + n^3 + 2 & n \geq 2
        \end{array}
    \right.\\
    \Rightarrow T(n) = 8 T(\frac{n}{2}) + n^3 + 2\\
    a = 8, b = 2, d = 3, a = b^d\\
    \Rightarrow T(n) = \Theta(n^{\log_b a}\log n)=\Theta(n^3\log n)    
\end{array}
$$