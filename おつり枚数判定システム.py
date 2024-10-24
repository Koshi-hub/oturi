def calculate_change(total_amount, product_price):
    # 硬貨の種類
    coins = [500, 100, 50, 10]
    change = total_amount - product_price

    if change < 0:
        return "投入金額が不足しています。"

    coin_count = {}
    
    for coin in coins:
        if change == 0:
            break
        count = change // coin
        if count > 0:
            coin_count[coin] = count
            change -= coin * count

    return coin_count

def main():
    print("おつりの枚数判定システム")
    total_amount = int(input("投入金額を入力してください: "))
    product_price = int(input("商品の価格を入力してください: "))
    
    change = calculate_change(total_amount, product_price)
    
    if isinstance(change, str):
        print(change)
    else:
        print("おつりの枚数:")
        for coin, count in change.items():
            print(f"{coin}円: {count}枚")

if __name__ == "__main__":
    main()
