def solution(phone_book):
    # 해시 테이블 생성
    hash_table = {}
    
    # 전화번로를 해시 테이블에 저장
    for phone_num in phone_book:
        hash_table[phone_num] = True
        
    # 각 전화번호의 일부를 해시값으로 변환하여 접두어 관계를 확인한다
    for phone_num in phone_book:
        pre = ""
        for digit in phone_num:
            pre += digit 
            if pre != phone_num and pre in hash_table:
                return False 
    # 모든 경우의 수를 다 했는데도 안되면 True를 리턴
    return True
    