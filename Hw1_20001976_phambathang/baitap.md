---
documentclass: article
fontsize: 14pt
title: Bài tập tuần 1
author: Phạm Bá Thắng - 20001976
---

# Xây dựng máy Turing

## Máy Turing thực hiện trừ 1 số nhị phân

$M_2=(K, \Sigma, \delta, S)$

$K = \{s, q, h \}, s - start, h - halt$

$\Sigma = \{0, 1, \blacktriangleright, \blacksquare \}\quad\blacktriangleright -\; begin,\, \blacksquare - end$

Table of transition functions $\delta$:

| Index |  t  |           k           | $\delta(t,k)=(k_1,t_1,\{\rightarrow/\leftarrow/-\})$ |
|:-----:|:---:|:---------------------:|:-----------------------------------------------------|
|   1   | $s$ |           0           | $(0, s, \rightarrow)$                                |
|   2   | $s$ |           1           | $(1, s, \rightarrow)$                                |
|   3   | $s$ | $\blacktriangleright$ | $(\blacktriangleright,s, \rightarrow)$               |
|   4   | $s$ |    $\blacksquare$     | $(\blacksquare,q, \leftarrow)$                       |
|   5   | $q$ |           0           | $(1,q,\leftarrow)$                                   |
|   6   | $q$ |           1           | $(0,h, -)$                                           |
|   7   | $q$ | $\blacktriangleright$ | $(\blacktriangleright,h, -)$                         |

## Máy Turing thực hiện việc thay tất cả các số 0 trong một dãy nhị phân thành các số 1 và ngược lại.

$M_3=(K, \Sigma, \delta, S)$

$K = \{s, h \}, s - start, h - halt$

$\Sigma = \{0, 1, \blacktriangleright, \blacksquare \}\quad\blacktriangleright -\; begin,\, \blacksquare - end$

Table of transition functions $\delta$:

| Index |  t  |           k           | $\delta(t,k)=(k_1,t_1,\{\rightarrow/\leftarrow/-\})$ |
|:-----:|:---:|:---------------------:|:-----------------------------------------------------|
|   1   | $s$ |           0           | $(1, s, \rightarrow)$                                |
|   2   | $s$ |           1           | $(0, s, \rightarrow)$                                |
|   3   | $s$ | $\blacktriangleright$ | $(\blacktriangleright,s, \rightarrow)$               |
|   4   | $s$ |    $\blacksquare$     | $(\blacksquare,h, \rightarrow)$                      |

## Máy Turing thực hiện việc loại bỏ các chữ số 0 trong dãy nhị phân. Sau khi bỏ cần dồn dãy lại.

$M_4=(K, \Sigma, \delta, S)$

$K = \{s, q_1, q_2, q_3, q_4, h \}, s - start, h - halt$

$\Sigma = \{0, 1,\blacktriangleright, \blacksquare \}, \blacktriangleright -\; begin,\, \blacksquare - end$

Table of transition functions $\delta$:

| Index |   t   |           k           | $\delta(t,k)=(k_1,t_1,\{\rightarrow/\leftarrow/-\})$ |
|:-----:|:-----:|:---------------------:|:-----------------------------------------------------|
|   1   |  $s$  |           1           | $(1, s, \rightarrow)$                                |
|   2   |  $s$  |           0           | $(0, q_1, -)$                                        |
|   3   |  $s$  | $\blacktriangleright$ | $(\blacktriangleright, s, \rightarrow)$              |
|   4   |  $s$  |    $\blacksquare$     | $(\blacksquare, q_3, \leftarrow)$                    |
|   5   | $q_1$ |           1           | $(1, q_2, -)$                                        |
|   6   | $q_1$ |           0           | $(0, q_1, \rightarrow)$                              |
|   7   | $q_1$ | $\blacktriangleright$ | $(\blacktriangleright, q_2, \rightarrow)$            |
|   8   | $q_1$ |    $\blacksquare$     | $(\blacksquare, q_3, \leftarrow)$                    |
|   9   | $q_2$ |           1           | $(0, q_2, \leftarrow)$                               |
|  10   | $q_2$ |           0           | $(1, s, \leftarrow)$                                 |
|  11   | $q_2$ | $\blacktriangleright$ | $(\blacktriangleright, q_2, \rightarrow)$            |
|  12   | $q_2$ |    $\blacksquare$     | $(\blacksquare, h, -)$                               |
|  13   | $q_3$ |           1           | $(1, h, -)$                                          |
|  14   | $q_3$ |           0           | $(\blacksquare, q_3, \leftarrow)$                    |
|  15   | $q_3$ | $\blacktriangleright$ | $(\blacktriangleright, h, -)$                        |
|  16   | $q_3$ |    $\blacksquare$     | $(\blacksquare, q_3, \leftarrow)$                    |


