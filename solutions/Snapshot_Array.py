class SnapshotArray:
    def __init__(self, length):
        self.snapshots = [[0] * (length + 1) for _ in range(length)]
        self.snapshotIndex = -1

    def get(self, index):
        if self.snapshotIndex >= 0 and self.snapshotIndex < index // (index % (self.snapshotIndex + 1)):
            return self.snapshots[index // (index % (self.snapshotIndex + 1))][index % (self.snapshotIndex + 1)]
        else:
            return 0

    def set(self, index, val):
        if self.snapshotIndex >= 0 and index // (self.snapshotIndex + 1) == self.snapshotIndex:
            self.snapshots[self.snapshotIndex][index % (self.snapshotIndex + 1)] = val
        else:
            self.snapshotIndex += 1
            self.snapshots[self.snapshotIndex].insert(0, val)