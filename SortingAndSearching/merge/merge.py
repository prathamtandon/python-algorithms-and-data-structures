# Given two sorted arrays A and B, where A has enough buffer at the
# end to hold B. Merge B into A in sorted order.

def merge(A, B):
    if len(A) <= len(B):
        return
    n = len(B)
    m = len(A) - len(B)

    a_ptr = m-1
    b_ptr = n-1
    merged_ptr = m+n-1

    while a_ptr >= 0 and b_ptr >= 0:
        if A[a_ptr] > B[b_ptr]:
            A[merged_ptr] = A[a_ptr]
            a_ptr -= 1
        else:
            A[merged_ptr] = B[b_ptr]
            b_ptr -= 1
        merged_ptr -= 1

    while b_ptr >= 0:
        A[merged_ptr] = B[b_ptr]
        b_ptr -= 1
        merged_ptr -= 1
