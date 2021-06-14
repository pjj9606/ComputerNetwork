import random

class YutNoLee():
    def __init__(self):
        self.SIZE = 5;
        self.origin_board = [[0 for j in range(0, self.SIZE)] for i in range(0, self.SIZE)]  # 복사용 임시변수
        self.board = [[0 for j in range(0, self.SIZE)] for i in range(0, self.SIZE)]
        self.termintae_flag = False
        self.__board_init()

    def __clean(self):
        self.origin_board = [[0 for j in range(0, self.SIZE)] for i in range(0, self.SIZE)]  # 복사용 임시변수
        self.board = [[0 for j in range(0, self.SIZE)] for i in range(0, self.SIZE)]
        self.termintae_flag = False


    # init 함수에서 선언한 클래스 멤버 초기화
    def __board_init(self):
        self.origin_board = [[0 for j in range(0, self.SIZE)] for i in range(0, self.SIZE)]


    # 인스턴스 변수 초기화
    def __clean(self):
        self.origin_board =[[0 for j in range(0, self.SIZE)] for i in range(0, self.SIZE)]
        self.termintae_flag = False


    # 윷 던짐
    def run_Yut(self):
        result = random.randInt(1,5)
        return result

    # 말 이동
    def move_Mal(self, num, team):
        a = 1

    def generate_YutNoLee(self):
        self.__clean()
        return self.board





