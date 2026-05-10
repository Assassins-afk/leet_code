class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_val = max(nums)

        is_prime = [True] * (max_val + 1)
        if max_val >= 0:
            is_prime[0] = False
        if max_val >= 1:
            is_prime[1] = False

        for i in range(2, int(max_val ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_val + 1, i):
                    is_prime[j] = False

        prime_to_indices = defaultdict(list)

        for i, num in enumerate(nums):
            temp = num
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    if is_prime[d]:
                        prime_to_indices[d].append(i)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1 and is_prime[temp]:
                prime_to_indices[temp].append(i)

        queue = deque([(0, 0)])
        visited = [False] * n
        visited[0] = True
        used_primes = set()

        while queue:
            index, steps = queue.popleft()

            if index == n - 1:
                return steps

            for next_idx in (index - 1, index + 1):
                if 0 <= next_idx < n and not visited[next_idx]:
                    visited[next_idx] = True
                    queue.append((next_idx, steps + 1))
            
            num = nums[index]
            if is_prime[num] and num not in used_primes:
                used_primes.add(num)

                for target in prime_to_indices.get(num, []):
                    if target != index and not visited[target]:
                        visited[target] = True
                        queue.append((target, steps + 1))
        return -1