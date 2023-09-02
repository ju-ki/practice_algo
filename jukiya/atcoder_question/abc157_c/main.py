def main():
    # 入力を受け取る: Nは作成する数字の桁数, Mは制約条件の数
    N, M = map(int, input().split())

    # Sは制約がかかる桁の位置, Cはその桁の数字
    S, C = [], []

    # M回のループで制約の情報を受け取る
    for _ in range(M):
        s, c = map(int, input().split())
        # C++の0-indexingに合わせるため、sから1を引く
        S.append(s - 1)
        C.append(c)

    # 0から999までの数字で答えを探す
    for ans in range(1000):
        # 数字を文字列に変換
        s = str(ans)

        # 文字列の長さがNでない場合は次の数字を試す
        if len(s) != N:
            continue

        ok = True
        # 全ての制約に対してチェック
        for i in range(M):
            for j in range(N):
                # 制約がかかる桁と現在の桁が一致し、その数字が制約と一致しない場合
                if j == S[i] and int(s[j]) != C[i]:
                    # この数字は答えにならない
                    ok = False
                    break
            if not ok:
                break

        # 全ての制約を満たす数字が見つかった場合
        if ok:
            print(ans)
            return

    # 見つからなかった場合
    print(-1)


if __name__ == "__main__":
    # スクリプトとして実行されたときにmain関数を呼び出す
    main()
