class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def is_possible(capacity: int) -> bool:
            total_days = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight > capacity:
                    total_days += 1
                    current_weight = weight
                else:
                    current_weight += weight

            return total_days <= days

        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = low + (high - low) // 2

            if is_possible(mid):
                high = mid  # Try a smaller capacity
            else:
                low = mid + 1  # Capacity is too small, increase it

        return low