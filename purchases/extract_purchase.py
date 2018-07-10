import re


class MakePurchaseHistory(object):
    def __init__(self):
        pass

    def make_purchase_history(self, response_json):
        a = self.__make_text_list(response_json)
        b = self.__make_purchase_dict(a)
        return b

    def __make_text_list(self, response_json):
        if isinstance(response_json, dict):
            key_list = ['responses', 'fullTextAnnotation', 'text']
            for n in key_list:
                if n in response_json:
                    return self.__make_text_list(response_json[n])

        elif isinstance(response_json, list):
            return self.__make_text_list(response_json[0])

        elif isinstance(response_json, str):
            return response_json.split('\n')

    def __make_purchase_dict(self, text_list):
        price_index = []
        i = 0

        for text in text_list:
            if text.startswith('¥'):
                price_index.append(text_list.index(text))
                i += 1
            elif i > 0:
                break

        goods_index = list(map(lambda tmp: tmp - i, price_index))

        goods_list = text_list[goods_index[0]:(goods_index[-1] + 1)]
        price_list = text_list[price_index[0]:(price_index[-1] + 1)]
        price_list_str = list(map(lambda p: re.sub(r'\D', '', p), price_list))
        price_list_int = list(map(lambda p: int(p), price_list_str))

        purchase_history = tuple(zip(goods_list, price_list_int))

        return purchase_history
