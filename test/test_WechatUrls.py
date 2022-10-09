# coding: utf-8
import os
from pprint import pprint
from wechatarticles import PublicAccountsWeb

if __name__ == "__main__":
    # 模拟登录微信公众号平台，获取微信文章的url
    cookie = "appmsglist_action_2392642500=card; ua_id=wczETTqr2AuVGusWAAAAANP96f11qPW9vbQMWiYYDZA=; wxuin=65190337525378; rand_info=CAESIM1F8LtICOoryKV5c08seXd4UBPPjhfYo92noa2C6Sjr; slave_bizuin=2392642500; data_bizuin=2393318235; bizuin=2392642500; data_ticket=l3bTqQVV1T3y5xbhZngqrhUwvfVZLeEq+7t+ELXnQ6jga588NXJQLAg8qo4o9JK8; slave_sid=bzhnWWR6TGxDaE5lOW1XNDNLZXRuNFY4UURFSk1VM0RUQnYwSmpwWDUyMHFXZDV0V1UwSmVZazlnTnphQWhxdFRwemFXU0RIR3d3anBCWU9RRlBUWjJpbENfTmpzSUZkZEdBaGgzYzhLZVdNcWY3S2hDdTFJOGw4Z215SGVMaTljTm5yMmNSdnpzMGljN0U3; slave_user=gh_5d9b00ad18f4; xid=8202c0967286333c2fbe305c0d56c9ad; mm_lang=zh_CN; _clck=2392642500|1|f5k|0"
    token = "1393088205"
    nickname = "养花大全"
    biz="MzA5NzE0MTcyMQ=="

    paw = PublicAccountsWeb(cookie=cookie, token=token)
    # articles_sum = paw.articles_nums(nickname)
    article_data = paw.get_urls(nickname,biz, begin="0", count="5")
    # official_info = paw.official_info(nickname)

    # print("articles_sum:", end=" ")
    # print(articles_sum)
    print("artcles_data:")
    pprint(article_data)
    # print("official_info:")
    # pprint(official_info)
