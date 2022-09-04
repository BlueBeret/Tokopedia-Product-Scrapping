from email import header
import requests
import json
from random import randint
import time
import signal
from tqdm import tqdm




base_url = "https://gql.tokopedia.com/graphql/PDPGetLayoutQuery"


headers =  {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,id;q=0.8",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "x-device": "desktop",
    "x-source": "tokopedia-lite",
    "x-tkpd-akamai": "pdpGetLayout",
    "x-tkpd-lite-service": "zeus",
    "x-version": "09853d2",
    "method": "POST",
  "mode": "cors",
  "credentials": "include"
  }

data_details = []
with open('tokopedia/done_tokopedia.txt') as fi:
    done = json.load(fi)
links_filename = 'tokopedia/links.json'
data_details_filename = 'tokopedia/data_details2.json'

with open(links_filename, 'r') as fi:
    links = json.load(fi)



def handler(signum, frame):
    res = input('exit? y/n')
    if res== 'y':
        with open(data_details_filename, 'w') as fo:
            json.dump(data_details, fo)
        with open('tokopedia/done_tokopedia.txt', 'w') as fo:
            json.dump(done, fo)
        exit(1)


signal.signal(signal.SIGINT, handler)
link = ""
try:
    for link in tqdm(links):
        if link in done:
            continue
        temp = link['link'].split('/')
        shopDomain = temp[3]
        productKey = temp[4]

        data = "[{\"operationName\":\"PDPGetLayoutQuery\",\"variables\":{\"shopDomain\":\""+shopDomain+"\",\"productKey\":\""+productKey+"\",\"layoutID\":\"\",\"apiVersion\":1,\"userLocation\":{\"cityID\":\"176\",\"addressID\":\"0\",\"districtID\":\"2274\",\"postalCode\":\"\",\"latlon\":\"\"},\"extParam\":\"\"},\"query\":\"fragment ProductVariant on pdpDataProductVariant {\\n  errorCode\\n  parentID\\n  defaultChild\\n  sizeChart\\n  totalStockFmt\\n  variants {\\n    productVariantID\\n    variantID\\n    name\\n    identifier\\n    option {\\n      picture {\\n        urlOriginal: url\\n        urlThumbnail: url100\\n        __typename\\n      }\\n      productVariantOptionID\\n      variantUnitValueID\\n      value\\n      hex\\n      stock\\n      __typename\\n    }\\n    __typename\\n  }\\n  children {\\n    productID\\n    price\\n    priceFmt\\n    optionID\\n    productName\\n    productURL\\n    picture {\\n      urlOriginal: url\\n      urlThumbnail: url100\\n      __typename\\n    }\\n    stock {\\n      stock\\n      isBuyable\\n      stockWordingHTML\\n      minimumOrder\\n      maximumOrder\\n      __typename\\n    }\\n    isCOD\\n    isWishlist\\n    campaignInfo {\\n      campaignID\\n      campaignType\\n      campaignTypeName\\n      campaignIdentifier\\n      background\\n      discountPercentage\\n      originalPrice\\n      discountPrice\\n      stock\\n      stockSoldPercentage\\n      startDate\\n      endDate\\n      endDateUnix\\n      appLinks\\n      isAppsOnly\\n      isActive\\n      hideGimmick\\n      isCheckImei\\n      minOrder\\n      __typename\\n    }\\n    thematicCampaign {\\n      additionalInfo\\n      background\\n      campaignName\\n      icon\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductMedia on pdpDataProductMedia {\\n  media {\\n    type\\n    urlOriginal: URLOriginal\\n    urlThumbnail: URLThumbnail\\n    videoUrl: videoURLAndroid\\n    prefix\\n    suffix\\n    description\\n    variantOptionID\\n    __typename\\n  }\\n  videos {\\n    source\\n    url\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductHighlight on pdpDataProductContent {\\n  name\\n  price {\\n    value\\n    currency\\n    __typename\\n  }\\n  campaign {\\n    campaignID\\n    campaignType\\n    campaignTypeName\\n    campaignIdentifier\\n    background\\n    percentageAmount\\n    originalPrice\\n    discountedPrice\\n    originalStock\\n    stock\\n    stockSoldPercentage\\n    threshold\\n    startDate\\n    endDate\\n    endDateUnix\\n    appLinks\\n    isAppsOnly\\n    isActive\\n    hideGimmick\\n    __typename\\n  }\\n  thematicCampaign {\\n    additionalInfo\\n    background\\n    campaignName\\n    icon\\n    __typename\\n  }\\n  stock {\\n    useStock\\n    value\\n    stockWording\\n    __typename\\n  }\\n  variant {\\n    isVariant\\n    parentID\\n    __typename\\n  }\\n  wholesale {\\n    minQty\\n    price {\\n      value\\n      currency\\n      __typename\\n    }\\n    __typename\\n  }\\n  isCashback {\\n    percentage\\n    __typename\\n  }\\n  isTradeIn\\n  isOS\\n  isPowerMerchant\\n  isWishlist\\n  isCOD\\n  isFreeOngkir {\\n    isActive\\n    __typename\\n  }\\n  preorder {\\n    duration\\n    timeUnit\\n    isActive\\n    preorderInDays\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductCustomInfo on pdpDataCustomInfo {\\n  icon\\n  title\\n  isApplink\\n  applink\\n  separator\\n  description\\n  __typename\\n}\\n\\nfragment ProductInfo on pdpDataProductInfo {\\n  row\\n  content {\\n    title\\n    subtitle\\n    applink\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductDetail on pdpDataProductDetail {\\n  content {\\n    title\\n    subtitle\\n    applink\\n    showAtFront\\n    isAnnotation\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductDataInfo on pdpDataInfo {\\n  icon\\n  title\\n  isApplink\\n  applink\\n  content {\\n    icon\\n    text\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment ProductSocial on pdpDataSocialProof {\\n  row\\n  content {\\n    icon\\n    title\\n    subtitle\\n    applink\\n    type\\n    rating\\n    __typename\\n  }\\n  __typename\\n}\\n\\nquery PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation, $extParam: String) {\\n  pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation, extParam: $extParam) {\\n    name\\n    pdpSession\\n    basicInfo {\\n      alias\\n      isQA\\n      id: productID\\n      shopID\\n      shopName\\n      minOrder\\n      maxOrder\\n      weight\\n      weightUnit\\n      condition\\n      status\\n      url\\n      needPrescription\\n      catalogID\\n      isLeasing\\n      isBlacklisted\\n      menu {\\n        id\\n        name\\n        url\\n        __typename\\n      }\\n      category {\\n        id\\n        name\\n        title\\n        breadcrumbURL\\n        isAdult\\n        isKyc\\n        minAge\\n        detail {\\n          id\\n          name\\n          breadcrumbURL\\n          isAdult\\n          __typename\\n        }\\n        __typename\\n      }\\n      txStats {\\n        transactionSuccess\\n        transactionReject\\n        countSold\\n        paymentVerified\\n        itemSoldFmt\\n        __typename\\n      }\\n      stats {\\n        countView\\n        countReview\\n        countTalk\\n        rating\\n        __typename\\n      }\\n      __typename\\n    }\\n    components {\\n      name\\n      type\\n      position\\n      data {\\n        ...ProductMedia\\n        ...ProductHighlight\\n        ...ProductInfo\\n        ...ProductDetail\\n        ...ProductSocial\\n        ...ProductDataInfo\\n        ...ProductCustomInfo\\n        ...ProductVariant\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}]"


        res = requests.post(base_url, data=data, headers=headers)
        res = res.json()[0]['data']['pdpGetLayout']
        product_content = res['components'][3]
        assert product_content['name'] == 'product_content'
        product_content = product_content['data'][0]

        product_detail = res['components'][4]
        assert product_detail['name'] == 'product_detail'
        product_detail = product_detail['data'][0]['content']

        deskripsi = ""
        spesifikasi = ""
        for i in product_detail:
            if i['title'] == 'Deskripsi':
                deskripsi = i['subtitle']
                continue
            spesifikasi += i['title'] + '\n' + i['subtitle'] + '\n'


        product_name = product_content['name']
        price_1 = product_content['price']['value'] if product_content['campaign']['originalPrice'] == 0  else product_content['campaign']['originalPrice']
        dis_price_1 =  product_content['campaign']['discountedPrice']
        rating = res['basicInfo']['stats']['rating']
        rating_people = res['basicInfo']['stats']['countReview']
        sold = res['basicInfo']['txStats']['countSold']

        data = {
            "product_name":product_name,
            "rating" : rating,
            "rating_people": rating_people,
            "sold": sold,
            "price_1": price_1,
            "dis_price_1": dis_price_1,
            "price_2": "",
            "dis_price_2": "",
            "price_3": "",
            "spesifikasi": spesifikasi,
            "deskripsi": deskripsi,
            "Page_URL": link
        }

        data_details.append(data)
        done.append(link)



except Exception as e:
    print(e)
    print(link)


with open(data_details_filename, 'w') as fo:
    json.dump(data_details, fo)
with open('tokopedia/done_tokopedia.txt', 'w') as fo:
    json.dump(done, fo)


