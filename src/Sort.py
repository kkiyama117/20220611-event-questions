def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]


def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    # 挿入ソート的な処理の実装

    # 左右の探索のindexを保存
    left_index, right_index = 0, 0

    # 左右の探索がぶつかるまで走査．do-whileのように一回処理が入る.
    while True:
        right_found = False
        left_found = False
        # ぶつかるまでで検索して変数に保持
        for idx in range(left_index, len(array)):
            # 見つかったらそのindexを保存して右からの検索を打ち切る．
            if array[idx] >= pivot:
                left_index = idx
                left_found = True
                break
        for idx in reversed(range(left_index, len(array))):
            # 見つかったらそのindexを保存して左からの検索を打ち切る．
            if array[idx] < pivot:
                right_index = idx
                right_found = True
                break
        # どちらでもみつかっていた場合のみ入れ替える．
        if left_found and right_found:
            array[left_index], array[right_index] = (
                array[right_index],
                array[left_index],
            )
        # そうでない場合はこれ以上入れ替えられないので分割して次の再帰へ.
        else:
            # この時検索がぶつかり未走査だとright_indexは正しい値を差さないので一回は捜査されるleft_index基準にする.
            # left_index == 0 (かつどちらかが未走査になる)の時のみ1個と残りに分ける.
            if left_index == 0:
                return [*sort(array[: left_index + 1]), *sort(array[left_index + 1 :])]
            else:
                return [*sort(array[:left_index]), *sort(array[left_index:])]
        # ぶつかっていたら全体の処理を終了し次の再帰へ．
        if left_index == right_index - 1:
            break
    # 次の再帰．
    return [*sort(array[:right_index]), *sort(array[right_index:])]
    # ここまで記述


if __name__ == "__main__":
    main()
