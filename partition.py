#====================================================================================================================
# From Leah Sturman and Holly Swisher's work: "Toward resolving Kang and Park's generalization of the Alder-Andrews Theorem"
# https://arxiv.org/abs/2407.18350v1
#====================================================================================================================
# Recursive function for the number of partitions of n into k parts:
def partition(k, n, p):
    # Base Case
    if k < 1 or n < 1: return p
    elif k == n: return p + 1
    # Recursive Call
    else: return partition(k-1, n-1, p) + partition(k, n-k, p)


print(partition(3, 100, 0))
