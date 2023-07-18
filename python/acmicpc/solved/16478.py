def test(Pab, Pbc, Pcd):
    res = Pab * Pcd / Pbc
    print(int(res) if int(res)==res else res)

def __init__():
    Pab, Pbc, Pcd = map(int, input().split())
    test(Pab, Pbc, Pcd)

__init__()