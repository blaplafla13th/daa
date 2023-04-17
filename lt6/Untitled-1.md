---
title: Luyện tập 6
author: Phạm Bá Thắng - 20001976
---

# Exercise 1. Cho mảng A có kích thước n. Giả sử, giá trị A[i] cho biết độ dài của tệp thứ i và người ta cần ghép (merge) tất cả các file đó thành 1 file duy nhất. Hãy kiểm tra xem thuật toán dưới đây có đưa ra lời giải tốt nhất cho bài toán này hay không?

**Thuật toán:** Ghép các file một cách liên tục (tức là chọn 2 file đầu tiên và ghép chúng lại. Sau đó, lấy file kết quả với ghép rồi ghép với file thứ 3 và cứ tiếp tục như thế, ...

**Lưu ý:** Với 2 file X và Y có kích thước là x và y, độ phức tạp của việc ghép làm O(x + y).

Kích thước sẽ tăng dần, các tệp có kích thước lớn hơn lại ghép với kích thước nhỏ hơn, liên tục cộng dồn lại, độ phức tạp sẽ tăng dần. Vậy nên thuật toán này không đưa ra lời giải tốt nhất cho bài toán.

$T(1) = n_1$

$T(n) = T(n-1)+T(n-2)+n_n \approx O(2^n)$

Ví dụ 4 file: 4, 8, 3, 5
$T(4) = 2T(3) + 5 = 2(2T(2) + 3) + 5 = 2(2(4 + 8) + 3) + 5 = 59$

# Exercise 2. Tương tự của bài 1, thuật toán dưới đây có đưa ra lời giải tối ưu hay không?

**Thuật toán:** Ghép các file theo cặp (tức là, sau bước đầu tiên thuật toán tạo ra n/2 file trung gian).

Đối với việc chia đôi ghép cặp các file, số lượng file cần ghép sẽ còn là $\log n$, lượng cộng dồn cũng nhỏ hơn, độ phức tạp sẽ giảm dần. Vậy nên thuật toán này đưa ra lời giải tối ưu.

Xét ví dụ trên:
- Lần 1: $t = 4 + 8 = 12$  
- Lần 2: $t = 3 + 5 = 8$  
- Lần 3: $t = 12 + 8 = 20$   
Tổng thời gian: $t = 12 + 8 + 20 = 40$ bớt đi được 19 lần

Việc cộng này sẽ làm giảm độ phức tạp thuật toán đi trong vài trường hợp nếu thứ tự độ dài được sắp xếp hợp lý 

# Exercise 3. Dựa vào kết quả phân tích bài 1 và bài 2 thì cách tốt nhất để ghép tất cả các file thành 1 file duy nhất là gì? Hãy nêu rõ cách đó.

Là cách 2