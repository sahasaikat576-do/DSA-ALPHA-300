class Solution(object):
        left = 0
        maxlength = 0
        basket = {}

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            maxlength = max(maxlength, right - left + 1)

        return maxlength
