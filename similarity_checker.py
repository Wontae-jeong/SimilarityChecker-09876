class SimilarityChecker:
    def set_strings(self, string1, string2):
        self.__string1 = string1
        self.__string2 = string2

    def get_score1(self) -> float:
        len_a = max(len(self.__string1), len(self.__string2))
        len_b = min(len(self.__string1), len(self.__string2))
        if len_a >= len_b * 2:
            return 0

        return round((1.0 - float((len_a - len_b) / len_b)) * 60, 1)

    def get_score2(self) -> float:
        str1_charset: set = set(char for char in self.__string1)
        str2_charset: set = set(char for char in self.__string2)
        total_cnt = len(str1_charset.union(str2_charset))
        same_cnt = len(str1_charset.intersection(str2_charset))
        return (same_cnt / total_cnt) * 40
