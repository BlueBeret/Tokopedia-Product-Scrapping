import requests
import json
from random import randint
import time
import signal
base_url = "https://gql.tokopedia.com/graphql/RecommendationFeedQuery"


headers =  {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "x-device": "desktop-0.0",
    "x-source": "tokopedia-lite",
    "x-tkpd-lite-service": "zeus",
    "x-version": "09853d2",
    "referrer": "https://www.tokopedia.com/"
  }




with open('tokopedia/links.json', 'r') as fi:
    links = json.load(fi)

def handler(signum, frame):
    res = input('exit? y/n')
    if res== 'y':
        with open('tokopedia/links.json', 'w') as fo:
            json.dump(links, fo)

        exit(1)


signal.signal(signal.SIGINT, handler)

try:
    counter = 0
    for kota in range(17,300):
        for district in range(100):
            
            hasNextPage = True
            pageNumber = 0
            print(len(links),counter, kota, district)
            counter = 0
            try:
                while hasNextPage:
                    pageNumber +=1
                    data = "[{\"operationName\":\"RecommendationFeedQuery\",\"variables\":{\"recomID\":1,\"type\":\"banner, banner_ads, position\",\"count\":20,\"page\":"+str(pageNumber)+",\"pageType\":\"home\",\"categoryVisited\":\"\",\"productVisited\":\"\",\"location\":\"user_addressId=0&user_cityId="+str(kota)+"&user_districtId="+str(district)+"&user_lat=&user_long=&user_postCode=\"},\"query\":\"query RecommendationFeedQuery($recomID: Int, $type: String!, $count: Int!, $page: Int!, $pageType: String, $categoryVisited: String, $productVisited: String, $location: String) {\\n  get_home_recommendation(page: $pageType, category_visited: $categoryVisited, product_visited: $productVisited, location: $location) {\\n    recommendation_tabs {\\n      id\\n      name\\n      imageUrl: image_url\\n      __typename\\n    }\\n    recommendation_product(recomID: $recomID, count: $count, page: $page, type: $type) {\\n      pageName\\n      product {\\n        id\\n        name\\n        category: category_breadcrumbs\\n        url\\n        clickUrl: click_url\\n        clusterID\\n        isWishlist: is_wishlist\\n        imageURL: image_url\\n        isTopads: is_topads\\n        trackerImageUrl: tracker_image_url\\n        price\\n        priceInt: price_int\\n        slashedPrice: slashed_price\\n        slashedPriceInt: slashed_price_int\\n        discountPercentage: discount_percentage\\n        isRating: is_rating\\n        rating\\n        ratingAverage\\n        countReview: count_review\\n        recommendationType: recommendation_type\\n        isShop: is_shop\\n        shop {\\n          shopID: id\\n          name\\n          url\\n          city\\n          __typename\\n        }\\n        labelGroups: label_group {\\n          type\\n          title\\n          position\\n          url\\n          __typename\\n        }\\n        badges {\\n          title\\n          image_url\\n          __typename\\n        }\\n        __typename\\n      }\\n      banner {\\n        id\\n        name\\n        imageURL: image_url\\n        url\\n        buAttribution: bu_attribution\\n        creativeName: creative_name\\n        target\\n        __typename\\n      }\\n      position {\\n        type\\n        __typename\\n      }\\n      hasNextPage: has_next_page\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}]"
                    res = requests.post(
                        'https://gql.tokopedia.com/graphql/RecommendationFeedQuery',
                        data=data,
                        headers=headers
                    )

                    data = res.json()[0]
                    products = data['data']['get_home_recommendation']['recommendation_product']['product']
                    hasNextPage = data['data']['get_home_recommendation']['recommendation_product']['hasNextPage']
                    for i in products:
                        link_and_image = {
                            'link': i['url'],
                            'img_url': i['imageURL']
                        }
                        if link_and_image not in links:
                            links.append(link_and_image)
                            counter += 1
            except Exception as e:
                print(e)

except Exception as e:
    print(e)





with open('tokopedia/links.json', 'w') as fo:
    json.dump(links, fo)