---
documentclass: article
fontsize: 14pt
title: Bài tập tuần 4
author: Phạm Bá Thắng - 20001976
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
```java
// Returns the sum of the integers in given array .
public static int example1 (int[ ] arr ) {
    int n = arr.length , total = 0;
    for ( int j =0; j < n ; j ++) // loop from 0 to n -1
        total += arr [ j ];
    return total ;
}
```
Chạy for từ i = 0 đến n - 1. Thực hiện phép cộng trong vòng lặp là $O(1)$ $\rightarrow T(n) = O(n)*O(1)= O(n)$

b.
```java
// Returns the sum of the integers with even index in given array.
public static int example2 (int[ ] arr ) {
    int n = arr.length , total = 0;
    for ( int j =0; j < n ; j += 2) // note the increment of 2
        total += arr [j];
    return total ;
}
```
Chạy for từ i = 0 đến n - 1 với bước nhảy là 2, số lần lặp thực hiện là $\frac{n}{2}$. Thực hiện phép cộng trong vòng lặp là $O(1)$  $\rightarrow T(n) = O(\frac{n}{2})*O(1)= O(n)$

c.
```java
// Returns the sum of the prefix sums of given array .
public static int example3 (int[ ] arr ) {
    int n = arr.length , total = 0;
    for ( int j =0; j < n ; j ++) // loop from 0 to n -1
        for ( int k =0; k <= j ; k ++) // loop from 0 to j
           total += arr[j];
   return total ;
}
```
Vòng lặp bên ngoài chạy từ 0 đến n - 1, vòng lặp bên trong chạy từ 0 đến j. Vậy số lần lặp là $\sum_{i=0}^{n-1}i = \frac{n(n-1)}{2}$. Thực hiện phép cộng trong vòng lặp là $O(1)$ $\rightarrow T(n) = O(\frac{n(n-1)}{2})*O(1)= O(n^2)$

d.
```java
// Returns the sum of the prefix sums of given array .
public static int example4 (int[ ] arr ) {
    int n = arr.length , prefix = 0 , total = 0;
    for ( int j =0; j < n ; j ++) { // loop from 0 to n -1
       prefix += arr[j];
       total += prefix ;
   }
   return total ;
}
```
Vòng lặp chạy từ 0 đến n - 1. Trong vòng lặp thực hiện 2 phép cộng nên độ phức tạp là $O(max(O(1),O(1))) = O(1)$. $\rightarrow T(n) = O(n)*O(1)= O(n)$

e.
```java
// Returns the number of times second array stores sum of prefix sums from first .
public static int example5 (int[] first , int[] second) {
// assume equal - length arrays
    int n = first.length , count = 0;
    for ( int i = 0; i < n ; i ++) { // loop from 0 to n -1
        int total = 0;
        for ( int j =0; j < n ; j ++) // loop from 0 to n -1
            for ( int k =0; k <= j ; k ++) // loop from 0 to j
                total += first [ k ];
        if (second [i] == total) count++;
    }
    return count ;
}
```
Vòng lặp thứ 2 chạy từ 0 đến n - 1, vòng lặp  vòng lặp thứ ba chạy từ 0 đến j. $\rightarrow$ số lần lặp là $\sum_{i=0}^{n-1}i = \frac{n(n-1)}{2}$. Thực hiện phép cộng trong vòng lặp thứ ba là $O(1)$ $\rightarrow$ độ phức tạp của vòng lặp thứ 2 là $O(\frac{n(n-1)}{2})*O(1)= O(n^2)$. Trong vòng lặp đầu tiên còn có phép so sánh độ phức tạp là $O(1) \rightarrow$ độ phức tạp trong vòng lặp là  $O(max(O(n^2),O(1))) = O(n^2)$, vòng lặp chạy từ 0 đến n - 1. $\rightarrow$ độ phức tạp của vòng lặp đầu tiên là $O(n)*O(n^2) = O(n^3)$