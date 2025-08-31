def findMaximumEngagement(balls):
    balls.sort(reverse = True) # 从大到小排列
    queue = []
    score = 0

    first = balls[0]
    queue.append(first)

    for ball in balls[1:]:
        max_contrib = 0
        insert = 0

        for i in range(len(queue)):
            left = queue[(i-1)%len(queue)] # 重要！
            right = queue[i]
            contrib = min(left, right)
            if contrib > max_contrib:
                max_contrib = contrib
                insert = i
        
        queue.insert(insert, ball)
        score += max_contrib

    return score


balls = [1, 3, 5, 3, 2]
print(findMaximumEngagement(balls))  # 输出 14