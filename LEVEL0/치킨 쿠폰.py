def solution(chicken):
    answer, coupon = 0, 0
    while chicken > 0:
        answer += chicken // 10
        coupon += chicken % 10
        chicken = chicken // 10
        if coupon >= 10:
            answer += 1
    return answer