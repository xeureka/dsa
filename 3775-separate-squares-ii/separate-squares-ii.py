class Node:
    __slots__ = 'l', 'r', 'min_cover_len', 'min_cover', 'todo'

    def __init__(self):
        self.l = 0
        self.r = 0
        self.min_cover_len = 0
        self.min_cover = 0
        self.todo = 0


class SegmentTree:
    def __init__(self, xs: List[int]):
        n = len(xs) - 1
        self.seg = [Node() for _ in range(2 << (n - 1).bit_length())]
        self.build(xs, 1, 0, n - 1)

    def get_uncovered_length(self) -> int:
        return 0 if self.seg[1].min_cover else self.seg[1].min_cover_len

    def maintain(self, o: int) -> None:
        lo = self.seg[o * 2]
        ro = self.seg[o * 2 + 1]
        mn = min(lo.min_cover, ro.min_cover)
        self.seg[o].min_cover = mn
        self.seg[o].min_cover_len = (lo.min_cover_len if lo.min_cover == mn else 0) + \
                                    (ro.min_cover_len if ro.min_cover == mn else 0)

    def do(self, o: int, v: int) -> None:
        self.seg[o].min_cover += v
        self.seg[o].todo += v

    def spread(self, o: int) -> None:
        v = self.seg[o].todo
        if v:
            self.do(o * 2, v)
            self.do(o * 2 + 1, v)
            self.seg[o].todo = 0

    def build(self, xs: List[int], o: int, l: int, r: int) -> None:
        self.seg[o].l = l
        self.seg[o].r = r
        if l == r:
            self.seg[o].min_cover_len = xs[l + 1] - xs[l]
            return
        m = (l + r) // 2
        self.build(xs, o * 2, l, m)
        self.build(xs, o * 2 + 1, m + 1, r)
        self.maintain(o)

    def update(self, o: int, l: int, r: int, v: int) -> None:
        if l <= self.seg[o].l and self.seg[o].r <= r:
            self.do(o, v)
            return
        self.spread(o)
        m = (self.seg[o].l + self.seg[o].r) // 2
        if l <= m:
            self.update(o * 2, l, r, v)
        if m < r:
            self.update(o * 2 + 1, l, r, v)
        self.maintain(o)


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = []
        events = []
        for (lx, y, l) in squares:
            rx = lx + l
            xs.append(lx)
            xs.append(rx)
            events.append((y, lx, rx, 1))
            events.append((y + l, lx, rx, -1))
        xs = sorted(set(xs))
        t = SegmentTree(xs)
        events.sort(key=lambda e: e[0])
        records = []
        tot_area = 0
        for (y, lx, rx, delta), e2 in pairwise(events):
            l = bisect_left(xs, lx)
            r = bisect_left(xs, rx) - 1
            t.update(1, l, r, delta)
            sum_len = xs[-1] - xs[0] - t.get_uncovered_length()
            records.append((tot_area, sum_len))
            tot_area += sum_len * (e2[0] - y)
        i = bisect_left(records, tot_area, key=lambda r: r[0] * 2) - 1
        area, sum_len = records[i]
        return events[i][0] + (tot_area - area * 2) / (sum_len * 2)