## Máy Turing thực hiện việc kiểm tra một dãy số nhị phân có đối xứng không.

$M_5=(K, \Sigma, \delta, S)$

$K = \{s, q_1, q_2, q_3, q_4, q_5, q_6, h\}, s - start, h - halt$

$\Sigma = \{0, 1, \blacktriangleright, \blacksquare, \square\} \blacktriangleright - begin, \blacksquare - end, \square -
blank$

Table of transition functions $\delta$:

| Index |   t   |           k           | $\delta(t,k)=(k_1,t_1,\{\rightarrow/\leftarrow/-\})$ |
|:-----:|:-----:|:---------------------:|:-----------------------------------------------------|
|   1   |  $s$  |          $0$          | $(0, s, \rightarrow)$                                |
|   2   |  $s$  |          $1$          | $(1, s, \rightarrow)$                                |
|   3   |  $s$  | $\blacktriangleright$ | $(\square, s, \rightarrow)$                          |
|   4   |  $s$  |    $\blacksquare$     | $(\square, q_1, \leftarrow)$                         |
|   5   |  $s$  |       $\square$       | $(\square, q_1, \leftarrow)$                         |
|   6   | $q_1$ |          $0$          | $(\square, q_2, \leftarrow)$                         |
|   7   | $q_1$ |          $1$          | $(\square, q_4, \leftarrow)$                         |
|   8   | $q_1$ | $\blacktriangleright$ | $(\blacktriangleright, s, \rightarrow)$              |
|   9   | $q_1$ |    $\blacksquare$     | $(\blacksquare, q_1, \leftarrow)$                    |
|  10   | $q_1$ |       $\square$       | $(1, h, -)$                                          |
|  11   | $q_2$ |          $0$          | $(0, q_2, \leftarrow)$                               |
|  12   | $q_2$ |          $1$          | $(1, q_2, \leftarrow)$                               |
|  13   | $q_2$ | $\blacktriangleright$ | $(\blacktriangleright, s, \rightarrow)$              |
|  14   | $q_2$ |    $\blacksquare$     | $(\blacksquare, q_1, \leftarrow)$                    |
|  15   | $q_2$ |       $\square$       | $(\square, q_3, \rightarrow)$                        |
|  16   | $q_3$ |          $0$          | $(\square, s, \rightarrow)$                          |
|  17   | $q_3$ |          $1$          | $(1, q_6, -)$                                        |
|  18   | $q_3$ | $\blacktriangleright$ | $(\blacktriangleright, s, \rightarrow)$              |
|  19   | $q_3$ |    $\blacksquare$     | $(\blacksquare, q_1, \leftarrow)$                    |
|  20   | $q_3$ |       $\square$       | $(\square, s, -)$                                    |
|  21   | $q_4$ |          $0$          | $(0, q_4, \leftarrow)$                               |
|  22   | $q_4$ |          $1$          | $(1, q_4, \leftarrow)$                               |
|  23   | $q_4$ | $\blacktriangleright$ | $(\blacktriangleright, s, \rightarrow)$              |
|  24   | $q_4$ |    $\blacksquare$     | $(\blacksquare, q_1, \leftarrow)$                    |
|  25   | $q_4$ |       $\square$       | $(\square, q_5, \rightarrow)$                        |
|  26   | $q_5$ |          $0$          | $(0, q_6, -)$                                        |
|  27   | $q_5$ |          $1$          | $(\square, s, \rightarrow)$                          |
|  28   | $q_5$ | $\blacktriangleright$ | $(\blacktriangleright, s, \rightarrow)$              |
|  29   | $q_5$ |    $\blacksquare$     | $(\blacksquare, q_1, \leftarrow)$                    |
|  30   | $q_5$ |       $\square$       | $(\square, s, -)$                                    |
|  31   | $q_6$ |          $0$          | $(\square, q_6, \rightarrow)$                        |
|  32   | $q_6$ |          $1$          | $(\square, q_6, \rightarrow)$                        |
|  33   | $q_6$ | $\blacktriangleright$ | $(\blacktriangleright, s, \rightarrow)$              |
|  34   | $q_6$ |    $\blacksquare$     | $(\blacksquare, q_1, \leftarrow)$                    |
|  35   | $q_6$ |       $\square$       | $(0, h, -)$                                          |

