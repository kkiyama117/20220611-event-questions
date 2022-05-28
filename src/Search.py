def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)


def serch_index(sorted_array, target_number):

    # ここから記述

    # 属に言う二分探索
    # 配列の探索部分の両端および中央値の添字(初期値は配列長の1/2,端数切り捨て)
    left_index = 0
    right_index = len(sorted_array) - 1
    while left_index <= right_index:
        # index及び探索中の数値更新
        index = (left_index + right_index) // 2
        array_target = sorted_array[index]

        # 探索数値と一致した場合即indexを返却
        if array_target == target_number:
            return index
        # 探索数値が中央値以下なら次回index未満の部分を探索
        elif array_target > target_number:
            right_index = index - 1
        # 探索数値が中央値以上なら次回indexより大きい部分を探索
        else:
            left_index = index + 1
        print(left_index, index, right_index)

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1


if __name__ == "__main__":
    main()
