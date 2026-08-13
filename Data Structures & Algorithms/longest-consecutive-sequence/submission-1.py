class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        remaining = set(nums)
        max_length = 0
        sequence_lengths = {} # sequence length by start value

        for current_num in nums:
            if current_num not in remaining:
                continue # skip because it's been processed already
            
            sequence_end = current_num
            # Find the end of the sequence (first number not in the sequence from remaining)
            while sequence_end in remaining:
                remaining.remove(sequence_end)
                sequence_end += 1

            # Find the current length and add previous calculated
            # sequence length starting at the end
            current_length = (sequence_end - current_num) + sequence_lengths.get(sequence_end, 0)
            sequence_lengths.pop(sequence_end, None)
            
            # Update the sequence_lengths, and max_length if needed
            sequence_lengths[current_num] = current_length
            max_length = max(max_length, current_length)
        
        return max_length