# Bài 2: Chứng minh các hàm sau là đệ quy nguyên thủy

## Multiplication 
$Mult(a, b) = a * b = a + a + ... + a (b\; times)$  

Base case: $Mult(a,0) = 0 = const$ là PRF do const là PRF  

Recursive case: $Mult(a,S(b)) = a * (b+1) = a * b + a = Add(Multi(a,b),a)=$ là PRF vì Add và các phức hợp của nó là PRF  
Từ đó Mult là PRF  

## Exponentiation
$Exp(a,b) = a^b = a*a*a...*a (b\; times)$  

Base case: $Exp(a,0) = 1 = const$ là PRF do const là PRF  

Recursive case: $Exp(a,S(b)) = a^{b+1} = a * a^{b} = Mul(Exp(a,b),a)=$ là PRF vì Mult và các phức hợp của nó là PRF  
Từ đó Exp là PRF

## Factorial
$Fact(n) = n! = n * (n-1) * (n-2) * ... * 1$  

Base case: $Fact(0) = 1 = const$ là PRF do const là PRF  

Recursive case: $Fact(S(n)) = (n+1)! = (n+1) * n! = Mul(S(n),Fact(n))=$ là PRF vì Mult và các phức hợp của nó là PRF  

Từ đó Fact là PRF  
<!-- 
## Predecessor or decrement: 
If a > 0 then a-1 else 0  
Base case: $Pred(a | a \leq 0) = 0 = const$ là PRF do const là PRF  
Recursive case: $Pred(S(n)) = n = P^n_1(n,S(n))$ là PRF vì P^n_1 và S cũng như các phức hợp của nó là PRF  
Từ đó Pred là PRF -->


# Bài 3: Phân tích thuật toán, viết thuật toán (Exercise 1.2, page 17-18, Anany’s book)

## Qua sông

### Sự kiện $S_0$:

1. Side A: sói, dê, đống bắp cải, thuyền
2. Side B: null

### Luật:

- $R_1$: Sói ăn dê
- $R_2$: Dê ăn bắp cải
- $R_3$: Nông dân chỉ chở được 1 cái sang bờ bên kia
- $R_4$: Nông dân không ăn nào trong ba
- $R_{1+2}$: Sói không ăn bắp cải

### Giải:

1. Dê sang do sói không ăn đống bắp cải theo luật $R_{1+2}$

   > Sự kiện $S_1$:
   >
   > 1. Side A: sói, đống bắp cải
   > 2. Side B: dê, thuyền

>

2. Quay về side A

   > Sự kiện $S_2$:
   >
   > 1. Side A: sói, đống bắp cải, thuyền
   > 2. Side B: dê

>

3. Chuyển sói hoặc đống bắp cải sang

   > Sự kiện $S_{3.1}$:
   >
   > 1. Side A: đống bắp cải
   > 2. Side B: dê,sói, thuyền
   >

   > Sự kiện $S_{3.2}$:
   >
   > 1. Side A: sói
   > 2. Side B: dê, đống bắp cải, thuyền

>

4. Chở dê sang để tránh $R_1$ trong $S_{3.1}$ và $R_2$ trong $S_{3.2}$

   > Sự kiện $S_{4.1}$:
   >
   > 1. Side A: đống bắp cải, thuyền, dê
   > 2. Side B: sói
   >

   > Sự kiện $S_{4.2}$:
   >
   > 1. Side A: sói, dê, thuyền
   > 2. Side B: đống bắp cải

>

5. Chở đống bắp cải trong $S_{4.1}$ và sói trong $S_{4.2}$ để tránh $R_1$ và $R_2$

   > Sự kiện $S_{5}$:
   >
   > 1. Side A:  dê
   > 2. Side B: sói,đống bắp cải, thuyền

>

6. Quay về side A

   > Sự kiện $S_{6}$:
   >
   > 1. Side A: dê, thuyền
   > 2. Side B: sói,đống bắp cải

>

7. Chở dê sang

   > Sự kiện $S_{6}$:
   >
   > 1. Side A: null
   > 2. Side B: sói,đống bắp cải, dê, thuyền

>

END

## Qua cầu

### Luật:

- A: 1 phút
- B: 2 phút
- C: 5 phút
- D: 10 phút

### Sự kiện $S_0$:

1. Side A: A, B, C, D, đèn
2. Side B: null

### Step

1. A với B đi hết 2 phút

   > Sự kiện $S_1$:
   >
   > 1. Side A: C, D
   > 2. Side B: A, B, đèn

>

2. A về đưa đèn hết 1 phút

   > Sự kiện $S_2$:
   >
   > 1. Side A: C, D, A, đèn
   > 2. Side B: B

>

3. C với D sang hết 10 phút

   > Sự kiện $S_3$:
   >
   > 1. Side A: A
   > 2. Side B: B, C, D, đèn

>

4. B về đưa đèn hết 2 phút

   > Sự kiện $S_4$:
   >
   > 1. Side A: A, B, đèn
   > 2. Side B: C, D

>

5. A với B đi hết 2 phút

   > Sự kiện $S_5$:
   >
   > 1. Side A: null
   > 2. Side B: A, B, đèn, C, D

>

Tổng 17 phút

## Thuật toán tính diện tích tam giác khi biết 3 cạnh a, b, c

a. $S = \sqrt{p(p-a)(p-b)(p-c)}$ với $p = (a + b+ c) / 2$  

Đây là công thức Heron để tính diện tích tam giác   

b. $S = \frac{1}{2} bc sinA$ với $A$ là góc xen giữa $b$ và $c$  

Áp dụng hệ quả của định lý Cauchy:  

$cosA = \frac{b^{2} + c^{2} - a^{2}}{2bc}$  

Áp dụng công thức lượng giác cơ bản:  

$sin^{2}A + cos^{2}A = 1$  

c. $S = \frac{1}{2} a h_a$ với $h_a$ là đường cao hạ từ đỉnh $A$  

Áp dụng định lý Heron:  

$h_a = 2 \frac{\sqrt{p(p-a)(p-b)(p-c)}}{a}$

## Nêu định nghĩa

- Algorithm design technique: is a general approach to solving problems algorithmically that is applicable to a variety
  of problems from different areas of computing. (Kĩ thuật thiết kế thuật toán là 1 phương pháp giải quyết vấn đề tổng
  quát áp dụng cho các lĩnh vực khác nhau)
- Pseudocode is a mixture of a natural language and programming language-like constructs and usually more precise than
  natural language,and its usage often yields more succinct algorithm descriptions. (Mã giả là một hỗn hợp giữa ngôn ngữ
  tự nhiên và lập trình để mô tả ngắn gọn 1 chương trình, thường rõ ràng và rõ ràng hơn so với ngôn ngữ tự nhiên)
- Proving an Algorithm’s Correctness is to use mathematical induction because an algorithm’s iterations provide a
  natural sequence of steps needed for such proofs. (Sử dụng toán học để chứng minh tính đúng đắn của thuật toán)

## Mô tả thuật toán mô tả số nguyên của số nhị phân dương

- English:
    1. Get the i-th number from the positive binary number, -is last number, i increase from 0 to the index of first
       number
    2. Calc $2^i*[i^{th} number]$
    3. Get total of them
- Pseudocode

```python
   import math
   
   decimal = 0
   i = 0
   while n > 0:
       decimal = decimal + 2 ** i * n % 10
       n = math.floor(n / 10)
```

## Mô tả thuật toán được sử dụng bởi điện thoại để thực hiện cuộc gọi điện thoại.

1. Nhận số điện thoại đầu vào
2. Gửi yêu cầu gọi lên nhà mạng
3. Đồng bộ clock với nhà mạng để thiết lập kết nối gửi nhận dữ liệu
4. Chia 2 luồng xử lý gửi nhận dữ liệu
5. Thực hiện truyền nhận cho đến khi kết thúc cuộc gọi

<!-- ## Các yêu cầu mà thuật toán cần có? Mô tả các bước chuyển thuật toán thành mã

1. Các yêu cầu:
    - Tính chính xác (correctness)
    - Tính hiệu quả (efficiency) gồm nhanh về mặt thời gian (time) và tốn ít không gian (space) bộ nhớ
    - Tính đơn giản (simplicity): dễ hiểu, dễ viết, dễ sửa
    - Tính tổng quát (generality): áp dụng cho tổng quát cho nhiều trường hợp bài toán khác nhau (generality of the
      problem the algorithm solves) cũng như áp dụng tổng quát cho nhiều đầu vào khác nhau (generality of the set of
      inputs it accepts) -->